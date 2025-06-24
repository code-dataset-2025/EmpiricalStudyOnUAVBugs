**Environment where the bug occurred:**

- **Hardware environment:** Pixhawk Cube (FMUv3)
- **Software environment:** PX4 Autopilot
- **Report Time:** Sep 9, 2019
- **PX4 Autopilot commit version:** commit 47e668e

**Steps for bug reproduction:**

- **Step 1:** Use the current Master branch (47e668e).
- **Step 2:** Set system parameter `SYS_AUTOCONFIG` to 13012.
- **Step 3:** Reboot the system.

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** N/A
- **Behavior after step 3:** Boot hangs at mixer loading, unable to reach nsh console, and console hangs.

**Expected behavior:**

- **Expected behavior 1:** The system should successfully boot up without hanging.
- **Expected behavior 2:** User should be able to reach the nsh console during boot.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** User provided log files and detailed boot information.
- **URL of the flight log provided by the user:** None provided.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `julianoes` asked `davids5` if he had insights into the issue.
- **Result of the operation after the user adopted suggestion 1:** N/A (the suggestion did not contain a specific action for the user).
- **Suggestion 2 provided by developers or other personnel:** Developer `sfuhrer` asked if the issue was still valid.
- **Result of the operation after the user adopted suggestion 2:** User `dlwalter` agreed to close the issue due to an inability to test for a few days.
