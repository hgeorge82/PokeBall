#type:ignore
from adafruit_display_shapes.triangle import Triangle
from adafruit_display_shapes.line import Line
from adafruit_display_shapes.circle import Circle
from adafruit_display_text import label
import adafruit_displayio_ssd1306
import time
import board
import busio
import digitalio
import terminalio
import displayio
def area_calc(x1, x2, x3, y1, y2, y3):
    area = abs((1/2) * (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2) ) )

    print(area)
    return area

displayio.release_displays()
sda_pin = board.GP4
scl_pin = board.GP5    
i2c = busio.I2C(scl_pin, sda_pin)
display_bus = displayio.I2CDisplay(i2c, device_address=0x3d, reset=board.GP21)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)




while True:

  print('Enter the first coordinate in format x,y:')
  coordinate1 = input()
  print('Enter the second coordinate in format x,y:')
  coordinate2 = input()
  print('Enter the third coordinate in format x,y:')
  coordinate3 = input()

  splash = displayio.Group()
  hline1 = Line(64,0,64,64, color=0xFFFF00)
  splash.append(hline1)
  hline2 = Line(0,32,128,32, color=0xFFFF00)
  splash.append(hline2)
  display.show(splash)
  try:
    coordinate1 = coordinate1.split(",")
    coordinate2 = coordinate2.split(",")
    coordinate3 = coordinate3.split(",")
    x1 = float(coordinate1[0])
    x2 = float(coordinate2[0])
    x3 = float(coordinate3[0])

    y1 = float(coordinate1[1])
    y2 = float(coordinate2[1])
    y3 = float(coordinate3[1])
    print(y3)

    triangle = Triangle(int(x1) + 64,(int(y1) + 32),(int(x2) + 64),(int(y2) + 32),(int(x3) + 64),(int(y3) + 32), outline=0xFFFF00)
    splash.append(triangle)
    display.show(splash)

    area = area_calc(x1, x2, x3, y1, y2, y3)
    ans = area


    print(f"The area of the triangle with vertices {coordinate1}, {coordinate2}, {coordinate3} is {ans} square kilometers.")


  except:
    print("these points are not a valid triangle.")


  