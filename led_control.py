from rpi_ws281x import *

class Leds:
    led_count = 12  # Number of LED pixels.
    led_pin = 12  # GPIO pin connected to the pixels (must support PWM!).
    led_freq_hz = 800000  # LED signal frequency in hertz (usually 800khz)
    led_dma = 10  # DMA channel to use for generating signal (try 10)
    # Set to 0 for darkest and led_brightness for brightest
    led_brightness = 255
    # Set to 0 for darkest and led_brightness for brightest
    # True to invert the signal (when using NPN transistor level shift)
    led_invert = False
    led_channel = 0
    led_strip = ws.SK6812_STRIP_RGBW



    def __init__(self):
        self.led_activated = [255, 255, 255]
        self.led_deactivated = [0, 255, 0]
        self.led_steps = 40
        self.led_fade_time = 2
        self.led_step_interval = self.led_fade_time/self.led_steps
        # led_array is the new 'strip'
        self.led_array = Adafruit_NeoPixel(
            self.led_count,
            self.led_pin,
            self.led_freq_hz,
            self.led_dma,
            self.led_invert,
            self.led_brightness,
            self.led_channel,
            self.led_strip,
        )
    
    def light_fade(self, activate = False):
        if activate:
            f = threading.Thread(target=self.fade, args=(led_deactivated[0], led_deactivated[1], led_deactivated[2], led_activated[0], led_activated[1], led_activated[2]))
        else:
            f = threading.Thread(target=self.fade, args=(led_activated[0], led_activated[1], led_activated[2], led_deactivated[0], led_deactivated[1], led_deactivated[2]))
        f.start()
    
    def fade(self, r1, g1, b1, r2, g2, b2):
        strip = self.led_array
        steps = self.led_steps
        interval = self.led_step_interval
        for k in range(1, steps + 1):
            if self.led_pulse_enabled:
                r = round(((r1 * (steps - k)) + (r2 * k)) / steps)
                g = round(((g1 * (steps - k)) + (g2 * k)) / steps)
                b = round(((b1 * (steps - k)) + (b2 * k)) / steps)
                color = rpi_ws281x.Color(r, g, b)
                time.sleep(interval)
                for j in range(strip.numPixels()):
                    strip.setPixelColor(j, color)
                strip.show()