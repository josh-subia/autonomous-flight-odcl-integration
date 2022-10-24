#This is a modified version of Mission Planner's "example4 wp.py" python script
#This python script sets waypoints to search the Air Delivery area. 
#It currently does not include commands to trigger a camera
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

#set RTH/RTL and flight termination point
home = Locationwp().Set(38.315339, -76.548108, 0, id)
to = Locationwp()
Locationwp.id.SetValue(to, int(MAVLink.MAV_CMD.TAKEOFF))
Locationwp.p1.SetValue(to, 15)
Locationwp.alt.SetValue(to, 50)
#waypoints to search the air delivery area
wp1 = Locationwp().Set(38.3144603, -76.5452184, 26, id)
wp2 = Locationwp().Set(38.3142627, -76.5439865, 26, id)
wp3 = Locationwp().Set(38.3142188, -76.5439994, 26, id)
wp4 = Locationwp().Set(38.3143323, -76.544707, 26, id)
wp5 = Locationwp().Set(38.3145041, -76.5452048, 26, id)
wp6 = Locationwp().Set(38.3143066, -76.5439736, 26, id)
wp7 = Locationwp().Set(38.3143505, -76.5439606, 26, id)
wp8 = Locationwp().Set(38.3145479, -76.5451912, 26, id)
wp9 = Locationwp().Set(38.3145917, -76.5451776, 26, id)
wp10 = Locationwp().Set(38.3143944, -76.5439477, 26, id)

#waypoint total is 12 because there is the "upload to", 10 search waypoints, and RTL waypoint
print ("set wp total")
MAV.setWPTotal(12)
print ("upload to")
MAV.setWP(to,0,MAVLink.MAV_FRAME.GLOBAL_RELATIVE_ALT);
print ("upload wp1")
MAV.setWP(wp1,1,MAVLink.MAV_FRAME.GLOBAL_RELATIVE_ALT);
print ("upload wp2")
MAV.setWP(wp2,2,MAVLink.MAV_FRAME.GLOBAL_RELATIVE_ALT);
print ("upload wp3")
MAV.setWP(wp3,3,MAVLink.MAV_FRAME.GLOBAL_RELATIVE_ALT);
print ("upload wp4")
MAV.setWP(wp4,4,MAVLink.MAV_FRAME.GLOBAL_RELATIVE_ALT);
print ("upload wp5")
MAV.setWP(wp5,5,MAVLink.MAV_FRAME.GLOBAL_RELATIVE_ALT);
print ("upload wp6")
MAV.setWP(wp6,6,MAVLink.MAV_FRAME.GLOBAL_RELATIVE_ALT);
print ("upload wp7")
MAV.setWP(wp7,7,MAVLink.MAV_FRAME.GLOBAL_RELATIVE_ALT);
print ("upload wp8")
MAV.setWP(wp8,8,MAVLink.MAV_FRAME.GLOBAL_RELATIVE_ALT);
print ("upload wp9")
MAV.setWP(wp9,9,MAVLink.MAV_FRAME.GLOBAL_RELATIVE_ALT);
print ("upload wp10")
MAV.setWP(wp10,10,MAVLink.MAV_FRAME.GLOBAL_RELATIVE_ALT);

#Commented out set WP to home because air delivery still needs to be coded
#print ("upload home - reset on arm")
#MAV.setWP(home,11,MAVLink.MAV_FRAME.GLOBAL_RELATIVE_ALT);
print ("final ack")
MAV.setWPACK();

print ("done")
