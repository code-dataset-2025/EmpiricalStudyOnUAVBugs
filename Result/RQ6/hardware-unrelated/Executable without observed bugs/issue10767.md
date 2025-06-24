**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned
- **Software environment:** PX4 Autopilot
- **Report Time:** Oct 26, 2018
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**dc62454

**Steps for bug reproduction:**

- **Step 1:** Change the TOML file, e.g., change Cm of some motors to 10 times, which should only affect yaw motion.
- **Step 2:** Build the project.

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** Only the first column changes in the `mixer_multirotor_*.h` files followed for quadrotor x and y.

**Expected behavior:**

- **Expected behavior 1:** The change in the TOML file should only affect the yaw motion.
- **Expected behavior 2:** The order in the mixer table should be roll, pitch, yaw, throttle for hexarotors and similar for quadrotors.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** The user provided steps to reproduce the issue by changing the moment coefficient in the TOML file and observing the mixer matrix output.
- **URL of the flight log provided by the user:** Not provided.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Comment by `dagar` indicating the reference to the original pull request for context.
- **Suggestion 2 provided by developers or other personnel:** Comment by `jlecoeur`, explaining why the observed behavior is not a bug and providing a detailed explanation of how the effectiveness and mixer matrices work.
- **Result of the operation after the user adopted suggestion 1:** N/A (suggestion was informational)
- **Result of the operation after the user adopted suggestion 2:** The issue was determined to not be a bug, and no further action was taken.
