# Mission 2: Make it go!
import sys, os, time

# Magic lines: don't change these
sys.path.append(os.path.expanduser("~/sphero-sdk-raspberrypi-python"))
from sphero_sdk import SpheroRvrObserver

rvr = SpheroRvrObserver()   # make the robot
rvr.wake()                  # wake it up
time.sleep(2)               # wait 2 seconds

speed = 64   # 0 is slow, 255 is FAST

# raw_motors(left mode, left speed, right mode, right speed)
# mode: 1 = forward, 2 = backward, 0 = stop
rvr.raw_motors(1, speed, 1, speed)   # both wheels forward
time.sleep(2)                        # keep going for 2 seconds
rvr.raw_motors(0, 0, 0, 0)           # both wheels stop

rvr.close()                 # say goodbye
