**Environment where the bug occurred:**

- **Hardware environment:** Pixhawk 4
- **Software environment:** PX4 Autopilot v1.13.0-beta with jmavsim
- **Report Time:** May 17, 2022
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**ff16131

**Steps for bug reproduction:**

- **Step 1:** Follow the steps to have PX4 in HITL mode.
- **Step 2:** Execute `./Tools/jmavsim_run.sh -q -s -d /dev/ttyACM0 -b 921600 -r 250`.
- **Step 3:** Observe the output messages related to sensor failures.

**Observed behavior by the user:**
- **Behavior after step 1:** Begins setup for HITL mode.
- **Behavior after step 2:** Setup occurs with several warnings related to illegal reflective access.
- **Behavior after step 3:** Preflight check fails with missing compass, accelerometer, gyroscope, and barometer. Arming is denied due to active flight termination.

**Expected behavior:**
- **Expected behavior 1:** Sensors should not be failing as simulation is through jMAVSim.
- **Expected behavior 2:** Vehicle should successfully arm for simulation.

**Additional information provided by the user for bug investigation:**
- **Actions taken by the user:** Tried with three different Pixhawk 4 units, consistently experiencing the same issue.
- **URL of the flight log provided by the user:** Not provided.

**Communication between developers or other personnel and the user:**
- **Suggestion 1 provided by developers or other personnel:** `julianoes` noted the issue with potential relation to \\\#19419, suggesting a workaround for lockdown not equating to termination in HITL.
- **Result of the operation after the user adopted suggestion 1:** Additional issues noted with refusal to take off related to flight time estimation and actuator output routing.
- **Suggestion 2 provided by developers or other personnel:** `NicolasM0` mentioned a local fix to the incorrect flight time estimation and discussed setting UAVCAN_ENABLE to 0 as a temporary fix to routing issues.
- **Result of the operation after the user adopted suggestion 2:** Acknowledgment by `julianoes` thanking `NicolasM0` for the fix.
- **Suggestion 3 provided by developers or other personnel:** `bkueng` noted that dynamic control allocation would make the UAVCAN_ENABLE setting unnecessary.
- **Result of the operation after the user adopted suggestion 3:** Commentary by developers but no user-provided results due to their ongoing discussion.
