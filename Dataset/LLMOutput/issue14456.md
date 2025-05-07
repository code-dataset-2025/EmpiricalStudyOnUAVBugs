**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned
- **Software environment:** Not explicitly mentioned
- **Report time:** Mar 23, 2020
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**1f4b2d1

**Steps for bug reproduction:**

- **Step 1:** Takeoff in stabilized/altitude mode.<font color='red'>未注明运行环境是哪个仿真环境或是实机</font>
- **Step 2:** Set `MPC_TILTMAX_AIR >= 90`.
- **Step 3:** Switch to position control mode.

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** N/A
- **Behavior after step 3:** The position control system generates invalid setpoints, triggering warnings and a failsafe stop and wait condition.

**Expected behavior:**

- **Expected behavior 1:** The position control system should handle tilt limits of 90 degrees without generating invalid setpoints.
- **Expected behavior 2:** There should be no warnings or failsafe condition if the parameters are set to extreme values within operational limits.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** The user provided steps to reproduce the issue.
- **URL of the flight log provided by the user:** [Flight Log](https://logs.px4.io/plot_app?log=c772812b-eba6-47f0-b2ed-965f2e1d9f4a)

**Communication between developers or other personnel and the user:**

- No specific suggestions or results from developer communication were provided in the report.
