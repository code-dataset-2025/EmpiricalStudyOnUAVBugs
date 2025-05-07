**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned
- **Software environment:** PX4 Autopilot
- **Report Time:** Sep 12, 2018
- **PX4 Autopilot commit version:** 273988c

**Steps for bug reproduction:**

- **Step 1:** Execute `make clean`.
- **Step 2:** Run `make posix_sitl_default gazebo_standard_vtol`.
- **Step 3:** Quit the application.
- **Step 4:** Run `make posix_sitl_default gazebo_standard_vtol` again.
- **Step 5:** Arm the drone.

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** Simulation runs successfully for the first time.
- **Behavior after step 3:** Application quits as expected.
- **Behavior after step 4:** Simulation goes wild right after arming.

**Expected behavior:**

- **Expected behavior 1:** The simulation should run successfully every time without requiring a `make clean` between runs.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** The user identified the problematic commit: "SITL: move all models to unified rcS startup and remove old scripts (commit 273988c)".
- **URL of the flight log provided by the user:** Not provided.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Not explicitly mentioned in the document.
- **Result of the operation after the user adopted suggestion 1:** N/A (no specific suggestions were made).
