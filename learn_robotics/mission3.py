#mission3-make the RVR drive forward, turn, drive forward again, and then return to its original position.
import sys
import time

sys.path.append('/home/pi/sphero-sdk-raspberrypi-python')

from sphero_sdk import SpheroRvrObserver
rvr = SpheroRvrObserver()

def main():
    rvr.wake()
    time.sleep(2)

    rvr.reset_yaw()
    time.sleep(2)
    # Your code here



    
    #bonus if you can make it return to its original position.






if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\nProgram terminated with keyboard interrupt.')
    finally:
        rvr.close()
