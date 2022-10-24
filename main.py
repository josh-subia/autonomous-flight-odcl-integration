#This is the main function that will run the autonomous-flight and odcl iteegrated script

#imports
import sys
import math
#import clr
import time
#import System
#from System import Byte

#Undecided if to be implemented yet: 
# Get waypoint navigation waypoints through user input and navigate them


# Takeoff Manual/Autonomous
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
    #waypoints to search the air delivery area
    wp[i] = Locationwp().Set(lat[i], long[i], alt[i], id) 
    print("Latitude", i, ":", lat[i])
    print("Longitude", i, ":", long[i])
    print("Altitude (in meters):", i, ":", alt[i])

#Navigate the search area


#If less than 5 identified targets, navigate the search area again


#Payload delivery


#Landing Manual/Autnomous