#This is the main function that will run the autonomous-flight and odcl iteegrated script

#imports
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

#import python files

idmavcmd = MAVLink.MAV_CMD.WAYPOINT
id = int(idmavcmd)
#set RTH/RTL and flight termination point
home = Locationwp().Set(38.315339, -76.548108, 0, id)
to = Locationwp()
Locationwp.id.SetValue(to, int(MAVLink.MAV_CMD.TAKEOFF))
Locationwp.p1.SetValue(to, 15)
Locationwp.alt.SetValue(to, 50)

#Get target locations from ODCL script
target_lat = []
target_long = []
target_id = []
    

#Payload delivery


#Landing Manual/Autnomous
