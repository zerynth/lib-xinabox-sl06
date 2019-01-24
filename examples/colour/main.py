###############################################
#   This is an example for the SL06 ambient
#   light, colour, gesture and proximity
#   sensor.
#
#   SL06 is enabled as a light sensor.
#
#   Place an object in front of the sensor
#   to determine how much red, green and blue
#   light it possesses.
###############################################

import streams
from xinabox.sl06 import sl06

streams.serial()

# SL06 instance
SL06 = sl06.SL06(I2C0)

# configure SL06
SL06.init()

# enable SL06 for light sensing
SL06.enableLightSensor()

while True:
    red = SL06.getRedLight()        # read red light level
    green = SL06.getGreenLight()    # read green light level
    blue = SL06.getBlueLight()      # read blue light level
    
    print('RED   :', red)
    print('GREEN :', green)
    print('BLUE  :', blue)
    
    sleep(2000)