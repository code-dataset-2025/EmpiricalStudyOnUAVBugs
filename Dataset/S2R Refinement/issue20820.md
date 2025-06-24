**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned
- **Software environment:** Ubuntu 20.04, ROS2 Foxy
- **Report Time:** Dec 22, 2022
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**c3e70b0

**Steps for bug reproduction:**

- **Step 1:** Launch the simulator by running:
    ```bash
    cd ~/PX4-Autopilot
    make px4_sitl gazebo
    ```
    
- **Step 2:** Launch `micrortps_agent`:
    ```bash
    source ~/px4_ros_com_ros2/install/setup.bash
    micrortps_agent -t UDP
    ```
    Resulted in an error: `micrortps_agent: command not found`.
    
- **Step 3:** Installed the microROS application and ran:<font color='red'>根据提供的网页安装microROS时执行到ros2 run micro_ros_setup create_agent_ws.sh时失败，返回报错信息E: Unable to locate package ros-humble-osrf-testing-tools-cpp
    ERROR: the following rosdeps failed to install
      apt: command [sudo -H apt-get install -y ros-humble-osrf-testing-tools-cpp] failed，这个包无法找到</font>
    
    ```bash
    source ~/microros_ws/install/local_setup.bash
    ros2 run micro_ros_agent micro_ros_agent udp4 --port 8888 -v
    ```
    Observed creation of topics successfully in the simulator terminal.
    
- **Step 4:** Modified `sensor_combined_listener.launch.py` to remove `ExecuteProcess` and ran:
    ```bash
    ros2 launch px4_ros_com sensor_combined_listener.launch.py
    ```
    The process started successfully, but no output was printed.
    
- **Step 5:** Manually subscribed to the topic:
    ```bash
    ros2 topic echo /fmu/out/sensor_combined
    ```
    Successfully received data from the topic.

**Observed behavior by the user:**

- **Behavior after step 1:** The simulator launched successfully and displayed the message `[commander] Ready for takeoff`.
- **Behavior after step 2:** Encountered an error: `micrortps_agent: command not found`.
- **Behavior after step 3:** The topics were successfully created, as seen in the simulator terminal.
- **Behavior after step 4:** The `sensor_combined_listener` launch process started, but no output was observed.
- **Behavior after step 5:** Successfully received data when manually subscribing to `/fmu/out/sensor_combined`.

**Expected behavior:**

- **Expected behavior 1:** The `sensor_combined_listener.launch.py` should print data from the `/fmu/out/sensor_combined` topic after being launched.
- **Expected behavior 2:** No errors should occur during the steps outlined above.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** 
    - Installed the microROS application.
    - Modified the `sensor_combined_listener.launch.py` file to remove `ExecuteProcess`.
    - Manually subscribed to the `/fmu/out/sensor_combined` topic and successfully verified that data was available.
- **URL of the flight log provided by the user:** Not provided.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** The issue might be due to mismatched QoS settings. Suggested verifying the QoS settings with:
    ```bash
    ros2 topic info /fmu/out/sensor_combined -v
    ```
- **Result of the operation after the user adopted suggestion 1:** The user was unable to match QoS settings and sought further guidance.
  
- **Suggestion 2 provided by developers or other personnel:** Recommended modifying the QoS settings in `sensor_combined_listener.cpp` as follows:
    ```cpp
    subscription_ = this->create_subscription<px4_msgs::msg::SensorCombined>("/fmu/out/sensor_combined", 
    rclcpp::QoS(rclcpp::KeepLast(1)).best_effort().durability_volatile(), 
    [this](const px4_msgs::msg::SensorCombined::UniquePtr msg) {
    ```
- **Result of the operation after the user adopted suggestion 2:** The issue was resolved. The user also identified that the launch file was missing the `output='screen'` parameter, which was added to fix the problem.
