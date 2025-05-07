**Environment where the bug occurred:**

- **Hardware environment:** Pixhawk 4
- **Software environment:** PX4 Autopilot v1.13.0-beta1, Gazebo 11
- **Report Time:** May 17, 2022
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**ff16131

**Steps for bug reproduction:**

- **Step 1:** Plug the Pixhawk 4 with PX4 v1.13.0-beta1 and HITL airframe config to USB port.
- **Step 2:** Wait for the Pixhawk 4 to boot.
- **Step 3:** Run the command `gzserver --verbose Tools/sitl_gazebo/worlds/hitl_iris.world`.

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** N/A
- **Behavior after step 3:** The simulation encounters a Tx queue overflow error after attempting to connect to the USB port.

**Expected behavior:**

- **Expected behavior 1:** Gazebo should not go into a Tx queue overflow.
- **Expected behavior 2:** The drone should be visible in QGroundControl (QGC) through UDP.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Tried using the master branch, installed a new Ubuntu 20.04, used a new Pixhawk 4, and confirmed that v1.12.3 works fine with Gazebo.
- **URL of the flight log provided by the user:** Not provided

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Julianoes identified that Gazebo HITL does not send MAVLink heartbeats, causing the mavlink instance not to start on the PX4 side.
- **Result of the operation after the user adopted suggestion 1:** Sending heartbeats more frequently during startup was implemented as a fix.
- **Suggestion 2 provided by developers or other personnel:** Use the path by id, such as /dev/serial/by-id/..., to avoid serial port instance number issues.
- **Result of the operation after the user adopted suggestion 2:** It provided insight into dealing with serial port issues but did not resolve individual model-specific issues described later by AllenHuangDongyue.
- **Suggestion 3 provided by developers or other personnel:** For issues with custom models, it might be due to the amount of data being sent from Gazebo filling up the TX buffer. 
- **Result of the operation after the user adopted suggestion 3:** AllenHuangDongyue acknowledged this as a plausible explanation but did not resolve the issue for custom models with tiltable rotors.
