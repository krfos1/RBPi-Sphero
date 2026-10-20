#mission2: Drive Forward
import sys
import time

sys.path.append('/home/pi/sphero-sdk-raspberrypi-python')

from sphero_sdk import SpheroRvrObserver
#Your code here




#bonus: if you can also make it return to its original position, try driving backwards.




if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram terminated with keyboard interrupt.")
    finally:
        rvr.close()
