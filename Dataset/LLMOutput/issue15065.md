**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned
- **Software environment:** PX4 Autopilot with commit version not mentioned
- **Report Time:** Jun 9, 2020
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**13d983d

**Steps for bug reproduction:**

- **Step 1:** Use failure injection using mavlink and systemcmd.<font color='red'>failure injection找不到导致第四步无法找到该参数</font>
- **Step 2:** Execute `make px4_sitl jmavsim`.
- **Step 3:** Take off and fly in POSCTL (e.g., using Joystick in QGC).
- **Step 4:** Enable failure injection by setting the parameter `SYS_FAILURE_EN` to `1`.
- **Step 5:** Trigger GPS lost using the command `failure gps off`.

**Observed behavior by the user:**

- **Behavior after step 1:** Failure injection setup completed successfully.
- **Behavior after step 2:** Simulator initialized and the vehicle is ready for testing.
- **Behavior after step 3:** Vehicle is flying in Position Control mode (POSCTL).
- **Behavior after step 4:** Failure injection was enabled.
- **Behavior after step 5:** Upon GPS loss, the vehicle initiates a blind landing despite the mode displayed in QGroundControl (QGC) being ALTCTL. The user can still switch to manual control, but they may not react in time.

**Expected behavior:**

- **Expected behavior 1:** Upon GPS loss in Position Control (POSCTL), the vehicle should transition to Altitude Control (ALTCTL), allowing the pilot to bring the vehicle back safely.
- **Expected behavior 2:** In Return-To-Launch (RTL), the vehicle should also behave as described in the failsafe logic, ensuring pilot control is retained.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** The user conducted systematic tests, including failure injection, logging parameters, and triggering GPS loss during flight.
- **URL of the flight log provided by the user:** 
  - [Log for POSCTL testing](https://logs.px4.io/plot_app?log=8bd577fe-63ea-41da-8846-33f2fef20db5)
  - [Log for RTL testing](https://logs.px4.io/plot_app?log=95824b1d-61df-4a02-ae1b-654f9a8e40d6)

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `MaEtUgR` pointed out that the failsafe mode is setting invalid horizontal position/velocity setpoints, triggering an error handler that initiates emergency landings.
  - **Result of the operation after the user adopted suggestion 1:** N/A (this was an observation and explanation, not an actionable suggestion).

- **Suggestion 2 provided by developers or other personnel:** Developer `MaEtUgR` further analyzed that the Altitude mode fails if the `activate()` and the first `update()` calls happen simultaneously in SITL due to zero delta time. A pull request (PR) was proposed to address this timing issue: [PX4/PX4-ECL#842](https://github.com/PX4/PX4-ECL/pull/842).
  - **Result of the operation after the user adopted suggestion 2:** The developer verified the issue was resolved on the master branch, and the PR was merged.

- **Suggestion 3 provided by developers or other personnel:** The issue was double-checked by `MaEtUgR` and confirmed as not reproducible after the fix.
  - **Result of the operation after the user adopted suggestion 3:** The issue was marked as resolved.

