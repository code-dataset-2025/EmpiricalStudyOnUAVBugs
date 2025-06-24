**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned
- **Software environment:** PX4 Autopilot, simulated environment using Software In The Loop (SITL)
- **Report Time:** Sep 21, 2019
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**fe4f6c1

**Steps for bug reproduction:**

- **Step 1:** Execute `make px4_sitl jmavsim`.<font color='red'>jmavsim不显示gui，能与QGC连接但无法取得GPS等参数</font>

**Observed behavior by the user:**

- **Behavior after step 1:** An error message is displayed: `ERROR [mavlink] system boot did not complete in 20 seconds`.

**Expected behavior:**

- **Expected behavior 1:** The error message should not appear, indicating the system boot should complete within the expected timeframe.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** User reports the error with output logs to identify the issue and questions if the problem has been introduced recently.
- **URL of the flight log provided by the user:** Not provided.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Dagar confirmed that the behavior was likely introduced in a recent change and noted that the 20-second timeout is arbitrary. It serves as a fallback if the system does not hit the mavlink `boot_complete` for some reason.
- **Result of the operation after the user adopted suggestion 1:** N/A (further actions not outlined in the communication).
