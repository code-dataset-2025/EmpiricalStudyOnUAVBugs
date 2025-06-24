**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned
- **Software environment:** Ubuntu 18.04, Melodic, newest version PX4-autopilot
- **Report Time:** Feb 6, 2023
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**2f21c59

**Steps for bug reproduction:**

- **Step 1:** Use the command `roslaunch px4 mavros_posix_sitl.launch`.<font color='red'>roslaunch报错 cannot import name 'Log' from 'rosgraph_msgs.msg'，改用ros2 launch报错Package 'px4' not found: "package 'px4' not found, searching:</font>
- **Step 2:** Navigate to `/PX4-Autopilot/integrationtests/python_src/px4_it/mavros/`.
- **Step 3:** Run the script `python2 mavros_offboard_posctl_test.py`.

**Observed behavior by the user:**

- **Behavior after step 1:** Simulation environment initiated with issues.
- **Behavior after step 2:** Readiness to execute test script.
- **Behavior after step 3:** Drone experiences Preflight Fail: High Accelerometer Bias errors, affecting vertical takeoff.

**Expected behavior:**

- **Expected behavior 1:** The drone takes off vertically without errors.
- **Expected behavior 2:** The drone should complete a perfect triangle trajectory.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** User attempted using `roslaunch` combined with different commands and compared with `make px4_sitl gazebo`.
- **URL of the flight log provided by the user:** https://youtu.be/rcNdcXxstQU

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Cleaning the `~/.ros` directory.
- **Result of the operation after the user adopted suggestion 1:** Not explicitly mentioned, but implied it may be helpful.
