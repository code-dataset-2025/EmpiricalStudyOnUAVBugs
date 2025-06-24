**Environment where the bug occurred:**

- **Hardware environment:** Beaglebone Blue (kernel v4.19.94-ti-r73)
- **Software environment:** PX4 Autopilot release/1.13
- **Report Time:** Jun 3, 2023
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**2f448e9

**Steps for bug reproduction:**

- **Step 1:** Run mavlink telemetry over the SoftApp (access point) 2.4ghz wifi and ping the beaglebone from the ground station.
- **Step 2:** Connect a PS4 dualshock 4 controller to the ground station via Bluetooth and enable settings for spring-loaded throttle in QGC.
- **Step 3:** Test throttle in altitude/position modes and observe actuator output when moving the thumbstick from down to midpoint.
- **Step 4:** Raise throttle in altitude/position modes using both joystick and RC.

**Observed behavior by the user:**

- **Behavior after step 1:** High latency (100+ms end to end) noticed, not directly causing the root issue but possibly contributing.
- **Behavior after step 2:** Able to throttle up and test controls in manual mode; functionality is consistent with both joystick and sbus receiver.
- **Behavior after step 3:** Actuator output does not increase when thumbstick is raised to midpoint in position or altitude mode, unlike in manual/stabilized mode.
- **Behavior after step 4:** Throttle increases until reaching MPC_THR_MIN, then fluctuates and spikes, eventually resulting in loss of motor control.

**Expected behavior:**

- **Expected behavior 1:** Joystick or transmitter should properly throttle up in alt/position mode when thumbstick is moved.
- **Expected behavior 2:** No latency issues over 2.4GHz WiFi telemetry that affects control input.
  

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Troubleshooting included testing both joystick and RC, and referring to discussions on the PX4 forum.
- **URL of the flight log provided by the user:** Not provided.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** A mention on Discussion Forum linking to similar issues and possibly relevant details.
- **Result of the operation after the user adopted suggestion 1:** Not stated (forum link provided for user reference).
