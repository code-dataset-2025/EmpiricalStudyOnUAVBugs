**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned<font color='red'>实际需要pixhwak飞控板</font>
- **Software environment:** PX4 Autopilot
- **Report Time:** Jul 8, 2022
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**10a2b4c

**Steps for bug reproduction:**

- **Step 1:** Flash new firmware (`make px4_fmu-v5x upload`).
- **Step 2:** Set `SYS_CTRL_ALLOC` to Enabled in the Parameters Tab (without setting the airframe).
- **Step 3:** Reboot the vehicle (in the Parameters tab).
- **Step 4:** Verify that the 'Actuators' Tab is present (indicating Control Allocation is enabled).
- **Step 5:** Select an airframe and reboot.
- **Step 6:** Observe that the 'Actuators' Tab is gone.

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** N/A
- **Behavior after step 3:** N/A
- **Behavior after step 4:** 'Actuators' Tab is present, indicating Control Allocation is enabled.
- **Behavior after step 5:** N/A
- **Behavior after step 6:** 'Actuators' Tab is gone, indicating Control Allocation is disabled.

**Expected behavior:**

- **Expected behavior 1:** Selecting an airframe shouldn't disable the control allocation.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** The report describes the steps to reproduce the bug and questions the logic behind parameter changes when switching airframes.
- **URL of the flight log provided by the user:** Not provided.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `sfuhrer` questioned the logic behind the user's steps and mentioned that `SYS_CTRL_ALLOC` being only temporary and might default soon for MC.
- **Result of the operation after the user adopted suggestion 1:** N/A (Response focused on explaining user perspective and expecting the parameter to remain unchanged).
  
- **Suggestion 2 provided by developers or other personnel:** Developer `hamishwillee` provided feedback that selecting an airframe should reset defaults.
- **Result of the operation after the user adopted suggestion 2:** N/A

- **Suggestion 3 provided by developers or other personnel:** User `junwoo091400` acknowledged that the parameter is now gone and the issue is not relevant anymore.
- **Result of the operation after the user adopted suggestion 3:** N/A
