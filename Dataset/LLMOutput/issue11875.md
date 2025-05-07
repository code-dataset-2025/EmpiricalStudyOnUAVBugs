**Environment where the bug occurred:**

- **Hardware environment:** Mention of Yuneec H520C with ultrasonic sensors
- **Software environment:** PX4 Autopilot and QGroundControl (QGC)
- **Report Time:** Apr 19, 2019
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**2b68076

**Steps for bug reproduction:**

- **Step 1:** Assume `get_global_position()->alt` returns a negative number, e.g., -11.0.
- **Step 2:** Assume `navigator->get_takeoff_min_alt()` returns 2.5.
- **Step 3:** Calculate `min_abs_altitude` with `-8.5` based on the logic and links provided.
- **Step 4:** Set `abs_altitude` as 3.0 (user-set altitude).
- **Step 5:** Determine if `abs_altitude < min_abs_altitude` is false.
- **Step 6:** Resulting in an altitude setting error, the vehicle flies 11 + 4 = 15 meters instead of the expected 4 meters.

**Observed behavior by the user:**

- **Behavior after step 1:** Global position altitude starts as a negative value.
- **Behavior after step 2:** Minimum takeoff altitude is calculated to be -8.5.
- **Behavior after step 3:** Absolute altitude comparison results in the incorrect flight altitude setting.
- **Behavior after step 4:** The drone flies to 15 meters instead of the intended altitude.
- **Behavior after step 5:** The user notices a discrepancy between expected and actual altitude settings during takeoff.

**Expected behavior:**

- **Expected behavior 1:** The vehicle should correctly calculate and use relative altitude for takeoff, especially in conditions close to sea level.
- **Expected behavior 2:** Consistent takeoff altitude calculation regardless of starting altitude values in the software or QGC.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** The user conducted tests using SITL (Software In The Loop) with different starting altitudes and reported observing the same logic issue in Yuneec's native code.
- **URL of the flight log provided by the user:** Not provided.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Suggest trying tests with debug output and setting simulator altitudes below sea level for further debugging.
- **Result of the operation after the user adopted suggestion 1:** User could reproduce the issue with SITL but did not find the solution.
- **Suggestion 2 provided by developers or other personnel:** Clarification regarding QGC's role in altitude calculations and the MAV_CMD_NAV_TAKEOFF message usage.
- **Result of the operation after the user adopted suggestion 2:** User acknowledged the clarification, deciding to close the issue without further actions.
