需求：step2 LL40LS（LiDAR-Lite激光雷达的一个型号）

**Environment where the bug occurred:**

- **Hardware environment:** Pixhawk4
- **Software environment:** Not explicitly mentioned
- **Report time:** Oct 27, 2019
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**380cae1

**Steps for bug reproduction:**

- **Step 1:** Flash master.
- **Step 2:** Connect LL40LS to i2c.<font color='red'>需求LL40LS激光雷达</font>
- **Step 3:** Set SENS_EN_LL40LS Enabled.
- **Step 4:** See console output (via console cable).

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** N/A
- **Behavior after step 3:** N/A
- **Behavior after step 4:** Command line interface stops working, and nsh command does not work.

**Expected behavior:**

- **Expected behavior 1:** When typing a command on nsh, the command should work.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Attached log files and screenshots.
- **URL of the flight log provided by the user:** Not provided.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `dagar` inquired if `mcsauder` had successfully used LL40LS on i2c recently.
- **Result of the operation after the user adopted suggestion 1:** N/A
- **Suggestion 2 provided by developers or other personnel:** Developer `dagar` asked `hyonlim` to provide the full boot output.
- **Result of the operation after the user adopted suggestion 2:** N/A
- **Suggestion 3 provided by developers or other personnel:** Developer `dagar` suggested increasing `CONFIG_MAX_TASKS` might solve the issue.
- **Result of the operation after the user adopted suggestion 3:** The bug was resolved by a subsequent fix, #13285.
