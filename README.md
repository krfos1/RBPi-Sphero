# Robot Boss Workshop

Starter files for a kids robot workshop (Raspberry Pi + Sphero RVR+).

- `mission1.py` to `mission4.py`: pre-made headers. Kids type their code under the marker line.
- `mission5.py`: kids copy their Mission 4 here, then add turns.
- `keys.py`: helper that reads one key press with no Enter. Don't edit.
- `solutions/`: finished versions of every mission plus `robot_boss.py`, the pro program.

## Teacher setup (once per Pi)
    git clone <this repo> ~/robot-boss
    cd ~/robot-boss
    python3 mission1.py

## Reset a file a kid broke
    git checkout mission1.py

## Update after you change the repo
    git pull
