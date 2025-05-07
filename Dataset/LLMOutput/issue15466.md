**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned
- **Software environment:** Transitioning from ArduPlane ChibiOS to PX4 on mro_x21-777 board
- **Report Time:** Aug 1, 2020
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**e2a9b68

**Steps for bug reproduction:**

- **Step 1:** Unpack the PX4 Autopilot software.
- **Step 2:** Connect QGroundControl (QGC) to ArduPlane (ChibiOS).
- **Step 3:** Flash mro_x21-777_default.px4 to the board.
- **Step 4:** Observe the connection behavior with QGC via USB.

**Observed behavior by the user:**

- **Behavior after step 3:** Flashing is reported as successful. 
- **Behavior after step 4:** QGC does not recognize the board via USB, and no logs are available.

**Expected behavior:**

- **Expected behavior 1:** QGC should establish a connection with the board after rebooting with PX4 firmware.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** The user flashed back to ChibiOS ArduPlane and noted immediate recognition by QGC. Also mentioned attempts to find a suitable PX4 firmware via QGC and the possibility of working with changed start scripts to identify the issue.
- **URL of the flight log provided by the user:** Not provided.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `dagar` acknowledged the issue and offered to investigate why QGC might not be recognizing the PX4 firmware.
- **Result of the operation after the user adopted suggestion 1:** The user further investigated the boot process and identified issues with LED indicators, suggesting incomplete boot processes.
- **Suggestion 2 provided by developers or other personnel:** Developer `dagar` reported that the issue should be resolved in commit #15521.
- **Result of the operation after the user adopted suggestion 2:** Fix not explicitly mentioned, but the issue was marked as closed.
