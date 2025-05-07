**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned
- **Software environment:** PX4 Autopilot with commit version 01db98f (latest master as of 2021-11-30)
- **Report Time:** Nov 30, 2021
- **PX4 Autopilot commit version:** 01db98f

**Steps for bug reproduction:**

- **Step 1:** Flash Pixhawk 4 with the latest master (2021-11-30, commit version 01db98f).
- **Step 2:** Boot with an airframe, for example, quad_x 4001.
- **Step 3:** Look for parameters named PWM_MAIN_TRIMx in the editor.

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** N/A
- **Behavior after step 3:** The editor shows all PWM_MAIN_{DISx, FAILx, MAXx, MINx, REVx} but does not show the TRIM parameters (PWM_MAIN_TRIMx).

**Expected behavior:**

- **Expected behavior 1:** PWM_MAIN and PWM_AUX should offer the same parameter set, including TRIM parameters.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** The user did a quick debug and suspected a race condition where mixers are not loaded when the first parameter update is completed. The user tested changing a parameter and reloading the ground station while the autopilot was still running, which resulted in the parameters becoming visible.
- **URL of the flight log provided by the user:** Not provided.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** The user mentioned they would create a pull request to remove the condition preventing parameter discovery but requested another developer, `@dagar`, to check for potential side effects.
- **Result of the operation after the user adopted suggestion 1:** N/A (the pull request process is mentioned, and the potential check by `@dagar` is pending).
