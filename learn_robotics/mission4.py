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




if __name__ == '__main__':
    try:
        main()

    except KeyboardInterrupt:
        print('\nProgram terminated with keyboard interrupt.')

    finally:
        rvr.close()
