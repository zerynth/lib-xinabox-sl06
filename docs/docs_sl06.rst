.. module:: sl06

**************
SL06 Module
**************

This is a module for the `SL06 <https://wiki.xinabox.cc/SL06_-_Gesture/>`_ Digital Proximity, Ambient Light, RGB and Gesture Sensor.
The board is based off the APDS-9960 manufactured by Avago Technologies.
The board uses I2C for communication.

Data Sheets:

- `APDS-9960 <https://docs.broadcom.com/docs/AV02-4191EN>`_

    
    
===============
 SL06 class
===============

.. class:: SL06(drvname, addr=0x39, clk=100000)

    Creates an intance of the SL06 class.

    :param drvname: I2C Bus used '( I2C0, ... )'
    :param addr: Slave address, default 0x39
    :param clk: Clock speed, default 100kHz
    
.. method:: init()

        Configures APDS-9960 by initializing registers to its default values.
        Call immediately after instantiating the SL06 class.
        Raises an exeption if any error occurs during initialization.

        Returns True if initialization is successful.

        
.. method:: getMode()
        
        Returns the mode of the sensor
        
.. method:: setMode(mode, enable)

        Sets the desired mode on APDS9960.
        Exception raised if unsuccessful.

        :param mode: desired mode. AMBIENT_LIGHT, PROXIMITY, GESTURE.
        :param enable: accepts 1 or 0

        Returns True if successful
        
.. method:: enableLightSensor(interrupts)
        
        Begins the light sensor.
        Exception raised if unsuccessful.

        :param interrupts: Input True to enable hardware interrupt on light level. Defaults to False

        
.. method:: disableLightSensor()
        
        Disables the light sensor.
        
        
.. method:: enableProximitySensor(interrupts)
        
        Begins the proximity sensor.
        Exception raised if unsuccessful.

        :param interrupts: Input True to enable hardware interrupt on proximity detection. Defaults to False

        
.. method:: disableProximitySensor()
        
        Disables the proximity sensor.
        
        
.. method:: enableGestureSensor(interrupts)
        
        Begins the gesture sensor.
        Exception raised if unsuccessful.

        :param interrupts: Input True to enable hardware interrupt on gesture detection. Defaults to False

        
.. method:: disableGestureSensor()
        
        Disables the gesture sensor.
        Exception raised if unsuccessful
        
        
.. method:: isGestureAvailable()
        
        Checks whether a gesture was detected.

        
.. method:: getGesture()
            
        Processes a gesture event and returns best guessed gesture.
        
        Returns the gesture direction as a string literal.

        
.. method:: enablePower()
        
        Turns APDS9960 on

        
.. method:: disablePower()
        
        Turns APDS9960 off

        
.. method:: getAmbientLight()
        
        Reads the ambient light measurement.
        Exception raised if unsuccessful

        Returns the ambient light measurement.

        
.. method:: getRedLight()
        
        Reads the red light level.
        Exception raised if unsuccessful.

        Returns the red light level.

        
.. method:: getBlueLight()
        
        Reads the blue light level.
        Exception raised if unsuccessful.

        Returns the blue light level.

        
.. method:: getGreenLight()
        
        Reads the green light level.
        Exception raised if unsuccessful.

        Returns the green light level.

        
.. method:: getProximity()
        
        Reads the proximity level.
        Exception raised if unsuccessful.

        Returns the proximity level.

        
