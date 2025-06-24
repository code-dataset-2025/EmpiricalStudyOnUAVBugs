**Environment where the bug occurred:**

- **Hardware environment:** FMUv1
- **Software environment:** Not explicitly mentioned
- **Report Time:** Oct 29, 2013
- **PX4 Autopilot commit version:** Commit 6d17af3

**Steps for bug reproduction:**

- **Step 1:** Use commit 6d17af3 to compile the PX4 Autopilot.
- **Step 2:** Run the `px4_simple_app` which prints some values and then returns instead of entering an infinite loop.

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** The FMU sometimes crashes when the app returns after printing values.

**Expected behavior:**

- **Expected behavior 1:** The application should be able to print values and return without causing a crash.
  

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Reproduced the issue and provided a backtrace from GDB during the crash.
- **URL of the flight log provided by the user:** Not provided.
  

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `LorenzMeier` asked on which hardware version the crash was reproduced.
- **Result of the operation after the user adopted suggestion 1:** User `julianoes` confirmed that the issue was on FMUv1.
- **Suggestion 2 provided by developers or other personnel:** Developer `LorenzMeier` mentioned that the issue was fixed in PR #509.
- **Result of the operation after the user adopted suggestion 2:** Implicitly resolved as the issue status was marked as "Closed".
