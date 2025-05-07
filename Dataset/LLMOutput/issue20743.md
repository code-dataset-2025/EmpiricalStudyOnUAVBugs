**Environment where the bug occurred:**

- **Hardware environment:** MRO H7, Matek H743-slim
- **Software environment:** PX4 Autopilot with Nuttx 10.3
- **Report Time:** Dec 11, 2022
- **PX4 Autopilot commit version:** 2cb4ef0

**Steps for bug reproduction:**

- **Step 1:** Flash main branch on an MRO or Matek flight controller (FC).

**Observed behavior by the user:**

- **Behavior after step 1:** After flashing the main branch, parameters can't be set or configured for the airframe in QGroundControl (QGC) or via terminal. The SD card appears unmounted as evidenced by terminal outputs, and attempts to resolve this by formatting the SD card or resetting parameters do not work. No log files are generated as the SD card cannot be accessed.

**Expected behavior:**

- **Expected behavior 1:** The system should allow setting parameters and configuring the airframe through QGC.
- **Expected behavior 2:** The SD card should be mounted correctly, with parameter files accessible.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Tried formatting the SD card to FAT32, and used `param reset_all` to reset parameters. Checked whether the SD card could be mounted via terminal commands.
- **URL of the flight log provided by the user:** Not provided.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Not explicitly mentioned in the comments.
- **Result of the operation after the user adopted suggestion 1:** Not applicable as no specific suggestions were noted in this document.
- **Suggestion 2 provided by developers or other personnel:** A follow-up comment indicates that the issue was addressed in another commit (#20812).
- **Result of the operation after the user adopted suggestion 2:** User `gorghino` acknowledged that the issue was resolved with the commit #20812.
