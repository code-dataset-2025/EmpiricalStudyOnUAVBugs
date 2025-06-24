**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned
- **Software environment:** PX4 Autopilot with commit version v1.7.3-296-g26f9e56
- **Report Time:** Feb 5, 2018
- **PX4 Autopilot commit version:** v1.7.3-296-g26f9e56

**Steps for bug reproduction:**

- **Step 1:** Try to build PX4 without having the ARM compiler installed.<font color='red'>删除ARM COMPILER之后仍然编译成功</font>
- **Step 2:** Install the ARM compiler.
- **Step 3:** Try to build PX4 again without executing 'make distclean'.<font color='red'>这一步无错误发生</font>

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** N/A
- **Behavior after step 3:** An ImportError occurs stating "No module named uavcan", and the build process fails.

**Expected behavior:**

- **Expected behavior 1:** PX4 should build successfully without errors after installing the ARM compiler, even without a 'make distclean'.
- **Expected behavior 2:** All necessary dependencies, including UAVCAN, should be resolved correctly.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** The user attempted to build the software and identified steps to reproduce the error.
- **URL of the flight log provided by the user:** Not provided.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `dagar` suggested that a few dependencies at the UAVCAN level might be missing.
- **Result of the operation after the user adopted suggestion 1:** N/A (No specific resolution reported as the issue was acknowledged and the suggestion was about identifying missing dependencies).
