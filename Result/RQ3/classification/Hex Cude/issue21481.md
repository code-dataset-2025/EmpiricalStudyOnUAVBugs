**Environment where the bug occurred:**

- **Hardware environment:** Hex CubeOrange
- **Software environment:** PX4 Autopilot (last main branch or v1.14.0_beta2 tag firmware)
- **Report Time:** Apr 15, 2023
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**5c1e0dd

**Steps for bug reproduction:**

- **Step 1:** Flash the last main branch firmware.
- **Step 2:** Open QGroundControl (QGC).
- **Step 3:** Open the Actuator tab, set PWM_MAIN1 to MOTOR1, PWM_MAIN2 to MOTOR2, PWM_MAIN3 to MOTOR3, and PWM_MAIN4 to MOTOR4.
- **Step 4:** Switch to Stabilized mode.
- **Step 5:** Arm the vehicle.
- **Step 6:** Push up the throttle.

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** N/A
- **Behavior after step 3:** N/A
- **Behavior after step 4:** N/A
- **Behavior after step 5:** N/A
- **Behavior after step 6:** The motors spin very strangely with noise and jerk, making the quadcopter barely able to fly.

**Expected behavior:**

- **Expected behavior 1:** Motors should spin smoothly without strange noises or jerking.
- **Expected behavior 2:** The quadcopter should be able to fly properly.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Tried using PWM_AUX outputs, which worked fine; confirmed the issue is not hardware-related by testing with v1.13 release version firmware where PWM_MAIN output worked well.
- **URL of the flight log provided by the user:** Not provided.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** User `AlexKlimaj` suggested setting the minimum PWM values higher.
- **Result of the operation after the user adopted suggestion 1:** Not mentioned.
