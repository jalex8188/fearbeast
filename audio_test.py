import pygame
import RPi.GPIO as GPIO
import time

switch = 31

mode = ""

active = False



def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)

    GPIO.input(31)
    pygame.mixer.pre_init(44100, -16, 1, 2048)
    pygame.init()
    pygame.mixer.init()
    childMusic = pygame.mixer.music.load("TheParting.wav")
    beastMusic = pygame.mixer.music.load("SCP-x3x.wav")
    playMusic = pygame.mixer.music.play(fade_ms=2000)
    fadeOut = pygame.mixer.music.fadeOut(2000)


def init():
    beastMusic
    playMusic
    while True:
        if GPIO.input(10) == GPIO.HIGH:
            if not active:
                print("Button was pushed!")
                fadeOut
                childMusic
                playMusic
                active = True
            else:
                pass
        else:
            if active:
                print("Button not pushed")
                fadeOut
                beastMusic
                playMusic
                active = False

setup()
init()
