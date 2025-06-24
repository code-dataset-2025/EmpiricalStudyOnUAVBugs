**Environment where the bug occurred:**

- **Hardware environment:** Cube Blue, Standard carrier board
- **Software environment:** PX4 Autopilot version 1.13.0, QGroundControl
- **Report Time:** Jun 23, 2022
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**ffb0097

**Steps for bug reproduction:**

- **Step 1:** Flash the newest firmware (1.13.0).
- **Step 2:** Open QGroundControl (QGC).
- **Step 3:** Click on analyze tools.
- **Step 4:** Click console and hit enter.

**Observed behavior by the user:**
- **Behavior after step 1:** N/A
- **Behavior after step 2:** N/A
- **Behavior after step 3:** N/A
- **Behavior after step 4:** No response is observed; the `nsh>` prompt does not appear.<font color='red'>操作完4步有nsh></font>

**Expected behavior:**
- **Expected behavior 1:** The `nsh>` prompt should appear in the console.

**Additional information provided by the user for bug investigation:**
- **Actions taken by the user:** Investigation by adding `mavlink start -d /dev/ttyACM0` to `rc.board_mavlink`, exploring hardware configurations, and observing behavior across different connections (serial vs. USB).
- **Other observations:** The issue seems to persist only with USB connections, not with serial radios.

**Communication between developers or other personnel and the user:**
- **Suggestion 1 provided by developers or other personnel:** Comment user `ecmnet` suggested adding `mavlink start -d /dev/ttyACM0` to `rc.board_mavlink`.
- **Result of the operation after the user adopted suggestion 1:** Initially, the issue seemed resolved, but persistence was noted after further testing and with the integration of a specific app.
- **Suggestion 2 provided by developers or other personnel:** Comment user `lefamz` suggested creating an `extras.txt` file containing the command on the SD card.
- **Result of the operation after the user adopted suggestion 2:** The workaround resolved the issue for some users, but was conditional depending on specific hardware boot sequences and setups.
- **Further interactions:** The issue was investigated further by multiple users who identified additional related platform and connection issues (USB vs. telem). Various troubleshooting and alternative setups such as changing QGroundControl versions were tested.

