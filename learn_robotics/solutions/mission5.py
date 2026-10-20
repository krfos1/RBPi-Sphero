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

    rvr.led_control.set_all_leds_rgb(red=0, green=255, blue=0)
    
    rvr.drive_control.turn_right_degrees(
        heading=0,
        amount=90
    )
    time.sleep(1)

    rvr.drive_control.drive_forward_seconds(
        speed=64,
        heading=90,
        time_to_drive=2
    )
    time.sleep(1)

    rvr.drive_control.turn_right_degrees(
        heading=90,
        amount=120
    )
    time.sleep(1)

    rvr.drive_control.drive_forward_seconds(
        speed=64,
        heading=210,
        time_to_drive=2
    )
    time.sleep(1)

    rvr.drive_control.turn_right_degrees(
        heading=210,
        amount=120
    )
    time.sleep(1)

    rvr.drive_control.drive_forward_seconds(
        speed=64,
        heading=330,
        time_to_drive=2
    )

    time.sleep(2)

if __name__ == '__main__':
    try:
        main()

    except KeyboardInterrupt:
        print('\nProgram terminated with keyboard interrupt.')

    finally:
        rvr.close()