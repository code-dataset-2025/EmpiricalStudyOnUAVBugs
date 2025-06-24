**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned
- **Software environment:** PX4 Autopilot version v1.13.3
- **Report Time:** Apr 26, 2023
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**0afd93a

**Steps for bug reproduction:**

- **Step 1:** Add the following to `msg/tools/urtps_bridge_topics.yaml`:
  ```bash
  - msg: vehicle_torque_setpoint
    receive: true
  - msg: vehicle_thrust_setpoint
    receive: true
  ```
- **Step 2:** Launch the script to generate the topic.
- **Step 3:** Clean the ROS 2 workspace and build again with the script in the package `px4_ros_com`.
- **Step 4:** Set `<enable_lockstep>0</enable_lockstep>` in the `.sdf.jinja` file of the desired drone (iris).
- **Step 5:** Start the simulation with `make px4_sitl_rtps gazebo`.
- **Step 6:** Start the micrortps agent with `micrortps_agent -t UDP`.<font color='red'>执行micrortps_agent -t UDP命令返回错误micrortps命令无法找到，搜索后发现https://github.com/PX4/PX4-Autopilot/issues/20952中提到micrortps_agent不在px4中使用</font>
- **Step 7:** Check that the topics for the torques and thrust are available.
- **Step 8:** Open QGroundControl (QGC).
- **Step 9:** Launch the offboard application to arm the drone and send full thrust on Z.

**Observed behavior by the user:**
- **Behavior after step 9:** The drone gets armed but the propellers don't spin, even though the topic is receiving the message.

**Expected behavior:**
- **Expected behavior 1:** The drone should arm.
- **Expected behavior 2:** The propellers should spin after arming.

**Additional information provided by the user for bug investigation:**
- **Actions taken by the user:** Investigated configuration of control allocation parameters; found the PWM_MAIN_FUNC parameter was missing.
- **URL of the flight log provided by the user:** [Log file](https://review.px4.io/plot_app?log=ebfc4251-ef61-4a8a-b592-deee7df20a88)

**Communication between developers or other personnel and the user:**
- **Suggestion 1 provided by developers or other personnel:** Fill `timestamp_sample` in the OffboardControlMode message; verify control allocation module is active.
- **Result of the operation after the user adopted suggestion 1:** The user found that a configuration error in control allocation parameters was the issue.
- **Suggestion 2 provided by developers or other personnel:** Provided a link to documentation for the offboard flight mode.
- **Result of the operation after the user adopted suggestion 2:** The user resolved the issue by correcting the control allocation configuration and thanked the developer for their assistance.
