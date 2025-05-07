**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned
- **Software environment:** Not explicitly mentioned
- **Report Time:** Sep 6, 2019
- **PX4 Autopilot commit version：** Not mentioned
- **last commit before the reporting time:**e450948

**Steps for bug reproduction:**

- **Step 1:** Do an auto takeoff with flow only (without ever having global frame initialized).
- **Step 2:** Start GPS in the air.
- **Step 3:** When the global position gets valid, the drone will start to fly towards some direction.

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** N/A
- **Behavior after step 3:** The drone starts to move to some direction (possibly the previous origin).

**Expected behavior:**

- **Expected behavior 1:** The drone should stay at the same location.
- **Expected behavior 2:** The origin of the local frame and the memorized positions should shift properly.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** The user plans to upload a log file soon (none mentioned at the time of report).
- **URL of the flight log provided by the user:** Not provided.

**Communication between developers or other personnel and the user:**

- No specific communication or suggestions from developers or other personnel mentioned in the document.
