#!/usr/bin/env python
# import matplotlib.pyplot as plt
# import matplotlib.image as mpimg
# img=mpimg.imread('../gtasa-blank-vector.png')
# imgplot = plt.imshow(img)
# plt.show()
import numpy as np
import cv2
image = cv2.imread("../gtasa-blank-vector.png")
grove = (50, 200, 50); ballas = (140, 0, 140); vagos = (0, 215, 255); aztecas = (225, 255, 0); mcb = (70, 70, 70); rgt = (60, 20, 220); dnb = (11, 134, 184); rifas = (170, 178, 32); leone = (0, 0, 130); forelli = (150, 0, 0); sindacco = (13, 13, 13)
ganton = np.array([[1438.11,1186.01],[1438.11,1239.6],[1337.11,1239.6],[1337.11,1186.01],[1438.11,1186.01]], np.int32)
cv2.fillPoly(image, [ganton], sindacco)
cv2.namedWindow('test map', cv2.WINDOW_NORMAL)
cv2.imshow("test map", image)
cv2.waitKey(0)
cv2.imwrite('test_map.png', image)