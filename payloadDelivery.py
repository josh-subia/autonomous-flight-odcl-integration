##This file is able to get target data from the ODCL script and deliver payloads

#Currently these are example target locations
#create empty latitude list
lat = [38.31443310, 38.31450780, 38.31432050, 38.31439840, 38.31428160]
#create empty longitude list
long = [-76.54509950, -76.54509950, -76.54461530, -76.54437120, -76.54401320, -76.54405740]
#create altitude set to 26 meters to deliver payloads
alt = 26

#servo variables
servo_port1 = 3
servo_port2 = 4
servo_port3 = 5
servo_port4 = 6
servo_port5 = 7
servo_PWM = 1500

#write waypoints and do_set_servo commands to waypoint file
f = open("payloadDelivery.waypoints", "w")
f.write(F"1 0	3	16	0.00000000	0.00000000	0.00000000	0.00000000	{lat[0]}	{long[0]}	[{alt}]	1\n")
f.write(F"2 0   3   183 {servo_port1}     {servo_PWM}  0.00000000  0.00000000  0.00000  0.00000 0.000000 1")
f.write(F"3 0	3	16	0.00000000	0.00000000	0.00000000	0.00000000	{lat[1]}	{long[1]}	[{alt}]	1\n")
f.write(F"4 0   3   183 {servo_port2}     {servo_PWM}  0.00000000  0.00000000  0.00000  0.00000 0.000000 1")
f.write(F"5 0	3	16	0.00000000	0.00000000	0.00000000	0.00000000	{lat[2]}	{long[2]}	[{alt}]	1\n")
f.write(F"6 0   3   183 {servo_port3}     {servo_PWM}  0.00000000  0.00000000  0.00000  0.00000 0.000000 1")
f.write(F"7 0	3	16	0.00000000	0.00000000	0.00000000	0.00000000	{lat[3]}	{long[3]}	[{alt}]	1\n")
f.write(F"8 0   3   183 {servo_port4}     {servo_PWM}  0.00000000  0.00000000  0.00000  0.00000 0.000000 1")
f.write(F"9 0	3	16	0.00000000	0.00000000	0.00000000	0.00000000	{lat[4]}	{long[4]}	[{alt}]	1\n")
f.write(F"10 0  3   183 {servo_port5}     {servo_PWM}  0.00000000  0.00000000  0.00000  0.00000 0.000000 1")
f.write("11  0	3	20	0.00000000	0.00000000	0.00000000	0.00000000	0.00000000	0.00000000	0.000000 1")
f.close()