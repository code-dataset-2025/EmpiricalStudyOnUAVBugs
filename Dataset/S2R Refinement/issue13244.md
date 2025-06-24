**Environment where the bug occurred:**

- **Hardware environment:** LJI500S test drone with NXP FMUK66 revC
- **Software environment:** Unknown, version v1.9.2 mentioned in comments
- **Report Time:** Oct 22, 2019
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**549fb0d

**Steps for bug reproduction:**

- **Step 1:** Set CBRK_FLIGHTTERM to 0 to enable the circuit breaker.
- **Step 2:** Set one of the PWM_MAIN_FAIL to 2000us and connect a servo to that PWM port.
- **Step 3:** Arm the drone and take off.
- **Step 4:** Force the drone to exceed the max roll/pitch angle of the default 60° (FD_FAIL_P and FD_FAIL_R).

**Observed behavior by the user:**
- **Behavior after step 1:** N/A
- **Behavior after step 2:** N/A
- **Behavior after step 3:** N/A
- **Behavior after step 4:** Motors do not stop, and a programmed PWM_MAIN_FAIL is not set (servo not moving).

**Expected behavior:**
- **Expected behavior 1:** Angle of more than 60 degrees should be detected.
- **Expected behavior 2:** Motors should stop.
- **Expected behavior 3:** PWM_MAIN_FAIL settings should become active.

**Additional information provided by the user for bug investigation:**
- **Actions taken by the user:** Configured RC loss failsafe to "Terminate" and tested this configuration by switching off the RC transmitter.
- **URL of the flight log provided by the user:** https://logs.px4.io/plot_app?log=58de9b83-0cf3-4e7f-9a0e-55df674bfdbf

**Communication between developers or other personnel and the user:**
- **Suggestion 1 provided by developers or other personnel:** `bresch` mentioned that the actual termination logic isn't present on v1.9.2 and suggested using the master or waiting for v1.10.
- **Result of the operation after the user adopted suggestion 1:** `dk7xe` confirmed it works well with the master version.
