**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned
- **Software environment:** PX4 Autopilot
- **Report Time:** Apr 5, 2021
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**2a0a747

**Steps for bug reproduction:**

- **Step 1:** Execute `make px4_sitl gazebo_tailsitter`.
- **Step 2:** Upload mission plan attached to the issue in QGroundControl (QGC).
- **Step 3:** Start the mission.

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** N/A
- **Behavior after step 3:** Model oscillates crazily and does not reach waypoints.

**Expected behavior:**

- **Expected behavior 1:** The model should follow the waypoints.
- **Expected behavior 2:** The model should not oscillate and should fly away correctly.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** User identified that git bisect points to PR #17223 as the potential issue.
- **URL of the flight log provided by the user:** Not provided.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `TSC21` pointed out issues with sensor rotation and error messages that might be affecting the SITL setup.
- **Result of the operation after the user adopted suggestion 1:** User `TSC21` discovered the issue was the mavlink-router running in the background causing loopbacks and confirmed it was resolved.
- **Suggestion 2 provided by developers or other personnel:** Developer `Jaeyoung-Lim` suggested running `make clean` to regenerate messages.
- **Result of the operation after the user adopted suggestion 2:** Developer `TSC21` inquired further about which messages needed regeneration, indicating the suggestion wasn't completely followed through in the comments.
- **Suggestion 3 provided by developers or other personnel:** Developer `julianoes` mentioned that the issue fix will be applied in PX4/PX4-SITL_gazebo-classic#735.
- **Result of the operation after the user adopted suggestion 3:** The issue was resolved as reflected in the closure of the bug report.
