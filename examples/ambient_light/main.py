###############################################
#   This is an example for the SL06 ambient
#   light, colour, gesture and proximity
#   sensor.
#
#   SL06 is enabled as a light sensor.
#
#   The ambient light level is measured and
#   displayed on the serial console.
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
    light = SL06.getAmbientLight()  # read the the ambient light level
    print('Ambient Light Level: ', light)
    
    sleep(2000)
