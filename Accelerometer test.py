#type: ignore
import adafruit_mpu6050 
import busio
import board
import time

sda_pin=board.GP14
scl_pin=board.GP15
i2c = busio.I2C(scl_pin, sda_pin)
mpu = adafruit_mpu6050.MPU6050(i2c)
print(mpu.acceleration )

while True:
    print (mpu.acceleration)
    if mpu.acceleration[0] > 36:
        print (mpu.acceleration[0])
        time.sleep(1)
    if mpu.acceleration[0] < -36:
        print (mpu.acceleration[0])
        time.sleep(1)
    if mpu.acceleration[1] > 36:
        print (mpu.acceleration[0])
        time.sleep(1)
    if mpu.acceleration[1] < -36:
        print (mpu.acceleration[0])
        time.sleep(1)
