from adafruit_display_text
import board
import busio
import adafruit_mpu6050

sda_pin=board.GP16
scl_pin=board.GP15
i2c = busio.I2C(scl_pin, sda_pin)

mpu = adafruit_mpu6050.MPU6050(i2c)
print(mpu.acceleration )

while True:
    print ( mpu.acceleration)
    if mpu.acceleration[0] > 9:
        print ( mpu.acceleration[0])
    if mpu.acceleration[0] < -9:
        print ( mpu.acceleration[0])
    if mpu.acceleration[1] > 9:
        print ( mpu.acceleration[0])
    if mpu.acceleration[1] < -9:    
        print ( mpu.acceleration[0])


    else: 
    print("don't give up")
    
    