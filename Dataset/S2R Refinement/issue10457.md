**Environment where the bug occurred:**

- **Hardware environment:** Pixracer board
- **Software environment:** PX4 Autopilot v1.8.0
- **Report Time:** September 11, 2018
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**c41d7eb

**Steps for bug reproduction:**

- **Step 1:** Run PX4 v1.8.0 as released with the Pixracer board, px4fmu v4.
- **Step 2:** Try to start motors.
- **Step 3:** Observe the armed and running light (steady red) with PWM signal at idle.

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** The armed and running light comes on (steady red), but the motors do not spin, and the PWM signal remains at idle.

**Expected behavior:**

- **Expected behavior 1:** The motors should spin when the system is armed.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** The user traced the issue to `src/drivers/px4fmu/fmu.cpp` and suggested a workaround involving setting `_safety_off = _safety_btn_off` if `GPIO_BTN_SAFETY` is defined.
- **URL of the flight log provided by the user:** Not provided.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `dagar` inquired about the safety button usage and expressed interest in moving the safety button handling out of `px4fmu`.
- **Result of the operation after the user adopted suggestion 1:** Not explicitly mentioned in the document.
- **Suggestion 2 provided by developers or other personnel:** `lorenzMeier` recommended using a kill switch for the specific use case.
- **Result of the operation after the user adopted suggestion 2:** Not explicitly mentioned in the document.
- **Suggestion 3 provided by developers or other personnel:** `davids5` asked `lericson` to test with #10477.
- **Result of the operation after the user adopted suggestion 3:** `lericson` mentioned in Comment 10 that the issue was fixed at some point, but no specific details were provided about the resolution.
