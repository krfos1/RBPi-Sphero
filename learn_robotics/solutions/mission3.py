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

    rvr.drive_control.drive_forward_seconds(
        speed=64, 
        heading=0,
        time_to_drive=2
        )
    
    rvr.drive_control.turn_right_degrees(
        heading=0, 
        amount=90
        )

    rvr.drive_control.drive_forward_seconds(
        speed=64, 
        heading=90,
        time_to_drive=2
        )

    #bonus if you can make it return to its original position.
    rvr.drive_control.drive_backward_seconds(
        speed=64, 
        heading=90,
        time_to_drive=2
    )
    rvr.drive_control.turn_left_degrees(
        heading=90, 
        amount=90
        )
    rvr.drive_control.drive_backward_seconds(
        speed=64, 
        heading=0,
        time_to_drive=2
    )

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\nProgram terminated with keyboard interrupt.')
    finally:
        rvr.close()