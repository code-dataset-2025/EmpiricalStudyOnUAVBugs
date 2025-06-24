**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned
- **Software environment:** PX4 Autopilot, specifically using the iris_vision model in Gazebo SITL
- **Report Time:** Oct 7, 2019
- **PX4 Autopilot commit version:** Current master and an older commit (190c817)

**Steps for bug reproduction:**

- **Step 1:** Modify `iris_vision.world` by changing the pose to `<pose>1.01 0.98 0.83 0 0 -1.5</pose>`.<font color='red'>修改.world中的pose</font>
- **Step 2:** Run `make px4_sitl gazebo_iris_vision`.
- **Step 3:** Switch to position mode.
- **Step 4:** Take off and hover a few meters above the ground.

**Observed behavior by the user:**

- **Behavior after step 3:** N/A
- **Behavior after step 4:** After a few seconds, the copter flies away at full speed, and the failsafe is triggered, switching it to Altitude mode.

**Expected behavior:**

- **Expected behavior 1:** Vision position estimation should be independent of the initial yaw of the copter.
- **Expected behavior 2:** The behavior either consistently works or consistently fails, regardless of initial yaw.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Tested across different versions, confirmed the problem exists in v1.9.2 and with prior commits.
- **URL of the flight log provided by the user:** Not provided.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `TSC21` inquired about the version of the firmware.
- **Result of the operation after the user adopted suggestion 1:** User confirmed testing with both current master and older versions.
- **Suggestion 2 provided by developers or other personnel:** Developer `julianoes` suggested removing `-Werror` to compile version 1.9.2.
- **Result of the operation after the user adopted suggestion 2:** User confirmed that the issue persists in v1.9.2.
- **Suggestion 3 provided by developers or other personnel:** Developer `kamilritz` suggested a possible fix in PX4/PX4-SITL_gazebo-classic#399.
- **Result of the operation after the user adopted suggestion 3:** Not explicitly mentioned, but this was implied as a suggested solution.
