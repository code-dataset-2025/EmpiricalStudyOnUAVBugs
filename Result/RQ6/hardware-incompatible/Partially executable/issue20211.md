**Environment where the bug occurred:**

- **Hardware environment:** V6X and V5X, tested by the author "davids5" and confirmed by "AlexKlimaj"
- **Software environment:** PX4 Autopilot, specific commit version not mentioned
- **Report Time:** Sep 14, 2022
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**9245d71

**Steps for bug reproduction:**

- **Step 1:** Connect FMU V6X
- **Step 2:** Load main firmware
- **Step 3:** Set parameter 4001<font color='red'>此步骤意义不明</font>
- **Step 4:** Set parameter `RC_INPUT_PROTO` to -1
- **Step 5:** Connect any of PPM, SBUS, or DSM <font color='red'>缺少这类设备</font>
- **Step 6:** Run `px4io status`

**Observed behavior by the user:**

- **Behavior after step 6:** Slow response and 0 raw R/C inputs

**Expected behavior:**
- **Expected behavior 1:** RC input should be processed without delay

**Additional information provided by the user for bug investigation:**
- **Actions taken by the user:** In-depth tracing of the hardware bug, provided steps to reproduce the issue.
  

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** AlexKlimaj confirmed the issue and linked specific lines in the code where failures occurred.
- **Result of the operation after the user adopted suggestion 1:** No explicit result provided, but detailed explanation given about the failure points.
- **Suggestion 2 provided by developers or other personnel:** Davids5 noted a timeout on the DMA completion and mentioned tracing it to identify possible causes.
- **Result of the operation after the user adopted suggestion 2:** No explicit result provided, ongoing investigation implied.
- **Suggestion 3 provided by developers or other personnel:** AlexKlimaj found that initial operations were working in init but failing in run.
- **Result of the operation after the user adopted suggestion 3:** No explicit result provided, ongoing discussion and analysis.
