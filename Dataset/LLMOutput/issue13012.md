**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned
- **Software environment:** PX4 Autopilot when simulating with `px4_sitl gazebo_hippocampus`
- **Report Time:** Sep 23, 2019
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**bb88d4c

**Steps for bug reproduction:**

- **Step 1:** Execute `make px4_sitl gazebo_hippocampus`.

**Observed behavior by the user:**

- **Behavior after step 1:** Unable to use the commander takeoff function due to "ERROR [commander] rejecting takeoff, no position lock yet." There are also issues with the simulated GPS and the barometer/magnetometer sensor readings going stale on PX4 boot.

**Expected behavior:**

- **Expected behavior 1:** Successful execution of `commander takeoff` with position lock.
- **Expected behavior 2:** Consistent sensor readings without errors indicating stale data for barometer and magnetometer.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** No specific flight log URL provided, reported the absence of GPS lat/lon/alt information.
- **Console log indicates:** Barometer and magnetometer measurements go stale with the same timestamps shortly after PX4 boot.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Julianoes suggested running `git bisect` to identify when the issue arose.
- **Result of the operation after the user adopted suggestion 1:** Not explicitly mentioned, possibly indicating no resolution found by that process.
- **Suggestion 2 provided by developers or other personnel:** Julianoes inquired about running tests without lockstep enabled.
- **Result of the operation after the user adopted suggestion 2:** The issue persisted despite disabling lockstep.
- **Additional notes:** Developer Jaeyoung-Lim closed the issue on Feb 1, 2021, after confirming that it had been fixed in the latest master version.
