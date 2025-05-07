**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned
- **Software environment:** Not explicitly mentioned
- **Report Time:** Oct 14, 2019
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**97e1edc

**Steps for bug reproduction:**

- **Step 1:** Take off FW vehicle in SITL.
- **Step 2:** Send `SET_POSITION_LOCAL_NED` setpoint with `type_mask=0x3000`.<font color='red'>mavlink传输命令失败</font>
- **Step 3:** Switch mode to offboard mode.

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** N/A
- **Behavior after step 3:** The fixed wing vehicle flies away, with roll and pitch setpoints set to zero, continuing in the last direction where offboard mode was triggered.

**Expected behavior:**

- **Expected behavior 1:** The fixed wing vehicle should circle around the loiter setpoint.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Not explicitly mentioned but discussed the nature of the issue about loiter radius and direction not being set correctly.
- **URL of the flight log provided by the user:** Not provided.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Initial thoughts by the author, Jaeyoung-Lim, indicating that loiter_radius and loiter_direction are not set properly and pointing out that the mavlink message does not contain necessary information.
- **Result of the operation after the user adopted suggestion 1:** N/A (no explicit indication of action taken following initial analysis).
