**Environment where the bug occurred:**

- **Hardware environment:** Pixhawk 4, also tested on Pixhawk 2.1 (Cube)
- **Software environment:** Ubuntu 18.04, HITL with jMAVsim, locally built px4_fmu-v5-multicopter
- **Report Time:** Nov 14, 2019
- **PX4 Autopilot commit version:** v1.10.0-rc
- **last commit before the reporting time:**9364393

**Steps for bug reproduction:**

- **Step 1:** Follow the recipe from the PX4 website.<font color='red'>该网页已不存在</font>
- **Step 2:** Using Manual/Stabilized mode, arm the vehicle and apply throttle.

**Observed behavior by the user:**

- **Behavior after step 1:** HITL setup is configured as per instructions.
- **Behavior after step 2:** The vehicle does not take off. Mavlink shell (listener command) shows actuator_outputs_1 with valid values and actuator_outputs_0 with 0 values.

**Expected behavior:**

- **Expected behavior 1:** SERVO_OUTPUT_RAW or HIL_ACTUATOR_CONTROLS should follow actuator_outputs_1 and the vehicle should take off in simulation.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** User performed additional troubleshooting steps by using MAVLink inspector to validate message generation and suggested a code change as a potential fix.
- **URL of the flight log provided by the user:** Flight Review Link not explicitly mentioned.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `julianoes` acknowledged the detailed report and indicated it was not good.
- **Result of the operation after the user adopted suggestion 1:** The user reported further observations with no direct follow-up on this specific comment.
- **Suggestion 2 provided by developers or other personnel:** N/A
- **Result of the operation after the user adopted suggestion 2:** N/A

Note: The user proposed a code change to resolve the issue and created a new issue or fix with reference #13488.
