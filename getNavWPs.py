#this file gets waypoint data from the navWaypoints.csv file and uploads it into Mission Planner
import csv

#create empty latitude list
lat = [];
#create empty longitude list
long = [];
#create empty altitude list
alt = [];
#number of waypoints
n = 0;
with open('navWPs.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for col in csv_reader:
        lat.append(col[0])
        long.append(col[1])
        alt.append(col[2])
        n += 1

for i in range(0, n)
    print("Latitude", i, ":", lat[i])
    print("Longitude", i, ":", long[i])
    print("Altitude (in meters):", i, ":", alt[i])