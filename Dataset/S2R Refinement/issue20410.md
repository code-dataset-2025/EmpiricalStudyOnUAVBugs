**Environment where the bug occurred:**

- **Hardware environment:** Matek H743-Slim V1.5
- **Software environment:** PX4 Autopilot with firmware version 1.13.1 
- **Report Time:** Oct 14, 2022
- **PX4 Autopilot commit version:** dc7f29e

**Steps for bug reproduction:**

- **Step 1:** Flash Flight Controller (FC) with the bootloader and Firmware.
- **Step 2:** Connect FC to the PC by USB.
- **Step 3:** Execute `roslaunch mavros px4.launch`.

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** ttyACM0 is found by the computer, but no MAVLink messages are received.
- **Behavior after step 3:** MAVLink does not start at ttyACM0, preventing connection with MAVROS.

**Expected behavior:**

- **Expected behavior 1:** Matek H743-Slim should connect with MAVROS over USB.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** The user reported the issue and later noted that connecting with QGroundControl (QGC) first, then closing it allowed connection with MAVROS.
- **User's workaround:** Added "mavlink start -d /dev/ttyACM0" at the end of `rcS` and created `/etc/extras.txt` on the SD card with the same line to fix the issue.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Not explicitly mentioned.
- **Result of the operation after the user adopted suggestion 1:** N/A (the user found a workaround independently by modifying configuration files).
