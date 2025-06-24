**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned
- **Software environment:** PX4 Autopilot running in SITL using Gazebo-classic
- **Report Time:** Feb 2, 2023
- **PX4 Autopilot commit version:** Not explicitly mentioned
- **last commit before the reporting time:**e3d73cd

**Steps for bug reproduction:**

- **Step 1:** Launch SITL from within Docker.
- **Step 2:** Execute `./Tools/docker_run.sh 'make px4_sitl_nolockstep gazebo-classic_rover'`.<font color='red'>使用该提交执行显示找不到目标gazebo-classic_rover，但使用'make px4_sitl'可以成功跑通</font>
- **Step 3:** Observe errors in the shell.

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** N/A
- **Behavior after step 3:** Barometer timeout errors appear in the shell.

**Expected behavior:**

- **Expected behavior 1:** No barometer errors should appear.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** The user noted that the issue does not occur in the stable branch and also occurs as far back as commit 5a2e41c. The user also mentioned that certain NuttX commands (e.g., `ls`, `ps`) seem disabled in SITL.
- **URL of the flight log provided by the user:** [Flight Log](https://logs.px4.io/plot_app?log=0352673a-690e-41a0-93cd-363471be4c7a)

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** None provided in the comments, but the user `321thijs123` asked if the issue had been resolved, and `russkel` suggested turning off sensors using the `SYS_HAS_BARO` parameter as a workaround.
- **Result of the operation after the user adopted suggestion 1:** `russkel` did not provide specific results for adopting this suggestion but mentioned switching to Ardupilot due to better support.

