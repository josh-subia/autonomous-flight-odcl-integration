#This is the main function that will run the autonomous-flight and odcl iteegrated script

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

#import python files
from getNavWPs import *

#Undecided if to be implemented yet: 
# Get waypoint navigation waypoints through user input and navigate them


# Takeoff Manual/Autonomous


#conduct waypoint navigation portion of mission demonstration
getNavWPs()

#Navigate the search area


#If less than 5 identified targets, navigate the search area again


#Payload delivery


#Landing Manual/Autnomous
