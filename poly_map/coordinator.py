#!/usr/bin/env python
import cv2
right_clicks = list()
def mouse_callback(event, x, y, flags, params):
    if event == 2:
        global right_clicks
        right_clicks.append([x, y])
        print right_clicks
img = cv2.imread("test_map.png")
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.setMouseCallback('image', mouse_callback)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()