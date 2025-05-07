**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned
- **Software environment:** PX4 Autopilot (specific commit version not mentioned)
- **Report Time:** May 10, 2023
- **PX4 Autopilot commit version:** not mentioned
- **last commit before the reporting time:**be03b7f

**Steps for bug reproduction:**

- **Step 1:** Setup the RC (remote control) in a way that the throttle is inverted.
- **Step 2:** Calibrate the radio with QGroundControl (QGC).
- **Step 3:** Check the minimal throttle value, for example, in the `uorb` topic `manual_control_setpoint`.
- **Step 4:** Check the value of `RCx_TRIM` for the throttle channel; it will be set to `RCx_MAX`.

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** Calibration completes, but throttle values are incorrectly set from 0 to 1.
- **Behavior after step 3:** Minimal throttle value appears incorrect.
- **Behavior after step 4:** `RCx_TRIM` for throttle channel set to maximum value, causing arming rejection.

**Expected behavior:**

- **Expected behavior 1:** The throttle value should be from -1 to 1.
- **Expected behavior 2:** The vehicle should arm when the throttle is set to a minimum.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Described the calibration steps and checked specific settings and parameters.
- **URL of the flight log provided by the user:** Not provided.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** MaEtUgR suggested looking at pull request #21682 as a potential solution.
- **Result of the operation after the user adopted suggestion 1:** Not explicitly mentioned.
- **Suggestion 2 provided by developers or other personnel:** MaEtUgR mentioned that the solution was merged on the main branch and version 1.14.
- **Result of the operation after the user adopted suggestion 2:** Issue resolved and changes merged.
