**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned
- **Software environment:** PX4 Autopilot v1.10
- **Report Time:** Jan 16, 2020
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**9647bc3

**Steps for bug reproduction:**

- **Step 1:** Send the drone on an auto mission with the sequence: change speed cmd -> set roi cmd -> takeoff -> waypoint -> waypoint...<font color='red'>无法先设置速度再起飞，将设置速度调到第三步，执行结束没有出现Bug</font>

**Observed behavior by the user:**

- **Behavior after step 1:** Instead of taking off 4-5m above ground, the drone lifts slightly above ground and hovers there. In some cases, the message "position control setpoint update failed" is observed. 

**Expected behavior:**

- **Expected behavior 1:** Normal takeoff to 5m above ground.
- **Expected behavior 2:** Completion of the planned mission with subsequent waypoints.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** User observed the issue occurs less than once in 30 flights. Noted that the triplet type switches quickly from takeoff(3) to position(0). Also mentioned the "position control setpoint update failed" error at mission start.
- **URL of the flight log provided by the user:** Not directly provided, implied potential future sharing.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `bresch` suggested that there might be an issue with the home position setting affecting altitude calculations.
  
- **Result of the operation after the user adopted suggestion 1:** User `dusan19` argued that the home position was not the issue as the altitude difference should normally command an upward velocity.

- **Suggestion 2 provided by developers or other personnel:** Developer `LorenzMeier` suggested improving home position setting based on GPS accuracy and considering a relative command in QGC.

- **Result of the operation after the user adopted suggestion 2:** N/A (no explicit mention of user adopting this suggestion).

- **Suggestion 3 provided by developers or other personnel:** Developer `MaEtUgR` explained a different issue to `NAmmann` related to autonomy being overridden by joystick movement.

- **Result of the operation after the user adopted suggestion 3:** `NAmmann` was advised to disable the RC override feature if the problem persisted, implying the issue was different from the original report.

- **Suggestion 4 provided by developers or other personnel:** `MaEtUgR` mentioned a possible relation to issue #13751 to `bresch`.

- **Result of the operation after the user adopted suggestion 4:** N/A (no specific follow-up).

This structured information helps capture the essence of the reported issue, its context, and the ongoing dialogue within the developer community to address it.
