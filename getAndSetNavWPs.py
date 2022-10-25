#This file is able to get waypoint data through user input and store it in an array
#Work that still has to be done is to officially upload these waypoint data to Mission Planner
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

#create empty latitude list
lat = [];
#create empty longitude list
long = [];
#create empty altitude list
alt = [];

#get number of waypoints
n = int(input("Enter number of waypoints: "))
#create empty list of n waypoints
wp = [] * n;

#iterate till all latitudes, longitudes, and altitudes are in their respective arrays
for i in range(0, n):
    #Get latitude,longitude and altitude
    print("Enter waypoint", i, "data")
    latIn = float(input("Enter latitude: "))
    longIn = float(input("Enter longitude: "))
    altIn = float(input("Enter altitude: "))
    #append them to the array
    lat.append(latIn)
    long.append(longIn)
    alt.append(altIn)

for i in range (0, n):
    wp[i] = Locationwp().Set(lat[i], long[i], alt[i], id) 
    print("Latitude", i, ":", lat[i])
    print("Longitude", i, ":", long[i])
    print("Altitude (in meters):", i, ":", alt[i])

idmavcmd = MAVLink.MAV_CMD.WAYPOINT
id = int(idmavcmd)

#set RTH/RTL and flight termination point
home = Locationwp().Set(38.315339, -76.548108, 0, id)
to = Locationwp()
Locationwp.id.SetValue(to, int(MAVLink.MAV_CMD.TAKEOFF))
Locationwp.p1.SetValue(to, 15)
Locationwp.alt.SetValue(to, 50)

print ("set wp total")
#Total WP is n+1 to account for Home
MAV.setWPTotal(n+1)
print ("upload to")
MAV.setWP(to,0,MAVLink.MAV_FRAME.GLOBAL_RELATIVE_ALT);
#for loop to upload waypoints
for i in range (1, n):
    print ("upload wp", i)
    MAV.setWP(wp[i], i, MAVLink.MAV_FRAME.GLOBAL_RELATIVE_ALT);

print ("final ack")
MAV.setWPACK();
