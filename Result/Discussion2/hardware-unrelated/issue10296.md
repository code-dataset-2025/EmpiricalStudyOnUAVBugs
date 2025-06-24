**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned
- **Software environment:** Not explicitly mentioned
- **Report Time:** Aug 21, 2018
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**0935354

**Steps for bug reproduction:**

- **Step 1:** Use the current master branch of PX4 Autopilot.
- **Step 2:** Cause an RC loss.

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** The vehicle yaws to the home heading upon losing RC connection even though loiter is set as RC loss behavior.<font color='red'>在sitl中打开再禁用虚拟手柄模拟RC LOSS，无人机确实发生偏航，但朝向不对着起始点和结束点</font>

**Expected behavior:**

- **Expected behavior 1:** The vehicle should maintain its current heading when RC loss occurs.
- **Expected behavior 2:** The failsafe conditions should not trigger unwanted behaviors like unintended yawing.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** The user noticed the issue is related to a failsafe being hit due to `FlightTasks::update()` failing in `mc_pos_control_main.cpp`.
- **URL of the flight log provided by the user:** [Flight Log](https://review.px4.io/plot_app?log=d9f20475-0558-45f8-9fc9-56d7389f173c)

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `Stifael` explained that the random yawing happens as the `mc_pos_control_main` takes time to receive the auto-loiter command from the commander upon RC loss. Planned to add a task that doesn't require RC.
- **Result of the operation after the user adopted suggestion 1:** N/A (No explicit operation adoption was mentioned).
  
- **Suggestion 2 provided by developers or other personnel:** `Stifael` noted that if `MPC_YAW_MODE` is set towards home, RC loss would cause yaw to home heading. Recommended setting it differently if undesired.
- **Result of the operation after the user adopted suggestion 2:** Developer `dakejahl` clarified that `MPC_YAW_MODE` was not set explicitly, and confirmed seeing changes but still faced intermittent issues.
  
- **Suggestion 3 provided by developers or other personnel:** `Stifael` further suggested a methodology using a yaw-lock during situations where the vehicle is within `NAV_ACC_RAD` to prevent unwanted yawing, while also acknowledging a bug in the navigator.
- **Result of the operation after the user adopted suggestion 3:** `dakejahl` conducted flight tests that confirmed the issue was resolved.
