**Environment where the bug occurred:**

- **Hardware environment:** SITL (Software In The Loop)
- **Software environment:** PX4 Autopilot
- **Report time:** Nov 26, 2020
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**bd09be4

**Steps for bug reproduction:**

- **Step 1:** Start SITL: `HEADLESS=1 make px4_sitl_rtps gazebo_iris_rtps`
- **Step 2:** In the shell, execute `pxh> uorb status`
- **Step 3:** Check for `sensor_combined` topic; many times, it is not found at all.
- **Step 4:** If the `sensor_combined` topic is not being published, set these parameters:
  - `param set EKF2_MULTI_IMU 0`
  - `param set SENS_IMU_MODE 1`

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** N/A
- **Behavior after step 3:** The `sensor_combined` topic is often not found, even when other sensor data appears normal.
- **Behavior after step 4:** The `sensor_combined` topic begins publishing after setting the parameters.

**Expected behavior:**

- **Expected behavior 1:** The `sensor_combined` topic should be consistently published.
- **Expected behavior 2:** The topic should be visible in the output of `uorb status`.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** The user identified and documented specific parameter changes that resolved the issue.
- **URL of the flight log provided by the user:** Not provided.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `dagar` asked what else SITL is doing when `sensor_combined` isn't found and confirmed issues with `listener sensor_combined` and `listener sensor_selection`.
- **Result of the operation after the user adopted suggestion 1:** The user confirmed that the `sensor_combined` and `sensor_selection` topics were never published.
- **Suggestion 2 provided by developers or other personnel:** Developer `dagar` mentioned knowing where to debug the issue.
- **Result of the operation after the user adopted suggestion 2:** The issue was resolved by a fix in commit #16348.
