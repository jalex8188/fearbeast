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
        set_channels(1, 1, False)
    
    def set_channels(self, max_steps, step, activate)
        fixtures = self.fixtures["fixtures"]
        for f in fixtures:
            light = str(f)
            channels = fixtures[light]
            # print(channels)
            for channel in channels:
                set_channel = int(channel)
                # print(f"channels are:{channel}")
                start_end = channels[channel]
                distance = int(abs(start_end[1] - start_end[0]))
                step_distance = int(round(distance/40))
                if activate:
                    set_value = step * step_distance
                else:
                    set_value = (max_steps - step) * step_distance
                # print(f"step distance is {step_distance}")
                print(f"Set Channel: {set_channel}, Set Value: {set_value}")
                self.dmx.set_channel(set_channel, set_value)  # Sets DMX channel 1 to max 255
        
    def light_fade(self, activate = False)
        step = 1
        max_steps = 40
        for s in range(max_steps):
            set_channels(max_steps, step, activate)
        
                
            step+= 1
            print(f"step is:{step}")
            self.dmx.submit()  # Sends the update to the controller
            time.sleep(1.5/max_steps)

                # print(f"start_end of channel are {start_end}")
            #     print(self.fixtures["fixtures"][str(light)])