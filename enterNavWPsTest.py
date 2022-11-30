#This file is able to get waypoint data through user input and saves it in a navWPs.waypoints file
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
        alt[i] = alt[i] * 0.30483

#print waypoints to the waypoint file
f = open("navWPs.waypoints", "w")
f.write("QGC WPL 110\n")
#Write the takeoff command
f.write("0 1 0 16 0 0 0 0 38.315339 -76.548108 0.000000 1\n")
#write waypoints to the waypoint file
f.write(f"1 0 3 22 0.00000000 0.00000000 0.00000000 0.00000000 {lat[0]} {long[1]} {alt[1]} 1\n")
for i in range(1, len(lat)):
    f.write(f"{i+1} 0 3 16 0.00000000 0.00000000 0.00000000 0.00000000 {lat[i]} {long[i]} {alt[i]} 1\n")

f.close()