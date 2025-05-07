**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned
- **Software environment:** PX4 Autopilot with a commit version not mentioned; possible interaction with commit 547dd85
- **Report Time:** Dec 28, 2018
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**36248cb

**Steps for bug reproduction:**

- **Step 1:** Run `make eagle_default upload`.<font color='red'>需求 Qualcomm Snapdragon 的开发板</font>
- **Step 2:** Start `px4`.
- **Step 3:** Observe a large number of errors.

**Observed behavior by the user:**

- **Behavior after step 1:** Not explicitly mentioned
- **Behavior after step 2:** Not explicitly mentioned
- **Behavior after step 3:** The system fails at runtime due to dynamic linking issues, resulting in undefined PLT symbol errors in `/libpx4.so`.

**Expected behavior:**

- **Expected behavior 1:** The software should build and start without runtime errors.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Suspected the issue might be related to recent commits, particularly around the time functions. User referenced that the system worked before clock/sleep changes (`d1b44e5` commit).
- **URL of the flight log provided by the user:** Not provided.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `dagar` suggested the possibility of a 'fake qurt executable' to catch such linking issues at build time.
- **Result of the operation after the user adopted suggestion 1:** Not explicitly mentioned in the comments.
  
- **Suggestion 2 provided by developers or other personnel:** Developer `julianoes` indicated that missing definitions might be the issue and acknowledged not being able to reproduce the issue initially.
- **Result of the operation after the user adopted suggestion 2:** After merging updates, `julianoes` was able to reproduce the issue and provided a fix with #11115.

