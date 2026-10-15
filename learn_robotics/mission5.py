# Mission 5 - Drive in a Square
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from robot import RVR

rvr = RVR()
rvr.wake()

for i in range(4):
    rvr.drive(heading=i * 90, speed=64)   # 0, 90, 180, 270
    rvr.sleep(1)

rvr.stop()
rvr.close()
