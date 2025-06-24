**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned
- **Software environment:** PX4 Autopilot
- **Report time:** Oct 15, 2018
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**40489af

**Steps for bug reproduction:**

- **Step 1:** Launch PX4 node.
- **Step 2:** Launch Mavros node.
- **Step 3:** Launch Gazebo.
- **Step 4:** Spawn drone model.
- **Step 5:** Try to arm via QGroundControl (QGC).

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** N/A
- **Behavior after step 3:** N/A
- **Behavior after step 4:** N/A
- **Behavior after step 5:** The drone cannot be armed; error messages state "Primary accelerometer not found" and "Arm/Disarm temporarily rejected."

**Expected behavior:**

- **Expected behavior 1:** The drone should arm successfully.
- **Expected behavior 2:** The drone should be operational after arming.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** User investigates and provides a launch file, attempts manual parameter setting workaround.
- **Flight log URL:** Not provided.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Manually set CAL_*_PRIME parameters to correct values (by mrivi).
- **Result of the operation after the user adopted suggestion 1:** Not explicitly mentioned, but implies it can temporarily resolve the issue.
- **Suggestion 2 provided by developers or other personnel:** Consider CI system improvements to simulate this scenario (by dagar).
- **Result of the operation after the user adopted suggestion 2:** Not explicitly mentioned.
- **Suggestion 3 provided by developers or other personnel:** Delete the parameter file in ~/.ros or use `catkin purge` to reset parameters (by mrivi).
- **Result of the operation after the user adopted suggestion 3:** Successfully resolves parameter loading issue, allowing new parameters to load.
- **Suggestion 4 provided by developers or other personnel:** Consider debugging noted peculiarities further (by julianoes and mrivi).
- **Result of the operation after the user adopted suggestion 4:** The issue was identified as due to parameter loading discrepancies, further monitored by developers.
- **Final resolution or status:** Attempts at solutions continue. The issue was marked as resolved by the closure on the master branch unless reopened if further issues persist.
