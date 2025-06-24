**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned
- **Software environment:** ROS with PX4 Autopilot
- **Report Time:** May 28, 2018
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**77cea88

**Steps for bug reproduction:**

- **Step 0:** Clone the PX4 Firmware inside the `ros_workspace/src` folder on the master branch.<font color='red'>ROS相关</font>
- **Step 1:** Build the package using the command `cd ros_workspace/src && catkin build px4`.
- **Step 2:** Observe the build process for errors.

**Observed behavior by the user:**

- **Behavior after step 0:** PX4 Firmware is cloned into the specified directory.
- **Behavior after step 1:** The build process fails with messages indicating that headers such as "ecl.h" cannot be found.

**Expected behavior:**

- **Expected behavior 1:** Successfully build PX4 as a ROS package without errors related to missing headers.
- **Expected behavior 2:** ROS environment is set up to work with PX4 Autopilot without manual intervention.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Attempted building with an earlier version (v1.7.3), which succeeded, suggesting an issue might have been introduced after that version.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `dagar` suggested adding a basic catkin build to Jenkins to ensure CI supports what is needed.
- **Result of the operation after the user adopted suggestion 1:** N/A (no specific result mentioned from this suggestion).

- **Suggestion 2 provided by developers or other personnel:** Developer `TSC21` acknowledged the task of adding the build to Jenkins but could not guarantee completion within the week.
- **Result of the operation after the user adopted suggestion 2:** N/A (no specific result mentioned from this suggestion).

- **Suggestion 3 provided by developers or other personnel:** Developer `dagar` mentioned a possible fix in PR #9679 and asked for testing.
- **Result of the operation after the user adopted suggestion 3:** No explicit follow-up, but a user indicated the problem persists.

- **Suggestion 4 provided by developers or other personnel:** Developer `TSC21` stated the issue was fixed in PR #10587.
- **Result of the operation after the user adopted suggestion 4:** No explicit follow-up, though another user later reported the issue in version 1.8.1, suggesting the fix might not have been complete.

Overall, the document illustrates a process of identifying, communicating, and working towards resolving a bug within a collaborative open-source project environment.
