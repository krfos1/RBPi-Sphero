#mission1-change the lights on the RVR.
import sys
import time

sys.path.append('/home/pi/sphero-sdk-raspberrypi-python')

from sphero_sdk import SpheroRvrObserver
from sphero_sdk import Colors
#Your code here


if __name__ == "__main__":
    try:
        main()

    except KeyboardInterrupt:
        print("\nProgram terminated with keyboard interrupt.")

    finally: 
        rvr.close()
