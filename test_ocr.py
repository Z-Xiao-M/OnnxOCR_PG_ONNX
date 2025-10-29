import cv2
import time
from onnxocr.onnx_paddleocr import ONNXPaddleOcr,sav2Img
import sys
import time
from db.connection import close_pg_onnx_connection
#固定到onnx路径·
# sys.path.append('./paddle_to_onnx/onnx')

model = ONNXPaddleOcr(use_angle_cls=True, use_gpu=False)


img = cv2.imread('test.jpg')
s = time.time()
result = model.ocr(img)
e = time.time()
print("total time: {:.3f}".format(e - s))
# print("result:", result)
for box in result[0]:
    print(box)

close_pg_onnx_connection()
# sav2Img(img, result,name=str(time.time())+'.jpg')