# Raspberry Pi Robotics Workshop

Starter files and setup instructions for the **Raspberry Pi + Sphero RVR+** robotics workshop.

## Raspberry Pi Setup (Once per Pi)

### Step 1: Connect and turn on the Raspberry Pi

Gather the following:

- Raspberry Pi (these display instructions assume a Raspberry Pi 4)
- Monitor and micro-HDMI-to-HDMI cable
- USB keyboard and mouse
- Compatible Raspberry Pi power supply
- microSD card with Raspberry Pi OS installed

1. With the Raspberry Pi unplugged, insert the microSD card.
2. Connect the micro-HDMI end of the display cable to the Raspberry Pi and the HDMI end to the monitor. On a Raspberry Pi 4, use the micro-HDMI port nearest the USB-C power port for the primary display.
3. Plug the keyboard and mouse into USB ports on the Raspberry Pi.
4. Turn on the monitor and select the correct HDMI input.
5. Connect the Raspberry Pi power supply. The Raspberry Pi should start booting.
6. Wait for the Raspberry Pi desktop or initial setup wizard to appear. Follow any on-screen first-time setup prompts.

> **Note:** If the microSD card does not already have Raspberry Pi OS installed, install it using Raspberry Pi Imager on another computer before starting. More instructions on this can be found in the Raspberry Pi documentation. 

### Step 2: Connect to Wi-Fi

1. On the Raspberry Pi desktop, click the network icon in the top-right corner.
2. Select the appropriate Wi-Fi network.
3. Enter the network password if prompted.
4. Confirm that the Raspberry Pi is connected to the internet.

### Step 3: Open the Terminal

Open **Terminal** from the Raspberry Pi desktop or applications menu. Enter the commands below one at a time.

### Step 4: Update the Raspberry Pi

```bash
sudo apt update
sudo apt upgrade -y
```

Wait for both commands to finish.

### Step 5: Install Git and Python

```bash
sudo apt install git python3 python3-pip -y
```

### Step 6: Download the workshop files

```bash
git clone https://github.com/krfos1/RBPi-Sphero.git ~/learn_robotics
```

This creates a folder named **`learn_robotics`** in the Raspberry Pi user's home directory.

> **Note:** The repository name remains `RBPi-Sphero` on GitHub; `learn_robotics` is the local folder name.

### Step 7: Open the workshop folder

```bash
cd ~/learn_robotics
ls
```

You should see workshop files such as `mission1.py` through `mission5.py`, `keys.py`, and `solutions/`.

### Step 8: Prepare the Sphero RVR+

Before running a mission, make sure the Sphero RVR+ is powered on and connected according to the workshop's hardware and SDK instructions. The exact connection method and any additional Python dependencies must be confirmed from the mission code and robot setup.

### Step 9: Run Mission 1

From the `learn_robotics` directory, run:

```bash
python3 mission1.py
```

Follow the mission instructions. If Python reports a missing module or connection error, ask the workshop instructor to confirm the required Sphero SDK installation and hardware connection.

## Workshop Files

- `mission1.py` to `mission4.py`: Starter missions with pre-made headers. Add code below the marker line.
- `mission5.py`: Copy Mission 4 and add turns.
- `keys.py`: Helper that reads one key press without Enter. Do not edit.
- `solutions/`: Finished mission versions and `robot_boss.py` (the pro program).
  # Additional Information
## Reset a Mission File

To discard uncommitted changes to a mission file and restore the repository version:

```bash
cd ~/learn_robotics
git restore mission1.py
```

**Warning:** This removes your unsaved Git changes to that file.

## Update Workshop Files

To get the latest changes from GitHub:

```bash
cd ~/learn_robotics
git pull
```

If `git pull` reports local changes that would be overwritten, save or back up those changes before continuing.

## Shut Down the Raspberry Pi Safely

When finished, use the Raspberry Pi desktop shutdown menu, or run:

```bash
sudo shutdown -h now
```

Wait until the Raspberry Pi has shut down before disconnecting its power supply.
