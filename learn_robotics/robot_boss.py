# Robot Boss: drive the RVR+ with your keyboard!
import sys, os, time

# Magic lines: don't change these
sys.path.append(os.path.expanduser("~/sphero-sdk-raspberrypi-python"))
from sphero_sdk import SpheroRvrObserver
from keys import get_key

# ---- Change me! ----
LED_COLOR = (255, 0, 128)   # (red, green, blue), 0-255
DRIVE_SPEED = 64            # 0 is slow, 255 is FAST
TURN_SPEED = 64
TURN_TIME = 0.5             # seconds each turn lasts
# --------------------

red, green, blue = LED_COLOR
OFF, FWD, REV = 0, 1, 2     # wheel modes
STOP = (OFF, 0, OFF, 0)

# The menu: each key is linked to what the wheels do
COMMANDS = {
    "w": (FWD, DRIVE_SPEED, FWD, DRIVE_SPEED),   # forward
    "s": (REV, DRIVE_SPEED, REV, DRIVE_SPEED),   # backward
}
TURNS = {
    "a": (REV, TURN_SPEED, FWD, TURN_SPEED),     # spin left
    "d": (FWD, TURN_SPEED, REV, TURN_SPEED),     # spin right
}

rvr = SpheroRvrObserver()   # make the robot
rvr.wake()                  # wake it up
time.sleep(2)               # wait 2 seconds
rvr.led_control.set_all_leds_rgb(red=red, green=green, blue=blue)

current = STOP
print("w s = drive, a d = turn, x = stop, q = quit")
try:
    while True:
        key = get_key()                 # check the keyboard
        if key == "q":
            break
        elif key == "x" or key == " ":
            current = STOP
        elif key in COMMANDS:
            current = COMMANDS[key]     # remember the new plan
        elif key in TURNS:
            rvr.raw_motors(*TURNS[key])
            time.sleep(TURN_TIME)       # turn for a moment
        rvr.raw_motors(*current)        # keep doing the plan
finally:
    rvr.raw_motors(*STOP)       # always stop at the end
    rvr.close()
