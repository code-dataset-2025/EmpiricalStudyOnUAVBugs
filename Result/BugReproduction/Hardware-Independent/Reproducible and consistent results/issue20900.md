**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned
- **Software environment:** Not explicitly mentioned
- **Report Time:** Jan 10, 2023
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**af33671

**Steps for bug reproduction:**

- **Step 1:** Use the command `make px4_sitl gazebo_iris_valgrind`.

**Observed behavior by the user:**

- **Behavior after step 1:** Valgrind reports a conditional jump or move depends on uninitialized value(s), specifically involving the variable `alt_reset_counter` in `EKF2Selector::PublishVehicleGlobalPosition()`.

**Expected behavior:**

- **Expected behavior 1:** The variable `alt_reset_counter` should be initialized to avoid potential issues during execution.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** The user assumed that the variable should be initialized but was unsure if setting it to 0 was sufficient or if it should be tracked as a private member variable.
- **URL of the flight log provided by the user:** Not provided.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `dagar` acknowledged the report and mentioned fixing it in PR #20906. They noted a desire to keep Valgrind and address sanitizer running clean but mentioned the challenge of speed on GitHub Actions.
- **Result of the operation after the user adopted suggestion 1:** Not applicable (no action required by the user).
