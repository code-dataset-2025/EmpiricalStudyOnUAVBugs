**Environment where the bug occurred:**

- **Hardware environment:** Octocopter, Pixhawk Cube, Here+ GPS
- **Software environment:** PX4 Autopilot v1.10.1
- **Report Time:** Apr 2, 2020
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**dfb5b5d

**Steps for bug reproduction:**

- **Step 1:** Upload the latest stable PX4 firmware (v1.10.1)
- **Step 2:** Boot UAV and start logging via shell command "logger on"
- **Step 3:** Stop logging after a short time with "logger stop"
- **Step 4:** Open ULog to see messages

**Observed behavior by the user:**

- **Behavior after step 1:** System initializes with uploaded firmware
- **Behavior after step 2:** Logging starts successfully
- **Behavior after step 3:** Logging stops successfully
- **Behavior after step 4:** Error message "[uorb] sensor_mag advertise failed (5)" appears in ULog file

**Expected behavior:**

- **Expected behavior 1:** The sensor_mag message should be successfully advertised without errors
- **Expected behavior 2:** Logging should not reflect any failures regarding sensor_mag advertisement

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Identified multiple magnetometers detected by the system, attempted to distinguish and manage them
- **URL of the flight log provided by the user:** Flight logs referenced with PX4 Flight Review, but no specific URL provided

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `dagar` explained the system currently supports only 4 magnetometers, and suggested potentially disabling the mpu9250 mags.
- **Result of the operation after the user adopted suggestion 1:** User acknowledged the suggestion, verified hardware components contributing to the issue, and planned to disable the mpu9250 mags.

- **Suggestion 2 provided by developers or other personnel:** User `Thijs----` asked for further guidance from `dagar` on how to disable internal mpu9250 and use other mags.
- **Result of the operation after the user adopted suggestion 2:** Planned to implement disabling the mpu9250 through modifications to `rc.board_sensors` configuration as suggested by `dagar`.
