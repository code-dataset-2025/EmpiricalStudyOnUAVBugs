**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned
- **Software environment:** QGroundControl (QGC) with PX4 Autopilot
- **Report Time:** Dec 3, 2018
- **PX4 Autopilot commit version:** commit 161cf7f

**Steps for bug reproduction:**

- **Step 1:** Flash Pixhawk 4 with Firmware (any commit later than 161cf7f).<font color='red'>这里提到该提交后任一版本，同时由于编译问题改用之后距离最近的release</font>
- **Step 2:** Open QGC and try to search for a parameter MPC_...<font color='red'>此时MPC等参数仍然存在</font>

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** QGC does not see most of the parameters.

**Expected behavior:**

- **Expected behavior 1:** The user should be able to see and modify parameters over QGC.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** The user utilized `git bisect` to determine the responsible commit, identifying it as commit 161cf7f.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `dagar` suggested that the multicopter controllers might not be starting and mentioned looking into the issue.
- **Result of the operation after the user adopted suggestion 1:** N/A (The comment was an observation and step to debug rather than a direct suggestion for the user to follow).

- **Suggestion 2 provided by developers or other personnel:** Developer `dagar` identified that the last commit to accommodate shellcheck led to issues with nsh (Nuttx).
- **Result of the operation after the user adopted suggestion 2:** N/A (The comment was a developer's finding rather than actionable for the user).
