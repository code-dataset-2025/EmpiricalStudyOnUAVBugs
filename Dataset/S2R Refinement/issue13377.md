**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned
- **Software environment:** PX4 Autopilot on Ubuntu 18.04, macOS, and Linux Fedora 30
- **Report Time:** Nov 4, 2019
- **PX4 Autopilot commit version:** Not explicitly mentioned (issues observed in v1.10.0-beta4 and current master)
- **last commit before the reporting time:**7b83da7

**Steps for bug reproduction:**

- **Step 1:** Start any Gazebo SITL simulation in headless mode, e.g., `HEADLESS=1 make px4_sitl gazebo_standard_vtol`.
- **Step 2:** Attempt to run the command a second time on the same PC start.

**Observed behavior by the user:**

- **Behavior after step 1:** Gazebo runs correctly in headless mode.
- **Behavior after step 2:** The following error occurs: `[Err] [gazebo_mavlink_interface.cpp:1155] poll timeout`, and trying to exit with Ctrl-C results in: `ERROR [px4] Startup script returned with return value: 2`.

**Expected behavior:**

- **Expected behavior 1:** Gazebo in headless mode runs without errors on subsequent runs.
  

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Not explicitly mentioned, but observed behavior on Ubuntu 18.04 and noted similar experiences by other users on different platforms.
- **URL of the flight log provided by the user:** Not provided.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Comment by `julianoes` noted the issue's inability to be reproduced on Fedora 30 but confirmed occurrence on macOS 10.14.6, and mentioned specific commits potentially causing the issue.
- **Result of the operation after the user adopted suggestion 1:** N/A (The suggestion was an acknowledgment and identification of possible problematic commits).
