**Environment where the bug occurred:**

- **Hardware environment:** Raspberry Pi 4, Pixhawk 4 mini
- **Software environment:** ROS2 Humble, micro_ros_agent on the Raspberry Pi, PX4 Autopilot (commit version not mentioned)
- **Report Time:** Nov 18, 2022
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**b36758b

**Steps for bug reproduction:**

- **Step 1:** Prepare the flight controller for HITL mode and install micro-ros-agent on the companion computer.
- **Step 2:** Setup the cabling between the companion computer and the Pixhawk 4 mini.
- **Step 3:** Start HITL environment with the Pixhawk 4 mini connected to the development computer via USB.
- **Step 4:** On the companion computer, run `ros2 run micro_ros_agent micro_ros_agent serial --dev /dev/ttyAMA1 -b 921600 -v`.
- **Step 5:** In QGC, open the mavlink shell of the Pixhawk 4 mini and run `microdds_client start -t serial -d /dev/ttyS1 -b 921600`.

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** N/A
- **Behavior after step 3:** N/A
- **Behavior after step 4:** Communication starts but aborts quickly with a segmentation fault error.
- **Behavior after step 5:** An error message is received stating "create entities failed: participant: 255".

**Expected behavior:**

- **Expected behavior 1:** The agent and the client should communicate successfully as they do in SITL.
- **Expected behavior 2:** The system should perform as expected when using UDP communication in a SITL environment.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Tried launching the agent with different verbosity levels; tested with a different setup involving a Pixhawk 4 on TELEM 2 port; attempted to reinstall micro_ros_agent and encountered a dynamic library conflict warning.
- **Additional context:** Verification of the serial connection by accessing the Mavlink shell with mavlink_shell.py, disabling MAVLink on TELEM 1, setting the serial baud rate, and enabling XRCE_DDS on TELEM1.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Try running the agent with more verbosity to obtain helpful information.
- **Result of the operation after the user adopted suggestion 1:** User still received errors, with additional debug messages that were unclear.
- **Suggestion 2 provided by developers or other personnel:** Consider trying communication without specifying the agent's address in order to start the client automatically using parameters in the SD card.
- **Result of the operation after the user adopted suggestion 2:** User found that specifying agent address (-h option) was necessary to start communication properly.

Additional interactions highlighted alternative approaches like using Micro XRCE-DDS Agent instead of micro-ros-agent, clarifications on required configurations, and other technical setup and troubleshooting steps were discussed.
