**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned
- **Software environment:** SITL Gazebo with PX4 Autopilot
- **Report Time:** Nov 5, 2021
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**88489ae

**Steps for bug reproduction:**

- **Step 1:** Start SITL with a plane model using the command `make px4_sitl gazebo_plane`.
- **Step 2:** Start a mission with a takeoff waypoint.

**Observed behavior by the user:**

- **Behavior after step 1:** The system is executed and prepared in the simulated environment.
- **Behavior after step 2:** The imbalanced propeller warning is triggered, advising landing.

**Expected behavior:**

- **Expected behavior 1:** The fixed-wing should take off and execute the mission without triggering an imbalanced propeller warning.
- **Expected behavior 2:** Normal operational behavior without false positive warnings during takeoff.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Provided a log URL for investigation.
- **URL of the flight log provided by the user:** [Flight Log](https://logs.px4.io/plot_app?log=15f471bd-2a86-4855-9206-ce111cd0b393)

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** TSC21 suggested reducing the threshold for fixed-wing models in Gazebo.
- **Result of the operation after the user adopted suggestion 1:** N/A (suggestion under consideration)
- **Suggestion 2 provided by developers or other personnel:** Bresch mentioned increasing the threshold as a quick fix or making the detector less sensitive for a more permanent solution.
- **Result of the operation after the user adopted suggestion 2:** N/A (actions to take based on suggestions not explicitly outlined)
- **Suggestion 3 provided by developers or other personnel:** Dagar commented that the issue was fixed in commit #18590.
