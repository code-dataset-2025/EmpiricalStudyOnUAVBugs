**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned
- **Software environment:** PX4 Autopilot
- **Report Time:** Feb 13, 2020
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**abd2bb4

**Steps for bug reproduction:**

- **Step 1:** Drone switched on
- **Step 2:** Create at least one log file on the SD card
- **Step 3:** List the logs in QGC repeatedly
- **Step 4:** Eventually, the list will be empty
- **Step 5:** Reboot via QGC
- **Step 6:** Log listing will be successful again

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** N/A
- **Behavior after step 3:** Logs are listed initially
- **Behavior after step 4:** The list of logs becomes empty unexpectedly
- **Behavior after step 5:** N/A
- **Behavior after step 6:** Logs are listed successfully

**Expected behavior:**

- **Expected behavior 1:** Logs should be listed correctly when requested
- **Expected behavior 2:** Rebooting should not be necessary for log retrieval

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** The user investigated the issue by duplicating a sequence that led to the bug, identifying it occurred after a series of log manipulations.
- **Errno encountered:** "File table overflow" was observed as the error at a specific point in the log handling code.
- **Specific line of code where failure occurs:** 
  - Listing logs: https://github.com/PX4/Firmware/blob/07d656e971a72d1202651dfd3b4642736fb078d7/src/modules/mavlink/mavlink_log_handler.cpp#L464
  - Downloading logs: https://github.com/PX4/Firmware/blob/07d656e971a72d1202651dfd3b4642736fb078d7/src/modules/mavlink/mavlink_log_handler.cpp#L366

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `julianoes` checked for missing file closures in the code but found nothing wrong initially.
- **Result of the operation after the user adopted suggestion 1:** User `ndepal` continued investigation and found the sequence causing the issue.
- **Suggestion 2 provided by developers or other personnel:** Developer `julianoes` attempted to debug by wrapping file open and close functions.
- **Result of the operation after the user adopted suggestion 2:** Patch applied for debugging to track file handling, resulting in the discovery of file descriptor (FD) leakage.
- **Suggestion 3 provided by developers or other personnel:** Developer `bkueng` identified an FD leak which was fixed by a subsequent commit (#14188).
