**Environment where the bug occurred:**

- **Hardware environment:** VTOL with Pixhawk 4
- **Software environment:** PX4 Autopilot, almost unchanged 1.9 stable flashed
- **Report time:** Jun 4, 2019
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**574f7e9

**Steps for bug reproduction:**

- **Step 1:** Start simulation with joystick configured.
- **Step 2:** When GPS is locked but in Manual mode from bootup, hold throttle stick high and switch to position mode.<font color='red'>在仿真中停止gps后无法控制</font>
- **Step 3:** Let go of the stick and let it center.
- **Step 4:** Arm the vehicle.

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** N/A
- **Behavior after step 3:** N/A
- **Behavior after step 4:** The vehicle goes up without a smooth takeoff and possibly detects landing even though it should idle.

**Expected behavior:**

- **Expected behavior 1:** The vehicle should take off smoothly.
- **Expected behavior 2:** The vehicle should not detect a landing incorrectly and should idle as expected.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** The user mentioned that commit `1c776f1` fixes this problem for multicopters and did extensive testing on multicopter platforms. However, it seems VTOL works differently and doesn't go through the same code.
- **URL of the flight log provided by the user:** Not provided.

**Communication between developers or other personnel and the user:**

There were no specific suggestions or follow-up communications included in the report content provided.
