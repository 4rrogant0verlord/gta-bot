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
los_flores = np.array([[1429, 1061], [1469, 1061], [1469, 1126], [1442, 1126], [1442, 1144], [1429, 1144], [1429, 1061]])
east_beach = np.array([[1470, 1061], [1525, 1061], [1525, 1239], [1439, 1239], [1439, 1186], [1443, 1186], [1443, 1127], [1470, 1127], [1470, 1061]])
willow_field = np.array([[1272, 1240], [1460, 1240], [1460, 1296], [1331, 1296], [1331, 1329], [1272, 1329], [1272, 1240]])
playa_del_seville = np.array([[1461, 1240], [1461, 1310], [1525, 1310], [1525, 1240], [1461, 1240]])
north_ocean_docks = np.array([[1525, 1311], [1525, 1354], [1357, 1354], [1357, 1380], [1272, 1380], [1272, 1330], [1332, 1330], [1332, 1297], [1460, 1297], [1460, 1311], [1525, 1311]])
south_ocean_docks = np.array([[1374, 1363], [1374, 1459], [1488, 1459], [1488, 1363], [1374, 1363]])
las_colinas = np.array([[1287, 1008], [1525, 1008], [1525, 1060], [1350, 1060], [1350, 1063], [1327, 1063], [1327, 1055], [1295, 1055], [1295, 1052], [1287, 1052], [1287, 1008]])
los_santos_airport = np.array([[1327, 1381], [1327, 1464], [1124, 1464], [1124, 1380], [1087, 1380], [1087, 1330], [1271, 1330], [1271, 1381], [1327, 1381]])
verdant_bluffs = np.array([[1041, 1239], [1041, 1278], [1010, 1278], [1010, 1405], [1086, 1405], [1086, 1329], [1196, 1329], [1196, 1240], [1041, 1239]])
conference_center = np.array([[1105, 1207], [1041, 1206], [1041, 1238], [1105, 1238], [1105, 1207]])
zones = [
	ganton,
	idlewood,
	little_mexico,
	unity_station,
	el_corona,
	glen_park,
	jefferson,
	east_los_santos,
	mulholland_intersection,
	downtown_los_santos,
	commerce,
	los_flores,
	east_beach,
	willow_field,
	playa_del_seville,
	north_ocean_docks,
	south_ocean_docks,
	las_colinas,
	los_santos_airport,
	verdant_bluffs,
	conference_center
	]

for i in zones:
	cv2.fillPoly(image, [i], random.choice(colors))
	# cv2.polylines(image, [i], True, black, thickness=2)
cv2.namedWindow('test map', cv2.WINDOW_NORMAL)
cv2.imshow("test map", image)
cv2.waitKey(0)
cv2.imwrite('test_map.png', image)
