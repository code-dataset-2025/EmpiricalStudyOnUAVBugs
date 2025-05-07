**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned
- **Software environment:** Not explicitly mentioned, related to PX4/NuttX
- **Report Time:** Oct 3, 2019
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**f885d22

**Steps for bug reproduction:**

- **Step 1:** Start logging (use 'logger on' for example).
- **Step 2:** Remove the SD card.<font color='red'>需要实机记录日志和SD卡</font>

**Observed behavior by the user:**

- **Behavior after step 1:** Logging starts.
- **Behavior after step 2:** Most of the time, the mavlink thread stops, and you can see that using 'top' where mavlink is at 0%.

**Expected behavior:**

- **Expected behavior 1:** The SD card status check should handle SD removal gracefully without causing mavlink or other modules to stop.
- **Expected behavior 2:** Operations requiring SD access, like reading missions, should either continue with an alternate mechanism or fail safely without blocking.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Added a mavlink message to check SD card status periodically and tested by removing the SD card during operation.
- **URL of the flight log provided by the user:** [Testing code](https://github.com/BazookaJoe1900/Firmware/tree/testing-sd_removal)

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** `dagar` considers it a problem and suggests handling the failure gracefully in dataman.
- **Result of the operation after the user adopted suggestion 1:** Not explicitly mentioned (requires deeper investigation).

- **Suggestion 2 provided by developers or other personnel:** `davids5` suggested a timeout mechanism and mentioned investigating after Oct 16th.
- **Result of the operation after the user adopted suggestion 2:** Not explicitly mentioned (pending investigation).

- **Additional communication:** Various discussions about the deeper OS-level issue and possible blocking due to semaphore handling without timeout.

