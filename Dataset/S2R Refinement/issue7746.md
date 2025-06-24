**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned
- **Software environment:** PX4 Autopilot
- **Report Time:** Aug 7, 2017
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**453937a

**Steps for bug reproduction:**

- **Step 1:** Observe mag timeouts during drone operations.
- **Step 2:** Notice mag timeouts coinciding with the land detector state changes.
- **Step 3:** Flash the firmware to a stable version to see if the issue persists.

**Observed behavior by the user:**

- **Behavior after step 1:** Intermittent mag timeouts occur.
- **Behavior after step 2:** Timeouts coincide with "maybe landed" state changes.
- **Behavior after step 3:** The timeout issue disappears when using a stable firmware version.

**Expected behavior:**

- **Expected behavior 1:** Consistent magnetometer operation without timeouts.
- **Expected behavior 2:** Land detector and other systems should not interfere with magnetometer operations.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** User flashed the stable firmware to compare behavior and provided detailed observations related to throttle and CPU usage.
- **URL of the flight log provided by the user:** [Bench test flight log](https://logs.px4.io/plot_app?log=7308ecce-8078-4c20-a458-d8461a9fe6e5)

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `dagar` suggested checking the high-priority work queue and stopping certain processes to understand CPU usage.
- **Result of the operation after the user adopted suggestion 1:** N/A (It's not clear from the document whether these were explicitly tested beyond initial checks).
- **Suggestion 2 provided by developers or other personnel:** Developer `bkueng` suggested changing the land detector task priority and rebuilding.
- **Result of the operation after the user adopted suggestion 2:** No change observed with priority set to 253.
- **Additional observations by the user:** The issue primarily occurred in VTOL mode during fixed-wing operations and was related to land detector logic not functioning correctly. They attempted to modify the code to restrict certain checks to rotary-wing mode only.
- **Conclusion:** User found a fix, though specific details are not provided in the document.
