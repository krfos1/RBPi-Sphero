#mission5- change the RVR lights to a color of your choice and then make it drive in a triangle.
import sys
import time

sys.path.append('/home/pi/sphero-sdk-raspberrypi-python')

from sphero_sdk import SpheroRvrObserver
from sphero_sdk import Colors

rvr = SpheroRvrObserver()

def main():
    rvr.wake()
    time.sleep(2)

    rvr.drive_control.reset_heading()
    # change the color first
    
    # try to make it drive in a triangle
    

if __name__ == '__main__':
    try:
        main()

    except KeyboardInterrupt:
        print('\nProgram terminated with keyboard interrupt.')

    finally:
        rvr.close()
