**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned
- **Software environment:** PX4 Autopilot
- **Report Time:** Jun 24, 2020
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**620916e

**Steps for bug reproduction:**

- **Step 1:** Execute `make px4_sitl gazebo_r1_rover`.
- **Step 2:** Start a mission.
- **Step 3:** Trigger a GPS failure.

**Observed behavior by the user:**
- **Behavior after step 1:** N/A
- **Behavior after step 2:** N/A
- **Behavior after step 3:** The differential rover goes into a fixed bank loiter, resulting in the vehicle spinning around while stationary.

**Expected behavior:**
- **Expected behavior 1:** The rover possibly should keep stationary when GPS is lost.

**Additional information provided by the user for bug investigation:**
- **Actions taken by the user:** The user realized this issue was a duplicate of #13467.
- **URL of the flight log provided by the user:** Not provided.

**Communication between developers or other personnel and the user:**
- **Suggestion 1 provided by developers or other personnel:** Quick fixes suggested by `dagar` include hacking navigator/gpsfailure for rover and handling it in the state machine with a link to relevant code.
- **Result of the operation after the user adopted suggestion 1:** Not explicitly mentioned; the user realized it was a duplicate issue.

- **Suggestion 2 provided by developers or other personnel:** `aaryanmurgunde` asked if a solution was found and provided a simulation setup concern which was clarified by `Jaeyoung-Lim`.
- **Result of the operation after the user adopted suggestion 2:** The user understood the behavior was independent of the simulation setup being used.

- **Suggestion 3 provided by developers or other personnel:** `sajisaka` asked for an update, showing empathy for the issue.
- **Result of the operation after the user adopted suggestion 3:** `Jaeyoung-Lim` responded that if GPS captures position when spinning occurs, it is not the same issue.
