**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned
- **Software environment:** Not explicitly mentioned
- **Report Time:** Sep 26, 2019
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**8ce4a15

**Steps for bug reproduction:**

- **Step 1:** Do a VTOL front transition in SITL (Software In The Loop simulation).
- **Step 2:** Perform the transition in any control mode (stabilized, altitude, position).

**Observed behavior by the user:**

- **Behavior after step 1:** No rate setpoints (`rate sp`) are published in the first second of a front transition.
- **Behavior after step 2:** The `rate_sp` freezes for 1 second at a large value when a roll input is given before the transition, almost resulting in a flip of the VTOL.<font color='red'>执行结束得到的log为https://review.px4.io/plot_app?log=3c809dff-0f7c-4324-b0bf-b5088c0c1bde，没有看出与原报告中相同的PWM型图形</font>

**Expected behavior:**

- **Expected behavior 1:** `rate sp` should be published immediately during a VTOL front transition.
- **Expected behavior 2:** There should be no freeze in `rate_sp` even when roll input is given before the transition.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** The user accidentally triggered the bug and provided a URL with a log file.
- **URL of the flight log provided by the user:** [Provided log file](https://review.px4.io/plot_app?log=7e8f18ac-0800-4c4b-a947-7773ed1ddc41)

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Not explicitly recorded.
- **Result of the operation after the user adopted suggestion 1:** Not applicable.
- **Suggestion 2 provided by developers or other personnel:** Not explicitly recorded.
- **Result of the operation after the user adopted suggestion 2:** Not applicable.

The communication mainly involves the user informing the developers, specifically tagging @dagar and @RomanBapst for their information.
