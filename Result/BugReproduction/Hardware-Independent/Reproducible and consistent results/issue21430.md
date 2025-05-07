**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned
- **Software environment:** PX4 Autopilot with ROS2 and Micro-XRCE-DDS setup
- **Report Time:** Apr 5, 2023
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**94fb334

**Steps for bug reproduction:**

- **Step 1:** Add specific lines to `dds_topics.yaml` in the `microdds_client` module.
- **Step 2:** Launch any PX4_SITL vehicle (e.g., using `make px4_sitl gz_x500`).
- **Step 3:** Connect a Micro-XRCE-Agent as described in the [PX4 ROS2 communication setup](https://docs.px4.io/main/en/ros/ros2_comm.html#setup-xrce-dds-agent-client).
- **Step 4:** Check which types of publishers are created by the `microdds_client`.

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** N/A
- **Behavior after step 3:** N/A
- **Behavior after step 4:** The `/fmu/out/vehicle_command_ack` topic is not visible as a ROS2 topic.

**Expected behavior:**

- **Expected behavior 1:** The topic `/fmu/out/vehicle_command_ack` should be visible as a ROS2 topic.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** None explicitly mentioned, but followed steps for reproducing the issue and was able to see the BatteryStatus message working.
- **URL of the flight log provided by the user:** Not provided.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `beniaminopozzan` mentioned that the DDS publishers are created after the first message is received by the client and suggested sending any `VehicleCommand` message after the client has started.
- **Result of the operation after the user adopted suggestion 1:** `kribe48` acknowledged the suggestion and expressed gratitude, indicating the suggestion was effective in clarifying their understanding.
