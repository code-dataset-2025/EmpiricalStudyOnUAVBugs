**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned
- **Software environment:** Not explicitly mentioned
- **Report Time:** Feb 27, 2019
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**e7dfb37

**Steps for bug reproduction:**

- **Step 1:** jMAVSim test in position control mode (default smoothing or velocity smoothing).<font color='red'>启动jmavsim在编译进度条结束后，启动GUI时遇到错误Inconsistency detected by ld.so: dl-lookup.c: 111: check_match: Assertion `version->filename == NULL || ! _dl_name_match_p (version->filename, map)' failed!</font>
- **Step 2:** Log `vehicle_attitude_setpoint`, `vehicle_local_position`, and `vehicle_local_positon_setpoint` at full speed.
- **Step 3:** Set `MPC_VEL_MANUAL` to a small value to be able to give constant full stick and stay far from any saturation (3 m/s, for example).
- **Step 4:** Takeoff and fly full stick straight to the North.

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** N/A
- **Behavior after step 3:** N/A
- **Behavior after step 4:** Attitude twitches due to the velocity controller, with thrust/pitch/pitchrate setpoint glitches despite smooth velocity.

**Expected behavior:**

- **Expected behavior 1:** A smooth flight without attitude glitches.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Investigated the control loop jitter as a potential source of glitches by examining the timing of setpoint generation relative to estimates.
- **URL of the flight log provided by the user:** [Flight log](https://logs.px4.io/plot_app?log=a63b076d-b174-40d0-80f3-a57bc4f6a87b)

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** None explicitly mentioned; however, the issue was acknowledged by tagging other developers.
- **Result of the operation after the user adopted suggestion 1:** Not applicable as there wasn't a suggestion for action.
- **Discussion update:** After further investigation, `bresch` noted on Jun 25, 2019, that the problem had not been observed again.
