###############################################
#   This is an example for the SL06 ambient
#   light, colour, gesture and proximity
#   sensor.
#
#   SL06 is enabled as a gesture sensor.
#
#   Swipe your hand across the sensor for a
#   reading to be printed on the console.
###############################################

import streams
from xinabox.sl06 import sl06

streams.serial()

# SL06 instance
SL06 = sl06.SL06(I2C0)

# configure SL06
SL06.init()

# enable SL06 for gesture sensing
SL06.enableGestureSensor()

while True:
    if SL06.isGestureAvailable():   # check for gesture
        dir = SL06.getGesture()     # read direction
        print(dir)                  # print direction on console
    
    sleep(100)