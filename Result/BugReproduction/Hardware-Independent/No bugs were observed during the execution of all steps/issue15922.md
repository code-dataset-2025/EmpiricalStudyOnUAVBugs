**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned
- **Software environment:** Ubuntu 18.04, Gazebo 9.0, ROS Melodic
- **Report Time:** Oct 9, 2020
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**f26d4f2

**Steps for bug reproduction:**

- **Step 1:** Checkout PX4 Firmware master
- **Step 2:** Run `make px4_sitl gazebo_boat`

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** Error occurs due to missing rc.boat_defaults file, preventing simulator startup.

**Expected behavior:**

- **Expected behavior 1:** The simulator should build and run successfully without errors.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** User solved the issue by downloading the rc.boat_defaults file from an older PX4 version (Stable Release v1.11.1) and placing it under the required directory to start the simulator.
- **URL of the flight log provided by the user:** None provided.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `Jaeyoung-Lim` acknowledged the report and mentioned that it was fixed in #15923.
- **Result of the operation after the user adopted suggestion 1:** N/A (fix was implemented in the subsequent pull request).
