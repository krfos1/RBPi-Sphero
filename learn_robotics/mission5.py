# Mission 5: Add the turns!
import sys, os, time

# Magic lines: don't change these
sys.path.append(os.path.expanduser("~/sphero-sdk-raspberrypi-python"))
from sphero_sdk import SpheroRvrObserver
from keys import get_key

rvr = SpheroRvrObserver()   # make the robot
rvr.wake()                  # wake it up
time.sleep(2)               # wait 2 seconds

speed = 64   # 0 is slow, 255 is FAST
turn_time = 0.5   # seconds to turn
current = (0, 0, 0, 0)   # what the wheels are doing now

print("Press w, s, a, d, x = stop, q = quit")
while True:
    key = get_key()   # check the keyboard
    if key == "w":
        current = (1, speed, 1, speed)   # forward
    elif key == "s":
        current = (2, speed, 2, speed)   # backward
    elif key == "a":
        rvr.raw_motors(2, speed, 1, speed)   # spin left
        time.sleep(turn_time)
    elif key == "d":
        rvr.raw_motors(1, speed, 2, speed)   # spin right
        time.sleep(turn_time)
    elif key == "x":
        current = (0, 0, 0, 0)           # stop
    elif key == "q":
        break
    rvr.raw_motors(*current)   # send the plan to the robot

rvr.raw_motors(0, 0, 0, 0)
rvr.close()
