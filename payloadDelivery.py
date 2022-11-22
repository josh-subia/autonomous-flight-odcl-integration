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

target_lat = []
target_long = []
target_id = []
#altitude is 26 meters, approximately 85 feet high
alt = 26
#num_wps

#set waypoints for payload delivery
for i in range (0, len(target_lat)):
    wp[i] = Locationwp().Set(lat[i], long[i], alt, id)

#upload waypoints for payload delivery
for i in range (0, len(target_lat)):
    print("upload waypoint ", i, "for payload delivery")
    MAV.setWP(wp[i], i, MAVLink.MAV_FRAME.GLOBAL_RELATIVE_ALT);

print("uploaded all waypoints for payload delivery")
MAV.setWPACK();