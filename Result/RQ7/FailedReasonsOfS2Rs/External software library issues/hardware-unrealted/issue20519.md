**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned, but the issue was reported using iris SITL gazebo simulation.
- **Software environment:** PX4 Autopilot without a specific commit version mentioned.
- **Report Time:** Oct 31, 2022
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**6d2dd79

**Steps for bug reproduction:**

- **Step 1:** Start the system's main branch using the micro-ros-agent.<font color='red'>执行micrortps_agent -t UDP命令返回错误micrortps命令无法找到，搜索后发现https://github.com/PX4/PX4-Autopilot/issues/20952中提到micrortps_agent不在px4中使用</font>
- **Step 2:** Begin an offboard script that publishes trajectory_setpoint messages (e.g., using a script from https://github.com/Jaeyoung-Lim/px4-offboard).
- **Step 3:** Stop the script by pressing `ctrl + c` in the terminal.
- **Step 4:** Observe that no failsafe message appears in QGroundControl, and the drone remains in offboard mode without being affected by the on-screen joystick.

**Observed behavior by the user:**

- **Behavior after Step 1:** N/A (no issue noted at this stage).
- **Behavior after Step 2:** The drone operates using the received trajectory setpoints.
- **Behavior after Step 3:** The drone continues to use the last received velocity setpoint and descends in offboard mode despite not receiving new trajectory setpoint messages.
- **Behavior after Step 4:** No failsafe is activated; the drone ignores manual joystick inputs.

**Expected behavior:**

- **Expected behavior 1:** A failsafe should activate when offboard setpoint streaming is stopped.
- **Expected behavior 2:** The drone should not remain in offboard mode when setpoint messages stop, and it should respond to manual joystick inputs.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** The user provided a flight log URL: https://logs.px4.io/plot_app?log=ed7a2222-3de3-4eec-88ba-0c2ca5aa4225.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `bkueng` asked the user to try the fix provided in PR #20535.
- **Result of the operation after the user adopted suggestion 1:** The user, `TedObrien`, confirmed that the issue was fixed; however, noted that the drone returns to offboard mode if setpoint streaming resumes post-failsafe, without user command, only from the failsafe state.
- **Suggestion 2 provided by developers or other personnel:** `bkueng` explained that the failsafe state clears automatically and offered to change this behavior if desired.
- **Result of the operation after the user adopted suggestion 2:** N/A (the user did not specifically respond to this suggestion).

**Additional comments:**

- The user noted that joystick input does not trigger a failsafe, which was a feature in previous versions, and expressed a preference for its return as a safety feature. `bkueng` explained where this behavior is handled in the codebase (https://github.com/PX4/PX4-Autopilot/blob/main/src/modules/commander/Commander.cpp#L2731) and asked if the user had the appropriate parameter set.
