**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned
- **Software environment:** Not explicitly mentioned
- **Report Time:** Jan 22, 2020
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**009ba63

**Steps for bug reproduction:**

- **Step 1:** Create a simple mission with a landing waypoint at the end.
- **Step 2:** Run the mission and wait until the drone has landed and disarmed.

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** After the mission ends and the drone is disarmed, QGroundControl (QGC) displays the message "Takeoff to x meters above home."

**Expected behavior:**

- **Expected behavior 1:** No message indicating a takeoff should be displayed after a mission has ended with a landing waypoint.
- **Expected behavior 2:** The system should switch to a land mode similar to what occurs in Return-To-Launch (RTL) mode, without resetting mission items immediately.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Identified the issue was due to the mission resetting after disarming and suggested deferring the setting of mission items until re-arming, although noted potential issues with mc_pos_control going into failsafe.
- **URL of the flight log provided by the user:** Not provided.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `dagar` asked for input from `RomanBapst`, who had recently reviewed similar logic.
- **Result of the operation after the user adopted suggestion 1:** N/A (as it was a query for further input rather than an actionable suggestion).
