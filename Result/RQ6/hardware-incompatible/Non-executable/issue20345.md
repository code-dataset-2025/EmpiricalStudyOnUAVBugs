**Environment where the bug occurred:**

- **Hardware environment:** Kakute H7 V1.2
- **Software environment:** PX4 Autopilot with commit c9441bb
- **Report Time:** Oct 3, 2022
- **PX4 Autopilot commit version:** commit c9441bb

**Steps for bug reproduction:**

- **Step 1:** Build firmware using the latest master branch.
- **Step 2:** Do a basic setup and test the motors in the Actuators tab.<font color='red'>缺少电机无法观测现象</font>

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** The motors are unable to spin up.

**Expected behavior:**

- **Expected behavior 1:** Setting PWM_MAIN_FUNCx and PWM_MAIN_TIMx correctly allows motors to be spun up.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** The user attempted to revert to a stable release (v1.13.0) where the issue was resolved. They also attempted to follow new setup guidelines but faced several specific issues including identifying & assigning motors and actuator testing sliders not working.
- **URL of the flight log provided by the user:** Not provided.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** User `bkueng` suggested following the setup guide on the PX4 documentation.
- **Result of the operation after the user adopted suggestion 1:** User `j-chen-opteran` encountered further issues despite following the new setup steps.

- **Suggestion 2 provided by developers or other personnel:** User `bkueng` inquired whether a reboot was done and asked for the results of ESCs initialization and the dshot status.
- **Result of the operation after the user adopted suggestion 2:** N/A (no additional information provided).

- **Suggestion 3 provided by developers or other personnel:** User `julianoes` mentioned a related issue where `vehicle_angular_velocity` was not started, suggesting that as a potential cause and provided a link to a relevant fix.
- **Result of the operation after the user adopted suggestion 3:** N/A (no documented result).
