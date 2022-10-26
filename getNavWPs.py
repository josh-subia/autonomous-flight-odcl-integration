#this file gets waypoint data from the navWaypoints.csv file and uploads it into Mission Planner
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

def getNavWPs():
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
    wp = [] * len(rows[0])

    #store latitude, longitude, and altitude in an array
    for i in range(0, len(rows[0])):
        lat.append(rows[0][i])
        long.append(rows[1][i])
        alt.append(rows[2][i])
        wp[i] = Locationwp().Set(lat[i], long[i], alt[i], id)
        #print("Latitude", i, ":", lat[i])
        #print("Longitude", i, ":", long[i])
        #print("Altitude", i, "(in meters):", alt[i])

    print ("set wp total")
    #Total WP is len(rows[0]) + 1 to account for Home
    MAV.setWPTotal(len(rows[0]) + 1)
    print ("upload to")
    MAV.setWP(to,0,MAVLink.MAV_FRAME.GLOBAL_RELATIVE_ALT);)

    #for loop to upload waypoints
    for i in range (1, len(rows[0]) + 1):
        print ("upload wp", i)
        MAV.setWP(wp[i-1], i, MAVLink.MAV_FRAME.GLOBAL_RELATIVE_ALT);

    print ("final ack")
    MAV.setWPACK();