**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned
- **Software environment:** Ubuntu 20.04, ROS Noetic, PX4 built from source
- **Report Time:** Apr 6, 2023
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**8f520ab

**Steps for bug reproduction:**

- **Step 1:** Switch on the drone.
- **Step 2:** Upload the mission file (QGC mission file should be attached).<font color='red'>原报告任务文件缺失</font>
- **Step 3:** Take off.
- **Step 4:** Run the command `./rostest_px4_run.sh mavros_posix_tests_offboard_attctl.test` from the test directory.

**Observed behavior by the user:**

- **Behavior after step 1:** Not explicitly mentioned
- **Behavior after step 2:** Not explicitly mentioned
- **Behavior after step 3:** Not explicitly mentioned
- **Behavior after step 4:** `mavros_offboard_attctl_test` fails.

**Expected behavior:**

- **Expected behavior 1:** The test should pass.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Increased roll angle from -0.25 to -0.75, increased thrust from 0.7 to 1.0, and slightly decreased boundary values to make the test pass.
- **URL of the flight log provided by the user:** Not provided

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** No suggestions from other personnel were mentioned.
- **Result of the operation after the user adopted suggestion 1:** N/A (User made own adjustments which resulted in the test passing).
