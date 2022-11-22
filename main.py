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
from enterNavWPs import *
from searchAreaWPs import *



#Undecided if to be implemented yet: 
# Get waypoint navigation waypoints through user input and navigate them


# Takeoff Manual/Autonomous


#conduct waypoint navigation portion of mission demonstration
getNavWPs()

#Navigate the search area


#Get target locations from ODCL script
target_lat = []
target_long = []
target_id = []

#If less than 5 identified targets, navigate the search area again
if(len(target_lat) < 5):
    #navigate the search area again
    

#Payload delivery


#Landing Manual/Autnomous
