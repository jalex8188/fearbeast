from DMXEnttecPro import Controller
import json
import time


#This isn't ready, will work on next
class Lights:
    def __init__(self):
        l = open('lighting_changes.json')
        fixtures = json.load(l)
        self.fixtures = fixtures
        
        self.dmx = Controller('/dev/ttyUSB0')  # Typical of Linux
        # dmx.set_channel(1, 255)  # Sets DMX channel 1 to max 255
        # dmx.submit()  # Sends the update to the controller
    
    def activate(self):
        fixtures = self.fixtures["fixtures"]
        set_channel = 1
        step = 1
        max_steps = 40
        for s in range(max_steps):
            for f in fixtures:
                light = str(f)
                channels = fixtures[light]
                # print(channels)
                for channel in channels:
                    set_channel = int(channel)
                    print(f"channels are:{channel}")
                    values = channels[channel]
                    distance = int(abs(values[1] - values[0]))
                    step_distance = int(round(distance/40))
                    set_value = step * step_distance
                    # print(f"step distance is {step_distance}")
                    self.dmx.set_channel(set_channel, step_distance)  # Sets DMX channel 1 to max 255
                
            self.dmx.submit()  # Sends the update to the controller
            time.sleep(1.5/max_steps)
                # step +=1

                # print(f"values of channel are {values}")
            #     print(self.fixtures["fixtures"][str(light)])

    def deactivate(self):
        fixtures = self.fixtures["fixtures"]
        set_channel = 1
        step = 1
        max_steps = 40
        for s in range(max_steps):
            for f in fixtures:
                light = str(f)
                channels = fixtures[light]
                # print(channels)
                for channel in channels:
                    set_channel = int(channel)
                    print(f"channels are:{channel}")
                    values = channels[channel]
                    distance = int(abs(values[1] - values[0]))
                    step_distance = int(round(distance/40))
                    set_value = (max_steps - step) * step_distance
                    # print(f"step distance is {step_distance}")
                    self.dmx.set_channel(set_channel, step_distance)  # Sets DMX channel 1 to max 255
                
            self.dmx.submit()  # Sends the update to the controller
            time.sleep(1.5/max_steps)
                # step +=1

                # print(f"values of channel are {values}")
            #     print(self.fixtures["fixtures"][str(light)])