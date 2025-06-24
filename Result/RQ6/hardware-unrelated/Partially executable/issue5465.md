**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned
- **Software environment:** SITL with Gazebo
- **Report Time:** Sep 7, 2016
- **PX4 Autopilot commit version:** 010c9e9

**Steps for bug reproduction:**

- **Step 1:** Execute `make posix gazebo`.
- **Step 2:** Use the command `pxh> commander takeoff`.

**Observed behavior by the user:**

- **Behavior after step 1:** The simulation setup proceeds as expected.
- **Behavior after step 2:** The takeoff command does not execute properly due to the broken state of the simulation in Gazebo.

**Expected behavior:**

- **Expected behavior 1:** The simulation in Gazebo should run without issues.
- **Expected behavior 2:** The takeoff command should be executed successfully in the Gazebo simulation.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Bisected the issue to commit 010c9e9; identified that the issue appears on Ubuntu 16.04 with Gazebo 7 but works on Mac; performed a fresh checkout which resolved the immediate issue; cleaned the workspace using `git clean -d -f -x` in `Tools/sitl_gazebo`.
- **URL of the flight log provided by the user:** Not provided.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `LorenzMeier` suggested trying the branch `stack_abstraction` which addresses OS-specific stack size issues.
- **Result of the operation after the user adopted suggestion 1:** Not explicitly stated, but user `julianoes` resolved the issue through a fresh checkout and cleaning the workspace.
- **Suggestion 2 provided by developers or other personnel:** Developer `dagar` recommended using `make distclean` when switching between branches with significant changes.
- **Result of the operation after the user adopted suggestion 2:** Issue was resolved by cleaning the workspace, indicating that `make distclean` could be a useful step in managing similar issues.
