import time
from sphero_sdk import SpheroRvrObserver, DriveFlagsBitmask


class RVR:
    def __init__(self):
        self.rvr = SpheroRvrObserver()
        self.heading = 0
        self.rvr.wake()
        time.sleep(2)  # give the RVR time to wake up
        self.rvr.reset_yaw()

    def _drive(self, speed, seconds, reverse=False):
        flags = DriveFlagsBitmask.drive_reverse.value if reverse else 0
        self.rvr.drive_with_heading(speed, self.heading, flags)
        time.sleep(seconds)
        self.stop()

    def forward(self, speed=64, seconds=1):
        self._drive(speed, seconds)

    def backward(self, speed=64, seconds=1):
        self._drive(speed, seconds, reverse=True)

    def left(self, degrees=90):
        self.heading = (self.heading - degrees) % 360
        self.rvr.drive_with_heading(0, self.heading, 0)
        time.sleep(1)

    def right(self, degrees=90):
        self.heading = (self.heading + degrees) % 360
        self.rvr.drive_with_heading(0, self.heading, 0)
        time.sleep(1)

    def stop(self):
        self.rvr.drive_with_heading(0, self.heading, 0)

    def set_color(self, red, green, blue):
        self.rvr.led_control.set_all_leds_rgb(red=red, green=green, blue=blue)

    # aliases in case mission1.py uses different names
    drive_forward = forward
    drive_backward = backward
    turn_left = left
    turn_right = right

    def close(self):
        self.stop()
        self.rvr.close()
