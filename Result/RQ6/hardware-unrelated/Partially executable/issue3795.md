**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned
- **Software environment:** Not explicitly mentioned
- **Report Time:** Feb 18, 2016
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**eb11c91

**Steps for bug reproduction:**

- **Step 1:** Have a mission with a takeoff waypoint (30m).
- **Step 2:** In manual mode, hover the drone at some altitude (5m).
- **Step 3:** Apply full yaw.
- **Step 4:** Switch to mission mode during the yaw.

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** N/A
- **Behavior after step 3:** N/A
- **Behavior after step 4:** The drone continues yawing slowly during the mission flight, resulting in a continuous pirouette.

**Expected behavior:**

- **Expected behavior 1:** The yaw setpoint from manual control should not carry over when switching to auto (mission) mode.
- **Expected behavior 2:** The drone should follow the mission waypoints without unintended yawing.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** The user provided a detailed reproduction procedure.
- **URL of the flight log provided by the user:** [http://logs.uaventure.com/view/wqG48Vi97iHGiKfNeWWymN](http://logs.uaventure.com/view/wqG48Vi97iHGiKfNeWWymN)

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** LorenzMeier commented that the issue was fixed.
- **Result of the operation after the user adopted suggestion 1:** The issue was marked as closed, indicating successful resolution.
