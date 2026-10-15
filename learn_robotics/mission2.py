# Mission 2 - Move Backward
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from robot import RVR

rvr = RVR()
rvr.wake()

rvr.drive(heading=180, speed=64)
rvr.sleep(2)

rvr.stop()
rvr.close()
