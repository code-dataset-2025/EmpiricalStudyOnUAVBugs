**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned<font color='red'>第一句upload可以看出实际需要pixhwak飞控板</font>
- **Software environment:** Not explicitly mentioned
- **Report Time:** Jun 30, 2022
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**f16ea92

**Steps for bug reproduction:**

- **Step 1:** Compile the firmware with `make px4_fmu-v5_rtps upload`.
- **Step 2:** Connect to QGroundControl.
- **Step 3:** In QGroundControl/Analyze Tools, try to start RTPS with `micrortps_client start`.<font color='red'>同issue19917micrortps命令无法找到，因为micrortps已经不在px4中使用</font>
- **Step 4:** Observe that the terminal stops, and when checking the connection in QGroundControl, it seems disconnected.
- **Step 5:** After a few seconds, QGroundControl reconnects, but `micrortps_client` is still not working.

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** N/A
- **Behavior after step 3:** Attempted to start `micrortps_client`, leading to a crash and disconnection.
- **Behavior after step 4:** Terminal stops and connection appears disconnected.
- **Behavior after step 5:** QGroundControl reconnects, but `micrortps_client` continues to malfunction.

**Expected behavior:**

- **Expected behavior 1:** `micrortps_client` should start without causing a crash.
- **Expected behavior 2:** Connection to QGroundControl should remain stable while using `micrortps_client`.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** 
  - Identified `microdds` as the cause of the problem.
  - Removed the `micro_dds` folder in the firmware.
  - Modified `PX4-Autopilot/boards/TARGET/rtps.px4board` to set `CONFIG_MODULES_MICRODDS_CLIENT=n`.

- **URL of the flight log provided by the user:** Not provided.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Inquiry by user `frnyb` on Sep 1, 2022, asking if a pull request has been opened for the fix.
- **Result of the operation after the user adopted suggestion 1:** Not documented, as the communication was a question rather than a suggestion.
