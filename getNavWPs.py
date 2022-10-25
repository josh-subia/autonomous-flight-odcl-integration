#this file gets waypoint data from the navWaypoints.csv file and uploads it into Mission Planner
import csv
import sys
import math
#import clr
import time
#import System
#from System import Byte

clr.AddReference("MissionPlanner")
#import MissionPlanner
clr.AddReference("MissionPlanner.Utilities") # includes the Utilities class
from MissionPlanner.Utilities import Locationwp
clr.AddReference("MAVLink") # includes the Utilities class
#import MAVLink

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

#store latitude, longitude, and altitude in an array
for i in range(0, len(rows[0])):
    lat.append(rows[0][i])
    long.append(rows[1][i])
    alt.append(rows[2][i])
    #print("Latitude", i, ":", lat[i])
    #print("Longitude", i, ":", long[i])
    #print("Altitude", i, "(in meters):", alt[i])

wp = [] * len(rows[0])
print(len(rows[0]))