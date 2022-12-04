#imports
import csv
import sys
import math
import clr
import time
import System
from System import Byte

clr.AddReference("MissionPlanner")
import MissionPlanner
clr.AddReference("MissionPlanner.Utilities") # includes the Utilities class
from MissionPlanner.Utilities import Locationwp
clr.AddReference("MAVLink") # includes the Utilities class
import MAVLink
idmavcmd = MAVLink.MAV_CMD.WAYPOINT
id = int(idmavcmd)

test = 1
while test < 5:
    print("Test: ", test)
    test += 1
    time.sleep(1)

target_lat = [38.3143699, 38.3143152, 38.3143152, 38.3143742, 38.3144794]
target_long = [-76.5450177, -76.5447387, -76.5443256,-76.5441540, -76.5447119]
target_id = []
#altitude is 26 meters, approximately 85 feet high
alt = 26
#number of waypoints
wp = [0] * len(target_lat)

#set RTH/RTL and flight termination point
home = Locationwp().Set(38.315339, -76.548108, 0, id)

#set waypoints for payload delivery
for i in range (0, len(target_lat)):
    wp[i] = Locationwp().Set(target_lat[i], target_long[i], alt, id)

#upload waypoints for payload delivery
for i in range (0, len(target_lat)):
    print("upload waypoint ", i, "for payload delivery")
    MAV.setWP(wp[i], i, MAVLink.MAV_FRAME.GLOBAL_RELATIVE_ALT);

print("uploaded all waypoints for payload delivery")
MAV.setWPACK();