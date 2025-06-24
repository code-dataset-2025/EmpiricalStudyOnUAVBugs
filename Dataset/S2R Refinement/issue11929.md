**Environment where the bug occurred:**

- **Hardware environment:** Pixhawk 4
- **Software environment:** Not explicitly mentioned
- **Report Time:** Apr 29, 2019
- **PX4 Autopilot commit version:** c50c44c<font color='red'>编译问题，使用之前最近的release替代</font>

**Steps for bug reproduction:**

- **Step 1:** The drone is switched on.
- **Step 2:** Connect with QGroundControl (QGC) via telemetry link or directly via a USB cable.
- **Step 3:** Go to MAVLink console.
- **Step 4:** Run `uorb status`.
- **Step 5:** Observe the connection status.

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** N/A
- **Behavior after step 3:** N/A
- **Behavior after step 4:** See only a couple of topics before the firmware hangs.<font color='red'>这里提到只有几个topics，但实际有22个输出</font>
- **Behavior after step 5:** Link disconnected, and only a reboot helps.

**Expected behavior:**

- **Expected behavior 1:** To see a full list of topics when running `uorb status`.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Described steps to reproduce the bug.
- **URL of the flight log provided by the user:** Not provided.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `julianoes` acknowledged the bug and mentioned being able to reproduce it on a Pixracer.
- **Result of the operation after the user adopted suggestion 1:** N/A (no further action suggested).
- **Suggestion 2 provided by developers or other personnel:** Developer `bkueng` mentioned a fix available in pull request \#11941.
- **Result of the operation after the user adopted suggestion 2:** Not explicitly mentioned, but implies that the issue was resolved with the fix.
