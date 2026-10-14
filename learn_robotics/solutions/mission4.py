# Mission 4: Remote control!
import sys, os, time

# don't change these
sys.path.append(os.path.expanduser("~/sphero-sdk-raspberrypi-python"))
from sphero_sdk import SpheroRvrObserver
from keys import get_key

rvr = SpheroRvrObserver()   # make the robot
rvr.wake()                  # wake it up
time.sleep(2)               # wait 2 seconds

speed = 64   # 0 is slow, 255 is FAST
current = (0, 0, 0, 0)   # what the wheels are doing now

print("Press w, s, x = stop, q = quit")
while True:
    key = get_key()   # check the keyboard
    if key == "w":
        current = (1, speed, 1, speed)   # forward
    elif key == "s":
        current = (2, speed, 2, speed)   # backward
    elif key == "x":
        current = (0, 0, 0, 0)           # stop
    elif key == "q":
        break
    rvr.raw_motors(*current)   # send the plan to the robot

rvr.raw_motors(0, 0, 0, 0)
rvr.close()
