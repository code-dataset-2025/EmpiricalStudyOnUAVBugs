**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned
- **Software environment:** Firmware version 10.0, Gazebo 9.0
- **Report Time:** Feb 19, 2020
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**01b280f

**Steps for bug reproduction:**

- **Step 1:** Execute `git checkout v1.10.0`.
- **Step 2:** Execute `git submodule update --init --recursive`.
- **Step 3:** Install dependencies using `pip install jinja2 empy catkin_pkg toml numpy`.
- **Step 4:** Set the simulation speed factor with `export PX4_SIM_SPEED_FACTOR=20`.
- **Step 5:** Build and run the simulation using `make px4_sitl gazebo_plane`.
- **Step 6:** In the PX4 console, execute `commander takeoff`.

**Observed behavior by the user:**

- **Behavior after step 1 to step 5:** N/A
- **Behavior after step 6:** The real time factor for the simulation goes consistently down from about 16 to 5 in 10 minutes.

**Expected behavior:**

- **Expected behavior 1:** The real time factor should remain stable and not decrease consistently.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Described bug reproduction steps and provided log files and gz stats via a link (though not specified).
- **URL of the flight log provided by the user:** Not explicitly mentioned in the document.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `julianoes` acknowledged the issue and indicated intentions to reproduce it.
- **Result of the operation after the user adopted suggestion 1:** N/A (the suggestion was acknowledgment)

- **Suggestion 2 provided by developers or other personnel:** Developer `shrit` suspected an issue related to SDF files and offered commit details for further investigation.
- **Result of the operation after the user adopted suggestion 2:** User `vwueest` attempted to apply the suggested commit but faced compatibility issues with required PX4 versions.

- **Suggestion 3 provided by developers or other personnel:** Developer `shrit` guided on checking out specific commits from submodules and described a workaround.
- **Result of the operation after the user adopted suggestion 3:** User `vwueest` followed instructions but still encountered compatibility issues with PX4 versions required for their setup, and sought further assistance.

- **Additional exchanges:** Developers discussed the possibility of profiling the simulation to identify performance degradation causes.
