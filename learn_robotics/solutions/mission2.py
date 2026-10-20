#mission2: Drive Forward
import sys
import time

sys.path.append('/home/pi/sphero-sdk-raspberrypi-python')

from sphero_sdk import SpheroRvrObserver

rvr = SpheroRvrObserver()

def main():
    rvr.wake()
    time.sleep(2)
    rvr.drive_control.reset_heading()
    #drive forward for 2 seconds
    rvr.drive_control.drive_forward_seconds(
        speed=64, 
        heading=0,
        time_to_drive=2
        )
    #bonus: if you can also make it return to its original position, try driving backwards.
    time.sleep(2)
    rvr.drive_control.drive_backward_seconds(
        speed=64,
        heading=0,
        time_to_drive=2
    )

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram terminated with keyboard interrupt.")
    finally:
        rvr.close()