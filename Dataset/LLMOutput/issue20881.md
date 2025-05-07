**Environment where the bug occurred:**

- **Hardware environment:** Holybro Kakute H7 v2
- **Software environment:** Using the pull request from #20545 for KakuteH7 v2 bootloader and autopilot.
- **Report Time:** Jan 7, 2023
- **PX4 Autopilot commit version:** 0c2a6ca782769dbb77f285784358c10d44eae4b8

**Steps for bug reproduction:**

- **Step 1:** Install the Kakute H7 v2 bootloader from the pull request.
- **Step 2:** Flash the Kakute H7 v2 autopilot from the pull request.
- **Step 3:** Connect via QGroundControl (QGC) and try to calibrate or change some parameters.
- **Step 4:** Reboot the board.

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** N/A
- **Behavior after step 3:** N/A
- **Behavior after step 4:** All parameters and calibrations reset to default.

**Expected behavior:**

- **Expected behavior 1:** Parameters and calibrations should be restored to the user-defined values after rebooting.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Checked code and relevant issues like #20025 to ensure correctness, but the issue persisted.
- **URL of the flight log provided by the user:** Not provided.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Reference/closure associated with pull request #20545.
- **Result of the operation after the user adopted suggestion 1:** Issue was closed without additional context on specific actions taken by the user.
