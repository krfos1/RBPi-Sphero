# Mission 3: Spin like a top!
import sys, os, time

# Magic lines: don't change these
sys.path.append(os.path.expanduser("~/sphero-sdk-raspberrypi-python"))
from sphero_sdk import SpheroRvrObserver

rvr = SpheroRvrObserver()   # make the robot
rvr.wake()                  # wake it up
time.sleep(2)               # wait 2 seconds

speed = 64   # 0 is slow, 255 is FAST

# left wheel backward, right wheel forward: spin LEFT
rvr.raw_motors(2, speed, 1, speed)
time.sleep(0.5)
rvr.raw_motors(0, 0, 0, 0)

# left wheel forward, right wheel backward: spin RIGHT
rvr.raw_motors(1, speed, 2, speed)
time.sleep(0.5)
rvr.raw_motors(0, 0, 0, 0)

rvr.close()                 # say goodbye
