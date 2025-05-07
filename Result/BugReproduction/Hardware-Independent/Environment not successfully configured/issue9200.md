**Environment where the bug occurred:**

- **Hardware environment:** IRIS+ (simulation)
- **Software environment:** PX4 Autopilot versions 1.6.5 and 1.7.3
- **Report Time:** Mar 30, 2018
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**1ee08da

**Steps for bug reproduction:**

- **Step 1:** Start Mavros over UDP link.
- **Step 2:** Execute `roslaunch mavros px4.launch fcu_url:="udp://:14540@127.0.0.1:14557"`.
- **Step 3:** Prepare the OFFBOARD control method.
- **Step 4:** Start the simulation with `make -j8 posix_sitl_default gazebo`.
- **Step 5:** Run the OFFBOARD control method.

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** N/A
- **Behavior after step 3:** N/A
- **Behavior after step 4:** The copter arms even though no GPS or PX4Flow fix is available.
- **Behavior after step 5:** 
  - The copter drifts during takeoff.
  - The copter rotates from East to North before stabilization.
  - Console output confirms GPS checks pass and EKF begins GPS fusion after drift and rotation.

**Expected behavior:**

- **Expected behavior 1:** The copter should not arm until GPS fix or PX4Flow fix is available.
- **Expected behavior 2:** If armed without position data, the copter should only drift but not rotate.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** 
  - Subscribed to `~setpoint_raw/local` topic and proposed verifying setpoints before allowing takeoff.
  - Proposed additional safety checks to prevent arming until valid position data is available.
  - Identified that `setpoint_raw/target_local` is published only when position control module is ready.
  - Discovered the default yaw setpoint is 0 unless explicitly initialized.
- **URL of the flight log provided by the user:** [Flight log link](https://logs.px4.io/plot_app?log=5477f120-408d-4ce5-82e1-3b3d695a3a03)

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `dagar` acknowledged the report and referenced an initial PR for improving system checks (#9193).
- **Result of the operation after the user adopted suggestion 1:** N/A (no specific outcome recorded for this suggestion).

- **Suggestion 2 provided by developers or other personnel:** `dagar` requested details on when control requirements (e.g., arming and state transitions) should be enforced and discussed incorporating these checks into PX4.
- **Result of the operation after the user adopted suggestion 2:** The user provided detailed observations about the publishing mechanism of `setpoint_raw/target_local` and proposed adding new offboard modes to handle different control scenarios.

- **Suggestion 3 provided by developers or other personnel:** `dagar` and user `AlexisTM` discussed a fix that would reinitialize attitude and position setpoints during arming.
- **Result of the operation after the user adopted suggestion 3:** The user implemented application-level safety checks and confirmed they resolved the issue. No further work was reported as needed.

- **Final outcome:** The issue was marked stale and eventually closed after no further activity. The user confirmed their workaround resolved the problem.
