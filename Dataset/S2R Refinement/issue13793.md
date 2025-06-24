**Environment where the bug occurred:**

- **Hardware environment:** Pixhawk1 or Pixhawk Cube, Flamewheel 450 drone or a custom larger drone
- **Software environment:** PX4 Autopilot v1.8.2, v1.9.2, or v1.10.0
- **Report Time:** Dec 27, 2019
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**e189733

**Steps for bug reproduction:**

- **Step 1:** Use Pixhawk1 or Pixhawk Cube with v1.8.2, v1.9.2, or v1.10 firmware.
- **Step 2:** Upload a mission with constant-altitude waypoints.
- **Step 3:** Take off and start the mission.
- **Step 4:** Observe the drone fluctuate 1-2 meters from the setpoint altitude.

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** N/A
- **Behavior after step 3:** N/A
- **Behavior after step 4:** The drone's altitude fluctuates 1-2 meters from the setpoint.

**Expected behavior:**

- **Expected behavior 1:** The drone's altitude should follow the setpoint altitude in mission mode.
- **Expected behavior 2:** The altitude accuracy should match the precision in position mode.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Tried missions on v1.10.0 and tuned the MPC_Z parameters without improvement.
- **URL of the flight log provided by the user:** [Log File](https://review.px4.io/plot_app?log=624517a3-9159-415c-8974-4fc790206f6f)

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `dagar` suggested tuning the position controller and syncing with current PX4 version (v1.10.0).
- **Result of the operation after the user adopted suggestion 1:** No improvements observed even after upgrading to v1.10.0 and tuning parameters.
- **Suggestion 2 provided by developers or other personnel:** Comment by `bresch` suggested the issue could be due to setup problems affecting velocity or position estimates.
- **Result of the operation after the user adopted suggestion 2:** Not detailed in the comments or report.
