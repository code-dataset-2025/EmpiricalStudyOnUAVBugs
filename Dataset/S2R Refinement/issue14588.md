**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned
- **Software environment:** Latest master branch of PX4 Autopilot
- **Report Time:** Apr 3, 2020
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**5f86ea7

**Steps for bug reproduction:**

- **Step 1:** Execute `make px4_sitl gazebo_tailsitter`.
- **Step 2:** Open QGroundControl (QGC) and send a takeoff command.
- **Step 3:** Switch from multicopter (mc) mode to fixed-wing (fw) mode.
- **Step 4:** Wait for a minute.
- **Step 5:** Switch from fixed-wing (fw) mode back to multicopter (mc) mode.
- **Step 6:** Observe the drone’s angle in Gazebo display for instability.

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** N/A
- **Behavior after step 3:** N/A
- **Behavior after step 4:** N/A
- **Behavior after step 5:** N/A
- **Behavior after step 6:** The drone’s angle displayed in Gazebo is unstable when switching from fw to mc.

**Expected behavior:**

- **Expected behavior 1:** Stable back-transmission from fixed-wing mode to multicopter mode.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** User tried different versions, v1.10 worked fine, but encountered the same problem in v1.11.0-BETA1.
- **URL of the flight log provided by the user:** [https://logs.px4.io/plot_app?log=25a0b4df-5602-4274-8d8f-b933c0dff8ac](https://logs.px4.io/plot_app?log=25a0b4df-5602-4274-8d8f-b933c0dff8ac)

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** @sfuhrer queried about whether the issue persists in the gazebo simulation and if the user has attempted a real flight.
- **Result of the operation after the user adopted suggestion 1:** User confirmed conducting a real flight where the system worked well.
- **Suggestion 2 provided by developers or other personnel:** Developer @sfuhrer suggested further investigation might be required due to a jumpy airspeed reading in SITL that might cause issues.
- **Result of the operation after the user adopted suggestion 2:** Not explicitly mentioned. User shared real flight results which were successful.
