**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned
- **Software environment:** Not explicitly mentioned
- **Report Time:** Sep 2, 2019
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**7162000

**Steps for bug reproduction:**

- **Step 1:** Flip transition switch to Fixed Wing (FW) mode.<font color='red'>这里的flip transition switch 应当是实机上的按钮</font>
- **Step 2:** Flip transition switch back to Multi-Copter (MC) mode.
- **Step 3:** Flip kill switch.

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** N/A
- **Behavior after step 3:** The MC motors are correctly switched off, but the FW pusher motor continues spinning, even after disarming.

**Expected behavior:**

- **Expected behavior 1:** Both MC motors and FW pusher motor should be switched off when the kill switch is activated, regardless of transition states.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** None explicitly mentioned.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `dagar` mentioned that the issue was likely fixed by commit #12838.
- **Result of the operation after the user adopted suggestion 1:** User `sfuhrer` confirmed that the issue was fixed with #12838 and expressed gratitude.
