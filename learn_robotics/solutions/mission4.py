# Mission 4 - Turn Right
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from robot import RVR

rvr = RVR()
rvr.wake()

rvr.drive(heading=90, speed=64)
rvr.sleep(1)

rvr.stop()
rvr.close()
