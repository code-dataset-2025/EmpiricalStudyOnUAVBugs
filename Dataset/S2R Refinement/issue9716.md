**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned 
- **Software environment:** PX4 Autopilot
- **Report Time:** Jun 19, 2018
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**89a9025

**Steps for bug reproduction:**

- **Step 1:** Set `EKF2_MAG_TYPE` to 4
- **Step 2:** Reboot vehicle or restart EKF2 in SITL (`gazebo_iris_opt_flow`)

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** The EKF does not initialize or produce an attitude estimate<font color='red'>命令行ekf2 status显示有所不同，但都是不可用（报告上为ok no，执行的结果为invalid）</font>

**Expected behavior:**

- **Expected behavior 1:** The EKF should initialize
- **Expected behavior 2:** The EKF should produce an attitude estimate

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** The user provided a SITL log link for further investigation: [Log from SITL](https://logs.px4.io/plot_app?log=5c2e7e20-35de-4278-bee8-40ba1b92c242)

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `priseborough` provided a link to a fix and noted an issue with sensor noise causing yaw drift.
- **Result of the operation after the user adopted suggestion 1:** User `mhkabir` confirmed yaw drift on the ground and in the air with a temperature-calibrated gyro, and provided a replay log for further analysis ([Replay log](https://review.px4.io/plot_app?log=c3632182-1b19-4c9c-9a19-a2816d6b982c)).
- **Suggestion 2 provided by developers or other personnel:** `priseborough` requested data logging from boot for debugging.
- **Result of the operation after the user adopted suggestion 2:** `mhkabir` acknowledged the lack and promised to provide logging from boot.
- **Suggestion 3 provided by developers or other personnel:** `priseborough` pinged `mhkabir` for updates.
- **Result of the operation after the user adopted suggestion 3:** No direct result as `probe` awaited further action from `mhkabir`.
- **Other contributions:** The issue was marked as stale and subsequently closed due to inactivity by the `stale` bot.
