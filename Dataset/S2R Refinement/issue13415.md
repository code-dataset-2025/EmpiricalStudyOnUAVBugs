**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned
- **Software environment:** PX4 Autopilot with Firmware version 1.9.2 (including #13312 and #13325)
- **Report Time:** Nov 7, 2019
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**b943bd7

**Steps for bug reproduction:**

- **Step 1:** Switch from manual to position mode.
- **Step 2:** Increase the velocity before switching modes for more noticeable effects.

**Observed behavior by the user:**

- **Behavior after step 1:** Experience a violent jerk when switching modes.
- **Behavior after step 2:** The jerk becomes more violent with higher velocities.

**Expected behavior:**

- **Expected behavior 1:** Smooth transition without large attitude controller demands.
- **Expected behavior 2:** Minimal or no jerks during mode switching.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Detuned the P gain on the velocity controller but still observed the issue.
- **URL of the flight log provided by the user:** [Flight Log](https://review.px4.io/plot_app?log=4fa7056e-d1bc-437f-829d-0b45e3087276)

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** mhkabir suggested trying v1.10.
- **Result of the operation after the user adopted suggestion 1:** Not specified.
- **Suggestion 2 provided by developers or other personnel:** bresch noted that the problem is with the initialization of the velocity controller, possibly due to the numerical derivative in the D-term of the controller.
- **Result of the operation after the user adopted suggestion 2:** A new simulation was run with the D gain set to 0, and no glitch was observed anymore.
