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

    rvr.drive_control.turn_right_degrees(
        heading=0,
        amount=90
    )
    time.sleep(2)

    rvr.drive_control.turn_right_degrees(
        heading=90,
        amount=90
    )
    time.sleep(2)

    rvr.drive_control.turn_right_degrees(
        heading=180,
        amount=90
    )
    time.sleep(2)

    rvr.drive_control.turn_right_degrees(
        heading=270,
        amount=90
    )
    time.sleep(2)

if __name__ == '__main__':
    try:
        main()

    except KeyboardInterrupt:
        print('\nProgram terminated with keyboard interrupt.')

    finally:
        rvr.close()