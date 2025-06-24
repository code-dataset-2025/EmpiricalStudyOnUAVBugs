Here is the formatted output for the provided bug report:

---

**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned
- **Software environment:** Not explicitly mentioned
- **Report Time:** Feb 27, 2020
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**d7e502e

**Steps for bug reproduction:**

- **Step 1:** Connect two GPS modules to the system.<font color='red'>实际需要2个GPS设备</font>
- **Step 2:** At `t=80s`, introduce a position offset to `gps0` (blue line).
- **Step 3:** Observe the internal GPS blended state (red line) and the output of the blending algorithm (green line).

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** N/A
- **Behavior after step 3:** The blending algorithm produces a faulty output, with the offset between the output signal and the internal blended GPS state not decreasing monotonically as expected.

**Expected behavior:**

- **Expected behavior 1:** The offset between the output signal and the internal blended GPS state should decrease monotonically.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Provided a replay log showing the behavior of the system with the two GPS modules and added a position offset to one GPS module.
- **URL of the flight log provided by the user:** Not explicitly mentioned.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `bresch` tagged `DanielePettenuzzo` for attention.
  - **Result of the operation after the user adopted suggestion 1:** N/A (no immediate action taken by the user).
- **Suggestion 2 provided by developers or other personnel:** The issue was resolved by merging PR `#14278` as mentioned by the user (`CarlOlsson`) on Mar 10, 2020.
  - **Result of the operation after the user adopted suggestion 2:** The issue was resolved and the report was closed.

---
