#mission1-change the lights on the RVR.
import sys
import time

sys.path.append('/home/pi/sphero-sdk-raspberrypi-python')

from sphero_sdk import SpheroRvrObserver
from sphero_sdk import Colors

rvr = SpheroRvrObserver()

def main():
    rvr.wake()
    time.sleep(2)
    rvr.led_control.set_all_leds_color(color=Colors.red)
    time.sleep(1)
    rvr.led_control.set_all_leds_rgb(red=255, green=0, blue=0)
    #bonus: if you can make the color purple using the set_all_leds_rgb function.
    #rvr.led_control.set_all_leds_rgb(red=128, green=0, blue=128)
    #rvr.led_control.set_all_leds_rgb(red=255, green=0, blue=255)

if __name__ == "__main__":
    try:
        main()

    except KeyboardInterrupt:
        print("\nProgram terminated with keyboard interrupt.")

    finally: 
        rvr.close()