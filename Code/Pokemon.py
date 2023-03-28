#type: ignore
import time
import board
import busio
import pulseio

import adafruit_gps #importing things

#sets TX and RX pins. Sets baudrate as well #9600 baudrate = 9600 bit per second 
uart = busio.UART(board.GP4, board.GP5, baudrate=9600, timeout=10) #

gps = adafruit_gps.GPS(uart, debug=False)  
gps.send_command(b"PMTK314,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0") # sends command to GPS to pin location
gps.send_command(b"PMTK220,1000")


last_print = time.monotonic()
#Values=open(f"/data/{int(time.monotonic())}.csv","w")
#Values=open("data.csv","w")
#with open(f"/data/{int(time.monotonic())}.csv", "w") as datalog:

with open("/data.csv", "w") as datalog: #
    
    while True:
        gps.update() #calls GPS
        current = time.monotonic() #gets value of time
        #print(x_acceleration)
        time.sleep(1)
        if not gps.has_fix: # loop if no fix is established 
            # Try again if we don't have a fix yet.
            print("Waiting for fix...")
            continue
        #gps_altitude.append(gps.altitude_m)
        #gps_speed.append(gps.speed_knots)
        if 'altitude_initial' is not None: #is not None = not available/not true 
            altitude_initial = gps.altitude_m # creates a list of altitude data
        if 'time_initial' is not None:
             time_initial = time.monotonic() #creates a list of time data
        if gps.altitude_m is not None: # if not true
            if gps.speed_knots is not None:
                print("speed check successful")
                print("Speed: {} knots".format(gps.speed_knots))
                print("Altitude: {} meters".format(gps.altitude_m))
                #Values.write(f"{gps.altitude_m},{gps.speed_knots}\n") # i changes every single     
                datalog.write(f"{time.monotonic()-time_initial},{gps.speed_knots},{gps.altitude_m-altitude_initial}\n") #gps.altitude_m - altitude_initial``
                print("writing to file")
                datalog.flush()
        #break 
