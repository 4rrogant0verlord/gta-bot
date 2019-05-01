#!/usr/bin/env python
import numpy as np
import cv2
image = cv2.imread("../gtasa-blank-vector.png")

cv2.namedWindow('test map', cv2.WINDOW_NORMAL)
cv2.imshow("test map", image)
cv2.waitKey(0)
cv2.imwrite('test_map.png', image)

# ganton = np.array([[1438,1186],[1438,1239],[1337,1239],[1337,1186],[1438,1186]])
# cv2.fillPoly(image, [ganton], grove)
# cv2.polylines(image, [ganton], True, black, thickness=2)