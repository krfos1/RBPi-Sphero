#mission4- make it spin like a top.
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

    # your code here
    # make sure to give it bit of time to think before each turn.
    # don't forget to adjust the heading after each move.




if __name__ == '__main__':
    try:
        main()

    except KeyboardInterrupt:
        print('\nProgram terminated with keyboard interrupt.')

    finally:
        rvr.close()
