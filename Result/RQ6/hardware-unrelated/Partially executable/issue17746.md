**Environment where the bug occurred:**

- **Hardware environment:** Tailsitter
- **Software environment:** PX4 Autopilot Firmware Version 1.11.3
- **Report Time:** Jun 10, 2021
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**8c4b900

**Steps for bug reproduction:**

- **Step 1:** Set `MIS_YAW_TMT` to a value lower than the time to turn 180 degrees in FW flight. In this case, `MIS_YAW_TMT` was set to 1.
- **Step 2:** Fly a mission with several altitude loiters.

**Observed behavior by the user:**

- **Behavior after completing the mission:** The RTL is triggered in FW flight because the timeout for heading in MC triggers, resulting in the following messages:
  - `[navigator] unable to reach heading within timeout`
  - `[commander] Mission cannot be completed`

**Expected behavior:**

- **Expected behavior 1:** Ignore the timeout since it is a FW flight.
- **Expected behavior 2:** Improve the description of `MIS_YAW_TMT` in the parameter reference to clarify what a value of 0 does.
- **Expected behavior 3:** An option to ignore the transition heading in a mission for VTOLs through a parameter would be beneficial.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** The user linked to the part of the code where the error seems to be triggered: [Code Link](https://github.com/PX4/PX4-Autopilot/blob/release/1.11/src/modules/navigator/mission_block.cpp#L398).
- **URL of the flight log provided by the user:** [Flight Log](https://logs.px4.io/plot_app?log=92979fd1-0fc9-44f9-9a14-2c80e6ed66d3).

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Comment by `ryanjAA` asking if the issue is still relevant.
- **Result of the operation after the user adopted suggestion 1:** Not applicable, as no action was required from the user.
- **Suggestion 2 provided by developers or other personnel:** Comment by `sfuhrer` noted inability to reproduce the bug, indicating it has likely been fixed.
- **Result of the operation after the user adopted suggestion 2:** Not specifically mentioned, but follows that the issue was likely resolved in subsequent updates to the software.
- **Further communication:** `ryanjAA` acknowledged `sfuhrer's` feedback with a positive response, thanking them.
