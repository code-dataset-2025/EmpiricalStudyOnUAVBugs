**Environment where the bug occurred:**

- **Hardware environment:** Pixhawk 6X FC
- **Software environment:** PX4 Autopilot with `release/1.13` branch
- **Report Time:** Aug 22, 2022
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**cfc5795

**Steps for bug reproduction:**

- **Step 1:** Build with `release/1.13` branch.
- **Step 2:** Calibration Accelerometer on a Pixhawk 6X.

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** Unable to calibrate the Pixhawk 6X accelerometer successfully, leading to a calibration error.<font color='red'>六个方向均校准成功</font>

**Expected behavior:**

- **Expected behavior 1:** Accelerometer calibration should complete successfully without errors.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Provided log files and videos to demonstrate the bug: `1.13.1 listener sensor_accel.txt`, `1.13.1 Test Cal Error.txt`, `1.13.1 Test Dmesg.txt`, `Pixhawk.6X.Calc.Issue.1.13.1.mp4`.
- **URL of the flight log provided by the user:** Not provided.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `julianoes` mentioned that while not always able to reproduce the accel problem, the gyro calibration issues were noted. Fixes by `@dagar` in #19660 seemed to improve the situation.
- **Result of the operation after the user adopted suggestion 1:** Calibration for gyro and accel looked much better once the suggested commits were cherry-picked onto the release/1.13 branch.
- **Suggestion 2 provided by developers or other personnel:** Backport performed in #20165.
- **Result of the operation after the user adopted suggestion 2:** N/A – no specific result mentioned associated with this backport in the provided information.
