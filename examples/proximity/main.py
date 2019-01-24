###############################################
#   This is an example for the SL06 ambient
#   light, colour, gesture and proximity
#   sensor.
#
#   SL06 is enabled as a proximity sensor.
#
#   Move and object to and away from the sensor
#   within a 10cm range. The proximity level
#   between the object and sensor is detected.
###############################################

import streams
from xinabox.sl06 import sl06

streams.serial()

# SL06 instance
SL06 = sl06.SL06(I2C0)  

# configure SL06
SL06.init()

# enable SL06 for proximity sensing
SL06.enableProximitySensor()

while True:
    prox = SL06.getProximity()  # read the proximity level
    print(prox)
    
    sleep(2000)
