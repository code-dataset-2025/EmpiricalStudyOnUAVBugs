**Environment where the bug occurred:**

- **Hardware environment:** Pixracer
- **Software environment:** PX4 Autopilot with FW version 1.11.0 80
- **Report Time:** Mar 20, 2020
- **PX4 Autopilot commit version:** 240aad1aef6ba2fe7c536f6577cb59a90a6047bc

**Steps for bug reproduction:**

- **Step 1:** Flash Pixracer.
- **Step 2:** Execute `param reset`.
- **Step 3:** Choose airframe or execute `param set SYS_AUTOSTART 4001`.
- **Step 4:** Reboot and try to connect.

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** N/A
- **Behavior after step 3:** N/A
- **Behavior after step 4:** MAVLink over USB does not seem to be working anymore.

**Expected behavior:**

- **Expected behavior 1:** MAVLink should operate over USB without issues after reboot.
- **Expected behavior 2:** Successful connection should be established enabling communication with the drone.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** User checked USB connection issues and noticed erratic behavior potentially linked to a faulty USB port.
- **URL of the flight log provided by the user:** Not provided.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `LorenzMeier` suggested to run `mavlink boot_complete` to determine if the boot process was interrupted.
- **Result of the operation after the user adopted suggestion 1:** Did not fix the issue; noted erratic behavior on Pixhawk 4 as well.
- **Suggestion 2 provided by developers or other personnel:** Indirect suggestion by `julianoes` recognizing the issue could be a USB hub or cable related problem.
- **Result of the operation after the user adopted suggestion 2:** Identified as a faulty port on the D-Link USB hub.
