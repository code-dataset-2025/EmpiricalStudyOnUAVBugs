**Environment where the bug occurred:**

- **Hardware environment:** Multi-copter
- **Software environment:** make px4_sitl gazebo
- **Report Time:** May 17, 2023
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**599a66c

**Steps for bug reproduction:**

- **Step 1:** Make `px4_sitl gazebo`
- **Step 2:** Arm the drone and start takeoff mode
- **Step 3:** When the drone is on the ground, execute the code to send `MAV_CMD_NAV_TAKEOFF` command

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** N/A
- **Behavior after step 3:** The drone shows strange behaviors such as ultra-low flying, rollover, and flying around

**Expected behavior:**

- **Expected behavior 1:** The behavior of takeoff with the `MAV_CMD_NAV_TAKEOFF` command should match the expected takeoff behavior as specified for the takeoff mode
- **Expected behavior 2:** No strange or unexpected behaviors during takeoff

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Tested with different coordinates and observed the effects; mentioned the parameter `COM_DISARM_PRFLT` affecting behavior if the drone stays on the ground too long.
- **URL of the flight log provided by the user:**
  - log 1: [Log 791a9860-1eca-48f2-8a3e-575de70051e9](https://logs.px4.io/plot_app?log=791a9860-1eca-48f2-8a3e-575de70051e9)
  - log 2: [Log e6ed2e26-d240-4b1b-aa6f-6c860ac4fe1f](https://logs.px4.io/plot_app?log=e6ed2e26-d240-4b1b-aa6f-6c860ac4fe1f)
  - log 3: [Log 50e0e9fa-96ba-478b-8524-533b2f22d365](https://logs.px4.io/plot_app?log=50e0e9fa-96ba-478b-8524-533b2f22d365)

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Lqs66 suggested that the drone should rise to the specified height before moving towards the target coordinates to avoid dangerous tilting close to the ground.
- **Result of the operation after the user adopted suggestion 1:** N/A (suggestion was made by the reporter, not a response from developers)
