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
#from getNavWPs import *
#from getNavWPs import getNavWPs

#Undecided if to be implemented yet: 
# Get waypoint navigation waypoints through user input and navigate them


# Takeoff Manual/Autonomous


##Conduct waypoint navigation portion of mission demonstration
#create empty latitude list
lat = []
#create empty longitude list
long = []
#create empty altitude list
alt = []
#create empty rows list
rows = []

#store data in a 2d array called rows
with open('navWPs.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        rows.append(row)

idmavcmd = MAVLink.MAV_CMD.WAYPOINT
id = int(idmavcmd)
#set RTH/RTL and flight termination point
home = Locationwp().Set(38.315339, -76.548108, 0, id)
to = Locationwp()
Locationwp.id.SetValue(to, int(MAVLink.MAV_CMD.TAKEOFF))
Locationwp.p1.SetValue(to, 15)
Locationwp.alt.SetValue(to, 50)

#number of waypoints
wp = [0] * len(rows[0])
#print("Length of wp[] ", len(wp))

#store latitude, longitude, and altitude in an array
for i in range(0, len(rows[0])):
    lat.append(float(rows[0][i]))
    long.append(float(rows[1][i]))
    alt.append(float(rows[2][i]))
    #print("Latitude ", i, ":", lat[i])
    #print("Longitude ", i, ":", long[i])
    #print("Altitude ", i, "(in meters):", alt[i])
    wp[i] = Locationwp().Set(lat[i], long[i], alt[i], id)
    

#print ("set wp total")
#Total WP is len(rows[0]) + 1 to account for Home
#print("WPTotal ", len(rows[0])+1)
#MAV.setWPTotal(len(rows[0]) + 1)
print ("upload to")
MAV.setWP(to,0,MAVLink.MAV_FRAME.GLOBAL_RELATIVE_ALT);

#for loop to upload waypoints
for i in range (1, len(rows[0]) + 1):
    print ("upload wp", i)
    MAV.setWP(wp[i-1], i, MAVLink.MAV_FRAME.GLOBAL_RELATIVE_ALT);

print ("final ack")
MAV.setWPACK();

##Navigate the search area
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
#Upload search area waypoints
print ("upload search area wp1")
MAV.setWP(wp1, len(rows[0])+1,MAVLink.MAV_FRAME.GLOBAL_RELATIVE_ALT);
print ("upload search area wp2")
MAV.setWP(wp2, len(rows[0])+2,MAVLink.MAV_FRAME.GLOBAL_RELATIVE_ALT);
print ("upload search area wp3")
MAV.setWP(wp3, len(rows[0])+3,MAVLink.MAV_FRAME.GLOBAL_RELATIVE_ALT);
print ("upload search area wp4")
MAV.setWP(wp4, len(rows[0])+4,MAVLink.MAV_FRAME.GLOBAL_RELATIVE_ALT);
print ("upload search area wp5")
MAV.setWP(wp5, len(rows[0])+5,MAVLink.MAV_FRAME.GLOBAL_RELATIVE_ALT);
print ("upload search area wp6")
MAV.setWP(wp6, len(rows[0])+6,MAVLink.MAV_FRAME.GLOBAL_RELATIVE_ALT);
print ("upload search area wp7")
MAV.setWP(wp7, len(rows[0])+7,MAVLink.MAV_FRAME.GLOBAL_RELATIVE_ALT);
print ("upload search area wp8")
MAV.setWP(wp8, len(rows[0])+8,MAVLink.MAV_FRAME.GLOBAL_RELATIVE_ALT);
print ("upload search area wp9")
MAV.setWP(wp9, len(rows[0])+9,MAVLink.MAV_FRAME.GLOBAL_RELATIVE_ALT);
print ("upload search area wp10")
MAV.setWP(wp10, len(rows[0])+10,MAVLink.MAV_FRAME.GLOBAL_RELATIVE_ALT);

#Get target locations from ODCL script
target_lat = []
target_long = []
target_id = []

#If less than 5 identified targets, navigate the search area again
#if(len(target_lat) < 5):
    #navigate the search area again
    

#Payload delivery


#Landing Manual/Autnomous
