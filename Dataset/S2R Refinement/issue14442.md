**Environment where the bug occurred:**

- **Hardware environment:** MindPX FCU or any other FCUs with onboard mpu6500 sensor not being the last driver launched
- **Software environment:** PX4 Autopilot version > v1.10.0
- **Report Time:** Mar 20, 2020
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**341dd6b

**Steps for bug reproduction:**

- **Step 1:** Use a MindPX FCU, or any other FCUs that use a 6500 sensor, ensuring the 6500 driver is not the last one launched.
- **Step 2:** Connect to QGroundControl (QGC) and start a magnetometer (mag) calibration.
- **Step 3:** Observe that the calibration fails.

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** N/A
- **Behavior after step 3:** The mag calibration fails, as indicated by warning messages.

**Expected behavior:**

- **Expected behavior 1:** The mag calibration should complete without issue.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Not explicitly mentioned, but it is implied the user identified and described the bug in detail.
- **URL of the flight log provided by the user:** Not provided.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Pull request #14441 was made to fix the issue.
- **Result of the operation after the user adopted suggestion 1:** N/A (the suggestion was for further review and merging, not directly actionable by the user).
- **Suggestion 2 provided by developers or other personnel:** Developer `dagar` commented that the issue has been resolved with the new Invensense drivers.
- **Result of the operation after the user adopted suggestion 2:** Presumably, the issue was resolved after updating to the latest drivers, but this is not explicitly confirmed in the comments.
