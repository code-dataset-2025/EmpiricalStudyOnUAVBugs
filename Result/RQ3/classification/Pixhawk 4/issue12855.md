**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned
- **Software environment:** PX4 Autopilot
- **Report Time:** Aug 31, 2019
- **PX4 Autopilot commit version:** 78ef8aab2df33cd00e2c969bbff37ffd82bcf385

**Steps for bug reproduction:**

- **Step 1:** Enable nsh (this can be done on one of the telemetry ports).<font color='red'>nsh实际需要在飞控板上操作</font>
- **Step 2:** Look at the output for any warning messages.

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** A warning message is displayed: "WARN  [mpu6000] unexpected ID 0xfd accepted".<font color='red'>选用距离最近的release并刷入飞控后nsh中没有出现该警报信息</font>

**Expected behavior:**

- **Expected behavior 1:** The driver should correctly identify the device ID without any warnings.
- **Expected behavior 2:** If a new device version is detected, it should be properly acknowledged without unnecessary warnings.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** The user attempted to find register information from the TDK datasheet without success.
- **URL of the flight log provided by the user:** Not provided.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `davids5` mentioned that the warning indicates a new IC version has arrived and suggested it is only a warning with no effect.
- **Result of the operation after the user adopted suggestion 1:** User continued to question the relevance and impact of the warning.
  
- **Suggestion 2 provided by developers or other personnel:** No further direct suggestions were provided, but there was some discussion about possibly removing the warning message or adjusting it to reflect the unknown status of the 0xfd ID.
- **Result of the operation after the user adopted suggestion 2:** The issue was eventually marked as a "dead end" by the user, indicating no satisfactory resolution was reached.
