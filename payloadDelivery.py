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

target_lat = [38.3143699, 38.3143152, 38.3143152, 38.3143742, 38.3144794]
target_long = [-76.5450177 -76.5447387 -76.5443256 -76.5441540 -76.5447119]
target_id = []
#altitude is 26 meters, approximately 85 feet high
alt = 26
#num_wps

#number of waypoints
wp = [] * len(target_lat)

#set RTH/RTL and flight termination point
home = Locationwp().Set(38.315339, -76.548108, 0, id)
to = Locationwp()
Locationwp.id.SetValue(to, int(MAVLink.MAV_CMD.TAKEOFF))
Locationwp.p1.SetValue(to, 15)
Locationwp.alt.SetValue(to, 50)

print ("set wp total")
MAV.setWPTotal(12)
print ("upload to")
MAV.setWP(to,0,MAVLink.MAV_FRAME.GLOBAL_RELATIVE_ALT);

#set waypoints for payload delivery
for i in range (1, len(target_lat)+1):
    wp[i-1] = Locationwp().Set(target_lat[i-1], target_long[i-1], alt, id)

#upload waypoints for payload delivery
for i in range (1, len(target_lat)+1):
    print("upload waypoint ", i, "for payload delivery")
    MAV.setWP(wp[i-1], i, MAVLink.MAV_FRAME.GLOBAL_RELATIVE_ALT);

print("uploaded all waypoints for payload delivery")
MAV.setWPACK();