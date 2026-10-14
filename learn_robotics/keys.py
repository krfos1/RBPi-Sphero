# keys.py: helper that reads ONE key press instantly (no Enter needed).
# User should never edit this file.
import sys, os, time, termios, tty, select

_last_call = 0.0

def get_key(wait=0.1):
    """Return the key pressed (lowercase), or "" if nothing was pressed."""
    global _last_call
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    try:
        tty.setcbreak(fd)
        # If the robot was busy (like turning), forget keys that piled up.
        if time.time() - _last_call > 0.3:
            termios.tcflush(fd, termios.TCIFLUSH)
        key = ""
        if select.select([fd], [], [], wait)[0]:
            key = os.read(fd, 1).decode(errors="ignore").lower()
        return key
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old)
        _last_call = time.time()
