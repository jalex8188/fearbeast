from DMXEnttecPro import Controller

#This isn't ready, will work on next
class Lights 
    def __init__(self):
        dmx = Controller('/dev/ttyUSB0')  # Typical of Linux
        dmx.set_channel(1, 255)  # Sets DMX channel 1 to max 255
        dmx.submit()  # Sends the update to the controller