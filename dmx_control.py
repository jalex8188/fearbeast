from DMXEnttecPro import Controller
import json



#This isn't ready, will work on next
class Lights:
    def __init__(self):
        l = open('lighting_changes.json')
        fixtures = json.load(l)
        self.fixtures = fixtures
        
        # dmx = Controller('/dev/ttyUSB0')  # Typical of Linux
        # dmx.set_channel(1, 255)  # Sets DMX channel 1 to max 255
        # dmx.submit()  # Sends the update to the controller
    
    def activate(self):
        fixtures = self.fixtures["fixtures"]
        set_channel = 1
        step = 0
        max_steps = 40
        for f in fixtures:
            light = str(f)
            channels = fixtures[light]
            # print(channels)
            for channel in channels:
                # print(f"channels are:{channel}")
                values = channels[channel]
                distance = abs(values[1] - values[0])
                step_distance = round(distance/40)
                print(f"step distance is {step_distance}")
                
                # print(f"values of channel are {values}")
            #     print(self.fixtures["fixtures"][str(light)])

    def deactivate(self):
        for f in self.fixtures["fixtures"]:
            for light in f:
                pass
                # print(light)