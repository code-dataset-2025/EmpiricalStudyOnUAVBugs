**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned
- **Software environment:** PX4 Autopilot versions V1.09 and V1.10
- **Report Time:** Nov 19, 2020
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**71306f7

**Steps for bug reproduction:**

- **Step 1:** Fly the drone in OFFBOARD mode frequently and for extended periods.<font color='red'>sitl中缺少外部信号源无法切换至offboard模式</font>

**Observed behavior by the user:**

- **Behavior after step 1:** The Pixhawk randomly switches from OFFBOARD mode to a different mode without any detectable reason such as offboard control failure or sensor failure. The mode switch is quick and often not recorded in the flight logs.

**Expected behavior:**

- **Expected behavior 1:** The UAV should not exit OFFBOARD mode without a valid reason.
- **Expected behavior 2:** If the UAV changes modes, it should switch into HOLD, POSITION, ALTITUDE, or STABILIZED mode based on the current architecture and parameters.
- **Expected behavior 3:** Mode changes should be explicitly recorded in the logs.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** 
  - Logs were shared where the mode changes occurred without RC input:
    - Log 1: https://logs.px4.io/plot_app?log=e83a1c3d-99a5-484a-b908-6eff075edc56
    - Log 2: https://logs.px4.io/plot_app?log=7ba7eefa-ed3e-4247-96c8-1a0294aea8d6
    

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Add hysteresis or a timeout for mode changes to ensure they aren't instantaneous, proposed by multiple participants in the discussion.
- **Result of the operation after the user adopted suggestion 1:** Not explicitly reported, as discussions suggested potential changes.
  
- **Suggestion 2 provided by developers or other personnel:** Add an INFO message on mode change with a reason for the change.
- **Result of the operation after the user adopted suggestion 2:** No immediate result reported.

- **Suggestion 3 provided by developers or other personnel:** Modify message logging structure to prevent relevant data from missing in case of quick mode switch glitches.
- **Result of the operation after the user adopted suggestion 3:** Developer `dagar` planned to split switches out for more reliable logging.

- **Suggestion 4 provided by developers or other personnel:** Developer `dagar` found the root cause and created a follow-up issue for tracking: #16264.
  
- **Result of the operation after the user adopted suggestion 4:** Ongoing fixes and improvements tracked in #16270.
