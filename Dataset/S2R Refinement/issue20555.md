**Environment where the bug occurred:**

- **Hardware environment:** Hexacopter with a takeoff mass of over 10 kg, running on an Auterion Skynode.
- **Software environment:** Auterion PX4 2.5
- **Report Time:** Nov 7, 2022
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**3e35f94

**Steps for bug reproduction:**

- **Step 1:** Power the drone and switch into manual mode.
- **Step 2:** Arm and take off in manual mode.
- **Step 3:** Switch into altitude mode.
- **Step 4:** Observe error.

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** N/A
- **Behavior after step 3:** Thrust drops out for a short moment during the transition from manual to altitude mode.
- **Behavior after step 4:** The thrust dropout causes additional load, but it quickly recovers.

**Expected behavior:**

- **Expected behavior 1:** The transition from manual to altitude mode should be smooth without thrust dropout.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Analysis identified a related anomaly in the `vehicle_local_position_setpoint` message, with acceleration setpoint commands of ~10g downwards causing lower thrust value.
- **URL of the flight log provided by the user:** Not provided, but mentioned examples of flights showing the same behavior.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `MaEtUgR` informed that the issue was resolved in a more recent version of PX4, specifically by fix #19162, and suggested contacting the company for a patched Auterion PX4 2.5 version.
- **Result of the operation after the user adopted suggestion 1:** The user acknowledged the information, expressed satisfaction that the issue was resolved in newer versions, and mentioned waiting for a company reply for a patched version.

