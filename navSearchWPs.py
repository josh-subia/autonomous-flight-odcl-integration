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

trig_dist = float(input("Enter camera trigger distance: "))
#convert to feet from meters
if inMeters == 0:
    for i in range(0, n):
        alt[i] = alt[i] * 0.30483

#print waypoints to the waypoint file
f = open("./test_files/navSearchWPs.waypoints", "w")
f.write("QGC WPL 110\n")
#Write the takeoff command
f.write("0 1 0 16 0 0 0 0 38.315339 -76.548108 0.000000 1\n")
#write navigation waypoints to the waypoint file
f.write(f"1 0 3 22 0.00000000 0.00000000 0.00000000 0.00000000 {lat[0]} {long[1]} {alt[1]} 1\n")
for i in range(1, len(lat)):
    f.write(f"{i+1} 0 3 16 0.00000000 0.00000000 0.00000000 0.00000000 {lat[i]} {long[i]} {alt[i]} 1\n")

#write search area waypoints to the waypoint file
f.write(f"{len(lat)+1} 1	0	16	0	0	0	0	38.3144350	-76.5452350	35.000000	1\n")
f.write(F"{len(lat)+2} 0	3	22	20.00000000	0.00000000	0.00000000	0.00000000	0.00000000	0.00000000	30.000000	1\n")
f.write(F"{len(lat)+3} 0	3	16	0.00000000	0.00000000	0.00000000	0.00000000	38.31442530	-76.54522930	26.000000	1\n")
#DO_SET_CAM_TRIGG_DIST currently set to take a photo every 15 meters
f.write(F"{len(lat)+4} 0	3	206	{trig_dist}	0.00000000	1.00000000	0.00000000	0.00000000	0.00000000	0.000000	1\n")
f.write(F"{len(lat)+5} 0	3	16	0.00000000	0.00000000	0.00000000	0.00000000	38.31422760	-76.54399680	26.000000	1\n")
f.write(F"{len(lat)+6} 0	3	16	0.00000000	0.00000000	0.00000000	0.00000000	38.31425390	-76.54398910	26.000000	1\n")
f.write(F"{len(lat)+7} 0	3	16	0.00000000	0.00000000	0.00000000	0.00000000	38.31445150	-76.54522110	26.000000	1\n")
f.write(F"{len(lat)+8} 0	3	16	0.00000000	0.00000000	0.00000000	0.00000000	38.31447780	-76.54521300	26.000000	1\n")
f.write(F"{len(lat)+9} 0	3	16	0.00000000	0.00000000	0.00000000	0.00000000	38.31428020	-76.54398130	26.000000	1\n")
f.write(F"{len(lat)+10} 0	3	16	0.00000000	0.00000000	0.00000000	0.00000000	38.31430660	-76.54397360	26.000000	1\n")
f.write(F"{len(lat)+11} 0	3	16	0.00000000	0.00000000	0.00000000	0.00000000	38.31450410	-76.54520480	26.000000	1\n")
f.write(F"{len(lat)+12} 0	3	16	0.00000000	0.00000000	0.00000000	0.00000000	38.31453040	-76.54519660	26.000000	1\n")
f.write(F"{len(lat)+13} 0	3	16	0.00000000	0.00000000	0.00000000	0.00000000	38.31433290	-76.54396580	26.000000	1\n")
f.write(F"{len(lat)+14} 0	3	16	0.00000000	0.00000000	0.00000000	0.00000000	38.31435930	-76.54395810	26.000000	1\n")
f.write(F"{len(lat)+15} 0	3	16	0.00000000	0.00000000	0.00000000	0.00000000	38.31455660	-76.54518850	26.000000	1\n")
f.write(F"{len(lat)+16} 0	3	16	0.00000000	0.00000000	0.00000000	0.00000000	38.31458290	-76.54518030	26.000000	1\n")
f.write(F"{len(lat)+17} 0	3	16	0.00000000	0.00000000	0.00000000	0.00000000	38.31438560	-76.54395030	26.000000	1\n")
f.write(F"{len(lat)+18} 0	3	16	0.00000000	0.00000000	0.00000000	0.00000000	38.31449480	-76.54445930	26.000000	1\n")
f.write(F"{len(lat)+19} 0	3	16	0.00000000	0.00000000	0.00000000	0.00000000	38.31460920	-76.54517210	26.000000	1\n")
#DO_SET_CAM_TRIGG_DIST set to 0
f.write(F"{len(lat)+21} 0	3	206	0	0.00000000	1.00000000	0.00000000	0.00000000	0.00000000	0.000000	1\n")
#Loiter unlimited
f.write(F"{len(lat)+22} 0	3	17  0.00000000	0.00000000	0.00000000	0.00000000	0.00000000	0.00000000	0.000000	1")
f.close()