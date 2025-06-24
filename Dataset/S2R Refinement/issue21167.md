**Environment where the bug occurred:**

- **Hardware environment:** Holybro v5
- **Software environment:** PX4 Autopilot from stable release/1.13
- **Report Time:** Feb 20, 2023
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**2008a44

**Steps for bug reproduction:**

- **Step 1:** Flash the Pixhawk from the stable release/1.13 with `CONFIG_MODULES_MICRODDS_CLIENT=n` parameter in `~/PX4-Autopilot/boards/px4/fmu-v5/rtps.px4board`
- **Step 2:** Set `RTPS_CONFIG` parameter to `TELEM2`, and then `SER_TEL2_BAUD` to `921600 8N1`.
- **Step 3:** Build the `px4_ros_com` workspace from the `release/1.13` branch.
- **Step 4:** Connect `TELEM2` and the PC through serial.
- **Step 5:** Run `rtps agent` with `micrortps_agent -t UART -d /dev/ttyUSB0 -b 921600`.
- **Step 6:** Run the `sensor_combined_listener`.
- **Step 7:** Attempt to run the `offboard_control`.

**Observed behavior by the user:**

- **Behavior after step 5:** The microRTPS Agent starts, indicating the connection of various subscribers and publishers.
- **Behavior after step 6:** Sensor data is correctly received by the `sensor_combined_listener`.
- **Behavior after step 7:** The offboard control node starts, an arm command is sent, but the drone does not arm.

**Expected behavior:**

- **Expected behavior 1:** The offboard control node should arm the drone successfully after running the necessary commands and configurations.
- **Expected behavior 2:** Successful communication and control of the drone through offboard control without the necessity of having a remote controller connected.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Highlighted the issue with RTPS configuration and offboard control node execution, provided the exact steps and output for reproduction, and pointed out that the presence of a remote controller is needed for arming in offboard mode.
- **URL of the flight log provided by the user:** Not provided.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Request for the flight log by beniaminopozzan.
- **Result of the operation after the user adopted suggestion 1:** User recognized a mistake and explained the need for a remote controller to be connected by default for offboard control.
  
- **Suggestion 2 provided by developers or other personnel:** Guidance on deactivating the need for a remote controller was provided by beniaminopozzan (parameters `COM_RCL_EXCEPT` and possibly `NAV_DLL_ACT` were mentioned).
- **Result of the operation after the user adopted suggestion 2:** Not explicitly outlined in the document.
