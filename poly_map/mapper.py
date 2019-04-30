import numpy as np
import cv2
image = cv2.imread("../gtasa-blank-vector.png")
blue = (255, 0, 0)
los_santos = np.array([[1123.07,948.874],[794.348,1018.21],[800.009,1535.48],[1535.5,1535.48],[1535.72,1036.76],[1123.07,948.87]], np.int32)
cv2.polylines(image, [los_santos], True, blue, thickness=30)
# cv2.imwrite('test.png', image)
cv2.namedWindow('blue polygon', cv2.WINDOW_NORMAL)
cv2.imshow("blue polygon", image)
cv2.waitKey(0)