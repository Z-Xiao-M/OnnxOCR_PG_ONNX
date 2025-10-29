import psycopg2
import json
from config import DB_CONFIG

# 全局单例连接（内部维护，不暴露给外部）
_g_conn = None


def _get_conn():
    global _g_conn
    # 连接未创建或已关闭，重建连接
    if _g_conn is None or _g_conn.closed != 0:
        try:
            _g_conn = psycopg2.connect(**DB_CONFIG)
        except Exception as e:
            raise RuntimeError(f"创建数据库连接失败: {str(e)}")
    return _g_conn


def pg_onnx_infer(model_name, model_version, input_data):
    conn = _get_conn()  # 复用全局连接
    cur = None
    try:
        cur = conn.cursor()  # 每次推理创建新游标（避免冲突）
        input_json = json.dumps(input_data)
        cur.execute("""
            SELECT pg_onnx_execute_session(%s, %s, %s::jsonb);
        """, (model_name, model_version, input_json))
        output = cur.fetchone()[0]
        return output
    except Exception as e:
        conn.rollback()  # 出错回滚
        raise RuntimeError(f"推理执行失败: {str(e)}")
    finally:
        if cur:
            cur.close()  # 游标用完即关（连接保持打开）


def close_pg_onnx_connection():
    global _g_conn
    if _g_conn is not None and _g_conn.closed == 0:
        _g_conn.close()
        _g_conn = None
    else:
        print("无活跃连接可关闭")
