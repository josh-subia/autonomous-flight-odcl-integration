#This file is able to get waypoint data through user input and saves it in a waypoints.csv file
#Work that still has to be done is to officially upload these waypoint data to Mission Planner
import csv
#create empty latitude list
lat = [];
#create empty longitude list
long = [];
#create empty altitude list
alt = [];

#get number of waypoints
n = int(input("Enter number of waypoints: "))
inMeters = int(input("Is altitude in meters or feet(if meters, enter '1', else enter '0')? "))
#iterate till all latitudes, longitudes, and altitudes are in their respective arrays
i = 0
while i < n:
    #Get latitude,longitude and altitude
    print("Enter waypoint", i, "data")
    latIn = float(input("Enter latitude: "))
    longIn = float(input("Enter longitude: "))
    altIn = float(input("Enter altitude: "))
    #append them to the array
    lat.append(latIn)
    long.append(longIn)
    alt.append(altIn)
    i += 1
    if(i == n):
        print("Is this data correct?")
        for i in range(0, n):
            print("Latitude", i, ":", lat[i])
            print("Longitude", i, ":", long[i])
            print("Altitude", i, ":", alt[i])
        correct = int(input("If this data is corrent, enter '1', else enter '0': "))
        #restart the loop if data is incorrect
        if(correct == 0):
            #get # of waypoints again
            n = int(input("Enter number of waypoints: "))
            lat = []
            long = []
            alt = []
            i = 0
        else:
            break

#convert to feet from meters
if inMeters == 0:
    for i in range(0, n):
        alt[i] = alt[i] * 0.3048


with open('navWPs.csv', 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',')
    csv_writer.writerow(lat)
    csv_writer.writerow(long)
    csv_writer.writerow(alt)
