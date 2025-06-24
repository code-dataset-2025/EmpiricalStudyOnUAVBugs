**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned
- **Software environment:** PX4 Autopilot used with ROS2/FastRTPS
- **Report Time:** Sep 28, 2021
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**03bd5e0

**Steps for bug reproduction:**

- **Step 1:** Launch simulator and set PX4 to HOLD mode.
- **Step 2:** Send only trajectory_setpoints using offboard at 10hz; nothing happens.
- **Step 3:** Send only trajectory_setpoints using offboard at 100hz and observe HOLD mode is overridden.

**Observed behavior by the user:**

- **Behavior after step 1:** Simulator is running with PX4 in HOLD mode.
- **Behavior after step 2:** No observable actions occur in the simulator.
- **Behavior after step 3:** HOLD mode is overridden by the offboard setpoints.

**Expected behavior:**

- **Expected behavior 1:** The system should distinguish between trajectory_setpoints from offboard and flight_tasks to avoid conflicts.
- **Expected behavior 2:** In offboard mode, flight_tasks should not send trajectory_setpoints to avoid possible conflicts.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** The user, benjinne, worked on multicopter and rover position controller fixes but had questions about multiple updates for trajectory_setpoint_sub.
- **URL of the flight log provided by the user:** Not provided.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `dagar` suggested respecting the nav_state before publishing and recommended publishing offboard setpoints on a different topic.
- **Result of the operation after the user adopted suggestion 1:** The user, benjinne, worked on the suggested fixes but further issues or results were not explicitly discussed.
- **Suggestion 2 provided by developers or other personnel:** None explicitly provided in terms of additional steps needed.
- **Result of the operation after the user adopted suggestion 2:** Not applicable as no additional actions were suggested in subsequent interactions.
