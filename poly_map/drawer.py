#!/usr/bin/env python
import random
import numpy as np
import cv2
image = cv2.imread("../gtasa-blank-vector.png")

grove = (50, 200, 50)
ballas = (140, 0, 140)
vagos = (0, 215, 255)
aztecas = (225, 255, 0)
mcb = (70, 70, 70)
rgt = (60, 20, 220)
dnb = (11, 134, 184)
rifas = (170, 178, 32)
leone = (0, 0, 130)
forelli = (150, 0, 0)
sindacco = (13, 13, 13)
black = (0, 0, 0)
colors = [grove, ballas, vagos, aztecas, mcb, rgt, dnb, rifas, leone, forelli, sindacco, black]

ganton = np.array([[1438, 1186], [1438, 1239], [1337, 1239], [1337, 1186], [1438, 1186]])
idlewood = np.array([[1337, 1239], [1337, 1150], [1310, 1150], [1310, 1140], [1231, 1140], [1231, 1239], [1337, 1239]])
little_mexico = np.array([[1230, 1240], [1201, 1240], [1201, 1211], [1217, 1211], [1217, 1170], [1230, 1170], [1230, 1240]])
unity_station = np.array([[1230, 1240], [1230, 1268], [1197, 1268], [1197, 1240], [1230, 1240]])
el_corona = np.array([[1197, 1269], [1197, 1329], [1271, 1329], [1271, 1240], [1230, 1240], [1230, 1269], [1197, 1269]])
glen_park = np.array([[1231, 1139], [1231, 1018], [1286, 1018], [1286, 1053], [1294, 1053], [1294, 1114], [1278, 1114], [1278, 1139], [1231, 1139]])
jefferson = np.array([[1279, 1139], [1279, 1115], [1295, 1115], [1295, 1056], [1326, 1056], [1326, 1064], [1350, 1064], [1350, 1149], [1311, 1149], [1311, 1139], [1279, 1139]])
east_los_santos = np.array([[1338, 1185], [1338, 1150], [1351, 1150], [1351, 1061], [1428, 1061], [1428, 1145], [1442, 1145], [1442, 1185]])
mulholland_intersection = np.array([[1144, 1065], [1144, 963], [1230, 963], [1230, 1065], [1144, 1065]])
downtown_los_santos = np.array([[1230, 1066], [1143, 1066], [1143, 1006], [1123, 1006], [1123, 1031], [1120, 1031], [1120, 1124], [1142, 1124], [1142, 1134], [1230, 1134], [1230, 1066]])
commerce = np.array([[1200, 1239], [1106, 1239], [1106, 1169], [1120, 1169], [1120, 1125], [1141, 1125], [1141, 1135], [1230, 1135], [1230, 1169], [1216, 1169], [1216, 1210], [1200, 1210], [1200, 1239]])
zones = [ganton, idlewood, little_mexico, unity_station, el_corona, glen_park, jefferson, east_los_santos, mulholland_intersection, downtown_los_santos]

for i in zones:
	cv2.fillPoly(image, [i], random.choice(colors))
	# cv2.polylines(image, [i], True, black, thickness=2)
cv2.namedWindow('test map', cv2.WINDOW_NORMAL)
cv2.imshow("test map", image)
cv2.waitKey(0)
cv2.imwrite('test_map.png', image)
