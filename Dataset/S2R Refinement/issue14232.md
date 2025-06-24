**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned
- **Software environment:** PX4 Autopilot
- **Report Time:** Feb 25, 2020
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**5bf2648

**Steps for bug reproduction:**

- **Step 1:** Collect a replay logfile with two GPS modules connected.<font color='red'>实际需要2个GPS设备</font>
- **Step 2:** During replay, force one GPS module to lose fix.

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** The position offset is still applied to the GPS data despite one GPS module losing fix.

**Expected behavior:**

- **Expected behavior 1:** The GPS data should converge to the GPS module still working if the other loses fix.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** A horizontal position offset is added to one GPS module to illustrate the issue more easily.
- **URL of the flight log provided by the user:** Not provided.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Comment by `julianoes` asking if this issue is related to another known issue.
- **Result of the operation after the user adopted suggestion 1:** Comment by `DanielePettenuzzo` stating uncertainty if they are related.
- **Suggestion 2 provided by developers or other personnel:** Not explicitly mentioned, but the issue was eventually solved by pull request \#14278.
- **Result of the operation after the user adopted suggestion 2:** Issue closed after resolution via pull request \#14278.
