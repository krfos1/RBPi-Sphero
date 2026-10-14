# Mission 1: Wake up and light up!
import sys, os, time

# don't change these
sys.path.append(os.path.expanduser("~/sphero-sdk-raspberrypi-python"))
from sphero_sdk import SpheroRvrObserver

rvr = SpheroRvrObserver()   # make the robot
rvr.wake()                  # wake it up
time.sleep(2)               # wait 2 seconds

red = 255
green = 0
blue = 128
rvr.led_control.set_all_leds_rgb(red=red, green=green, blue=blue)

time.sleep(5)               # enjoy the lights
rvr.close()                 # say goodbye
