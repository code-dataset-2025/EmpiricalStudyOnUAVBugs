**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned
- **Software environment:** PX4 Autopilot
- **Report Time:** Mar 5, 2020
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**4698a09

**Steps for bug reproduction:**

- **Step 1:** Execute `make px4_sitl gazebo_iris_opt_flow`.
- **Step 2:** Attempt to switch to position control.
- **Step 3:** Switch to altitude control to takeoff, then attempt to switch to position control again.

**Observed behavior by the user:**

- **Behavior after step 1:** Simulation runs with the optical flow model.
- **Behavior after step 2:** Unable to switch to position control.
- **Behavior after step 3:** Unable to switch to position control after taking off in altitude control.

**Expected behavior:**

- **Expected behavior 1:** Position control should work when there is GPS input available.
- **Expected behavior 2:** Seamless transition between altitude control and position control should be possible in the simulated environment.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** The user observed the number of good optical flow matches and checked the LOCAL_POSITION_NED velocity estimates.
- **URL of the flight log provided by the user:** [Log flight](https://logs.px4.io/plot_app?log=aa17113c-b016-4118-a14c-b5c63bca6281)

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `Jaeyoung-Lim` inquired if the issue was still present.
- **Result of the operation after the user adopted suggestion 1:** User `julianoes` reported the issue of the drone flipping in Gazebo 11 and attempted takeoff issues in ALTCTL.
- **Suggestion 2 provided by developers or other personnel:** Not explicitly mentioned, but `julianoes` reported on May 26, 2020, that the issue had resolved even when GPS was disabled.

**Result of the operation after the user adopted suggestion 2:** The issue was resolved as reported by `julianoes` on May 26, 2020.
