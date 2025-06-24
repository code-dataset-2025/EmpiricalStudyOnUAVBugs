**Environment where the bug occurred:**

- **Hardware environment:** CUAVx7 (with comparison using CUAVv5)
- **Software environment:** Not explicitly mentioned (related to CUAVx7 configuration)
- **Report Time:** Mar 26, 2021
- **PX4 Autopilot commit version:** a124426

**Steps for bug reproduction:**

- **Step 1:** Use firmware version a124426.
- **Step 2:** Set the model to 4001.
- **Step 3:** Calibrate all sensors.
- **Step 4:** Apply certain parameter settings (not fully detailed).
- **Step 5:** Restart the system.
- **Step 6:** Connect to the remote control.

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** N/A
- **Behavior after step 3:** N/A
- **Behavior after step 4:** N/A
- **Behavior after step 5:** PWM output was present from AUX interface but not from MAIN interface.
- **Behavior after step 6:** No output from the MAIN channel.

**Expected behavior:**

- **Expected behavior 1:** The CUAVx7 MAIN channel should produce PWM output.
- **Expected behavior 2:** Consistent PWM outputs after system restart and remote connection.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Compared outputs between CAUVx7 and CUAVv5.
- **URL of the flight log provided by the user:** Not provided.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `dagar` acknowledged the potential regression issue.
- **Result of the operation after the user adopted suggestion 1:** N/A (acknowledgment did not contain specific action steps or solutions).
