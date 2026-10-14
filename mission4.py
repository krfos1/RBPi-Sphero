# Mission 4: Remote control
import sys, os, time

# Magic lines: don't change these
sys.path.append(os.path.expanduser("~/sphero-sdk-raspberrypi-python"))
from sphero_sdk import SpheroRvrObserver
from keys import get_key

rvr = SpheroRvrObserver()   # make the robot
rvr.wake()                  # wake it up
time.sleep(2)               # wait 2 seconds

# ---- Mission 4: Remote control ----
# Type your code below this line (copy it from the slides)



# ---- end of your code ----
rvr.raw_motors(0, 0, 0, 0)   # stop
rvr.close()                 # say goodbye
