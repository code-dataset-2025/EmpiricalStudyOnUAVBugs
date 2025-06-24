# Extracted Information for PX4 Autopilot Bug Report:

**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned
- **Software environment:** Not explicitly mentioned
- **Report Time:** Aug 5, 2019
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**f21dc82

---

**Steps for bug reproduction:**

- **Step 1:** Set `MIS_YAW_TMT` to a value other than `0` (e.g., `MIS_YAW_TMT = 1`).
- **Step 2:** Plan a mission with a separate VTOL transition (not a VTOL takeoff, as heading is not enforced during takeoff).
- **Step 3:** Simulate in SITL where the vehicle needs to turn a significant angle (e.g., 90°) within the time set in `MIS_YAW_TMT`.

---

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** N/A
- **Behavior after step 3:** The mission does not abort even when the vehicle fails to align with the yaw setpoint within the `MIS_YAW_TMT` duration.<font color='red'>与之不同，飞机停止了执行任务</font>

---

**Expected behavior:**

- **Expected behavior 1:** Abort the mission when the vehicle cannot align with the yaw setpoint at the transition point within the time set in `MIS_YAW_TMT`.

---

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** The user investigated the source of the problem and noted that the counter responsible for measuring the yawing time at the transition waypoint resets continuously. This occurs because `_waypoint_position_reached` is reset to `false` after every execution of `is_mission_item_reached()` in `mission_block.cpp`. This issue seems to have been introduced in commit `#4992`.
- **URL of the flight log provided by the user:** Not provided.

---

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Not explicitly mentioned, but the issue was later fixed in commit `#12630`.
- **Result of the operation after the user adopted suggestion 1:** The issue was resolved in commit `#12630`.

---

Let me know if you'd like further details or additional formatting!
