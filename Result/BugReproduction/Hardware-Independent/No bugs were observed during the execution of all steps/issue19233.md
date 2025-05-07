**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned
- **Software environment:** PX4 Autopilot, SITL with Gazebo
- **Report Time:** Feb 20, 2022
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**cc6c6c3

**Steps for bug reproduction:**

- **Step 1:** Run `make px4_sitl gazebo_rover`.
- **Step 2:** See error logs indicating missing mixers and inability to load properly.

**Observed behavior by the user:**

- **Behavior after step 1:** The rover SITL model fails to move.
- **Behavior after step 2:** Errors regarding missing mixers are displayed, and the rover does not function as expected.

**Expected behavior:**

- **Expected behavior 1:** The rover should start and move in the Gazebo simulation without errors.
- **Expected behavior 2:** The rover should have the appropriate mixer configuration to control it correctly in SITL.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** User attempted to investigate the issue by tagging developers for suggestions.
- **URL of the flight log provided by the user:** Not provided.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** User `oceanusxiv` mentioned changes in mixer settings, specifically adjusting PWM_MAIN_FUNC6.
- **Result of the operation after the user adopted suggestion 1:** The user continued experiencing issues with position control and steering oscillation, indicating partial understanding and resolution.

