**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned
- **Software environment:** PX4 Autopilot, ROS
- **Report time:** Sep 3, 2022
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**7bbdc22

**Steps for bug reproduction:**

- **Step 1:** Clone the PX4 repository.
- **Step 2:** Run the command `no_sim=1 make px4_sitl_default gazebo`.

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** The simulator launches despite the `no_sim=1` flag.

**Expected behavior:**

- **Expected behavior 1:** The PX4 SITL should start without launching a Gazebo simulator.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Attempted to use the `no_sim=1` flag to prevent the simulator from launching.
- **URL of the flight log provided by the user:** Not provided.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `dagar` suggested running the PX4 binary directly after compiling and provided commands for doing so, mentioning a need for document synchronization due to changes.
- **Result of the operation after the user adopted suggestion 1:** `Returncode13` acknowledged the workaround and mentioned the use case, indicating the issue was a learning exercise and confirmed closing the issue.
- **Suggestion 2 provided by developers or other personnel:** Not provided.
- **Result of the operation after the user adopted suggestion 2:** Not applicable.

