**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned
- **Software environment:** PX4 Autopilot
- **Report Time:** Oct 27, 2020
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**69986af

**Steps for bug reproduction:**

- **Step 1:** Use a VTOL Tailsitter type drone.
- **Step 2:** Perform a transition.

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** Very weird thrust fluctuations, seemingly taking two references from the MC and FW controllers.<font color='red'>在sitl gazebo中执行没有出现</font>

**Expected behavior:**

- **Expected behavior 1:** The thrust reference should be smooth during transition.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Setting `MPC_USE_HTE` to 0 seems to solve the issue, although not confirmed.
- **URL of the flight log provided by the user:**
  - [Log 1](https://logs.px4.io/plot_app?log=1e0b41e7-79d0-4d75-be15-27168f4274cc)
  - [Log 2](https://review.px4.io/plot_app?log=6ce3fbeb-33d0-44db-8232-f3f9dd0f87b2)

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** The issue might be related to the blending logic of MC and FW, toggling between two values (suggested by user RicardoM17 and mentioned by bresch).
- **Result of the operation after the user adopted suggestion 1:** Identified that setting `MPC_THR_MIN` affects the thrust "clipping" during transition.

- **Suggestion 2 provided by developers or other personnel:** The issue might occur due to the tailsitter doing its rotation by 90 degrees (discussed by bresch and RicardoM17).
- **Result of the operation after the user adopted suggestion 2:** N/A (no explicit result mentioned).

- **Suggestion 3 provided by developers or other personnel:** Check the blending of MC and FW during manual and stabilized modes in the firmware to address information being published from two different places (suggested by xdwgood).
- **Result of the operation after the user adopted suggestion 3:** Implementation of condition `_control_mode.flag_control_altitude_enabled` to address undesired overlaps in flight control during transition.

- **Suggestion 4 provided by developers or other personnel:** Developer sfuhrer proposed cherry-picking a commit that disables the transition flight task for tailsitters in manual mode.
- **Result of the operation after the user adopted suggestion 4:** Issue confirmed as resolved with subsequent commits, specifically #16244.

The issue was concluded as resolved with the development changes and no further actions were required from the user.
