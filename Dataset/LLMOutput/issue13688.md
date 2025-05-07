**Environment where the bug occurred:**

- **Hardware environment:** Cube flight controller
- **Software environment:** PX4 Firmware 1.8.2
- **Report Time:** Dec 6, 2019
- **PX4 Autopilot commit version:** Not explicitly mentioned
- **last commit before the reporting time:**2f63981

**Steps for bug reproduction:**

- **Step 1:** Initialize EKF2 on the ground with vision available. Publish vision pose and orientation to `/mavros/vision_pose/pose_cov`.
- **Step 2:** Move the drone nearby on the ground where vision is not available.
- **Step 3:** Take off in manual mode using RC.
- **Step 4:** Fly to an area where vision is available (1.5-2 meters height).
- **Step 5:** If vision is available, grab position and orientation from `/mavros/local_position/pose` and publish several setpoints to `/mavros/setpoint_position/local`.
- **Step 6:** Switch to OFFBOARD mode.

**Observed behavior by the user:**

- **Behavior after step 6:** The drone suddenly drops 0.5-1 meters but then stabilizes, ascends again, and follows the setpoints as expected.

**Expected behavior:**

- **Expected behavior 1:** The drone should hover at its current position when OFFBOARD mode is enabled.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** None explicitly mentioned concerning further investigation actions.
- **URL of the flight log provided by the user:** Not provided.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `julianoes` asked if the issue persists in newer firmware versions, specifically 1.9.2 or 1.10.
- **Result of the operation after the user adopted suggestion 1:** The user confirmed they were using version 1.8.2 but did not follow up with testing on newer firmware versions.
- **Suggestion 2 provided by developers or other personnel:** `julianoes` suggested that the problem might be fixed in newer releases (1.9 or 1.10) and recommended trying those.
- **Result of the operation after the user adopted suggestion 2:** No follow-up response from the user, leading the developer to close the issue due to inactivity.
