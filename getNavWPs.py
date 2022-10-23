#This file is able to get waypoint data through user input and store it in an array
#Work that still has to be done is to officially upload these waypoint data to Mission Planner
#create empty latitude list
lat = [];
#create empty longitude list
long = [];
#create empty altitude list
alt = [];

#get number of waypoints
n = int(input("Enter number of waypoints: "))

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
    print("Latitude", i, ":", lat[i])
    print("Longitude", i, ":", long[i])
    print("Altitude:", i, ":", alt[i])