**Environment where the bug occurred:**

- **Hardware environment:** Originally occurred on an S500 with Pixhawk 4
- **Software environment:** SITL with QGC and a joystick setup
- **Report Time:** Nov 20, 2019
- **PX4 Autopilot commit version:** 84fe64b1c20a4ae8067f04b1e21a961263bac4db

**Steps for bug reproduction:**

- **Step 1:** Start SITL, wait for GPS.
- **Step 2:** Switch mode to HOLD, arm, then disarm without taking off.
- **Step 3:** Arm and takeoff in POSCTL.
- **Step 4:** Switch to RTL. This is when the throttle spike to 0 usually happens; it might not be apparent and may only be visible in a log.

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** N/A
- **Behavior after step 3:** N/A
- **Behavior after step 4:** Throttle intermittently went to 0 upon engaging RTL.

**Expected behavior:**

- **Expected behavior 1:** Throttle should not drop to 0 even if navigator takes a while to figure out the next action.
- **Expected behavior 2:** Flight task should perform a failsafe and maintain the current position while the new RTL setpoint is being published.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Identified faulty logic related to the triplet resetting and publishing in the navigator module.
- **URL of the flight log provided by the user:** [Log file link](https://logs.px4.io/plot_app?log=f1b66ae0-3751-481a-89cb-c7b9adc12037)

**Communication between developers or other personnel and the user:**

- No specific communication or suggestions documented in the provided information.
