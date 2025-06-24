**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned
- **Software environment:** PX4 Autopilot
- **Report Time:** Jun 5, 2020
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**626895e

**Steps for bug reproduction:**

- **Step 1:** Use the master branch to fly (tailsitter VTOL).
- **Step 2:** In altitude mode, attempt transmission from multicopter (mc) to fixed-wing (fw).

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** The drone's pitch angle does not change, and there is no tilt acceleration when attempting to switch from mc to fw.

**Expected behavior:**

- **Expected behavior 1:** The VTOL should enter the transmission state correctly whenever a switch is used.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** The user suspects numerical calculation issues under certain extreme conditions (e.g., actual/setpoint angle of pitch both being 0) and has planned investigations to identify the problem source.
- **URL of the flight log provided by the user:** [Flight log](https://logs.px4.io/plot_app?log=4df87c34-da2f-46be-b612-ddcc13b135c8)

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `sfuhrer` acknowledged the issue, indicated understanding of the problem, and expressed intention to investigate it further.
- **Result of the operation after the user adopted suggestion 1:** N/A (developer is yet to investigate).
- **Suggestion 2 provided by developers or other personnel:** N/A
- **Result of the operation after the user adopted suggestion 2:** Fix implemented in \#15352 as referred to by user `xdwgood` in a follow-up comment.
