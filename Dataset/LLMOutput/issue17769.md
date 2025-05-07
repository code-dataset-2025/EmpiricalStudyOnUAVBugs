**Environment where the bug occurred:**

- **Hardware environment:** Pixracer, Pixhawk 4
- **Software environment:** PX4 Autopilot (specific commit version not mentioned)
- **Report Time:** Jun 16, 2021
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**a728431

**Steps for bug reproduction:**

- **Step 1:** Connect Pixracer with USB.
- **Step 2:** Hit accel calibration in QGroundControl (QGC).

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** Calibration process starts but gets stuck at the first step. QGC outputs an error indicating calibration failed due to reading sensor.

**Expected behavior:**

- **Expected behavior 1:** The accelerometer should calibrate without issues.
- **Expected behavior 2:** The calibration process should proceed through the steps and complete successfully.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** User attempted to calibrate the accelerometer multiple times; shared shell output logs.
- **URL of the flight log provided by the user:** Provided by `mrpollo`, URL: https://logs.px4.io/plot_app?log=7f5fd267-4b90-453e-9420-90e62a415409

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** `mrpollo` successfully calibrated using QGC Daily and shared the log.
- **Result of the operation after the user adopted suggestion 1:** Not directly reported by the user.
  
- **Suggestion 2 provided by developers or other personnel:** `dagar` mentioned the issue was fixed in \#17776.
- **Result of the operation after the user adopted suggestion 2:** The author, `julianoes`, did not report back, indicating possible resolution, as the issue was closed.

- **New comment by `Aditya-Innovacious` (Jul 16, 2024):** Reported having a similar issue with Pixhawk 6x, asking about changes in \#19357 where fixes were reverted.

