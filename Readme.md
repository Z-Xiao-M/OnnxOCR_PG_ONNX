如果项目对您有帮助，欢迎点击右上角 **Star** 支持！✨  
## **原OnnxOCR** (https://github.com/jingsongliujing/OnnxOCR)
- 本项目仅作为实验 验证了在PostgreSQL中运行onnx模型的可行性 所以本项目还依赖[postgres](https://github.com/postgres/postgres)和[pg_onnx](https://github.com/kibae/pg_onnx)

## **环境安装** 
```bash  
python>=3.6  

pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt  
```  

## **注意**：  
- 数据库的配置位于config.py 按照实际的情况配置
- 在确定了数据库之后 需要创建pg_onnx拓展 导入相关模型 导入模型语句如下(这里我没有使用cuda 可以考虑实际情况配置)
```sql
SELECT pg_onnx_import_model(
               'cls',
               'v1', 
               PG_READ_BINARY_FILE('你的代码路径/OnnxOCR_PG_ONNX/onnxocr/models/ppocrv5/cls/cls.onnx')::bytea,
               '{"cuda": false}'::jsonb, 
               '相关描述'
       );

SELECT pg_onnx_import_model(
               'det',
               'v1', 
               PG_READ_BINARY_FILE('你的代码路径/OnnxOCR_PG_ONNX/onnxocr/models/ppocrv5/det/det.onnx')::bytea,
               '{"cuda": false}'::jsonb, 
               '相关描述'
       );

SELECT pg_onnx_import_model(
               'rec',
               'v1', 
               PG_READ_BINARY_FILE('你的代码路径/OnnxOCR_PG_ONNX/onnxocr/models/ppocrv5/rec/rec.onnx')::bytea,
               '{"cuda": false}'::jsonb, 
               '相关描述'
       );
```

## **一键运行**
```bash  
python test_ocr.py  
```  

## **结果**
```bash
(onnx-env) postgres@zxm-VMware-Virtual-Platform:~/OnnxOCR_PG_ONNX$ python test_ocr.py
total time: 29.654
[[[92.0, 198.0], [742.0, 175.0], [747.0, 305.0], [97.0, 328.0]], ('姓名奥巴马', 0.9977725505828857)]
[[[90.0, 415.0], [1328.0, 396.0], [1331.0, 538.0], [92.0, 556.0]], ('性别男民族肯尼亚', 0.9989805296063423)]
[[[90.0, 646.0], [1397.0, 637.0], [1397.0, 758.0], [91.0, 767.0]], ('出生1961年8月4日', 0.9986594644459811)]
[[[98.0, 885.0], [375.0, 892.0], [372.0, 994.0], [96.0, 986.0]], ('住址', 0.9953028857707977)]
[[[377.0, 892.0], [1522.0, 883.0], [1523.0, 1001.0], [378.0, 1011.0]], ('华盛顿特区宜宾法尼亚', 0.9969237744808197)]
[[[392.0, 1083.0], [1207.0, 1083.0], [1207.0, 1210.0], [392.0, 1210.0]], ('大道1600号白宫', 0.9857945972018771)]
[[[83.0, 1467.0], [752.0, 1474.0], [750.0, 1595.0], [81.0, 1589.0]], ('公民身份号码', 0.9998583197593689)]
[[[923.0, 1483.0], [2384.0, 1461.0], [2386.0, 1592.0], [925.0, 1613.0]], ('123456196108047890', 0.996591372622384)]
```

## 声明
`test.jpg`图片来自(https://github.com/tuyuai/TuYuIDCard/tree/master/images)