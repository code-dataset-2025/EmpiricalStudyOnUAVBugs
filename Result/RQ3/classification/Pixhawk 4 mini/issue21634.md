**Environment where the bug occurred:**

- **Hardware environment:** Pixhawk 4 mini
- **Software environment:** PX4 Autopilot (commit version not mentioned)
- **Report Time:** May 24, 2023
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**822d784

**Steps for bug reproduction:**

- **Step 1:** Press the PWM calibration button or call the corresponding command in the shell.
- **Step 2:** The PWM outputs go high immediately after pressing the calibration button, even with the battery connected.
- **Step 3:** Try to complete the procedure without having an auto-detected battery.
- **Step 4:** Upon ESC calibration timeout, observe the PWM output stays on a high value until rebooting PX4.
- **Step 5:** Check that the highest and lowest value of the PWM calibration corresponds to the configured minimum and maximum PWM value used in flight.
- **Step 6:** Connect the battery and observe that it is not recognized despite having a power module.

**Observed behavior by the user:**

- **Behavior after step 1:** PWM outputs go high immediately with no way to abort; props could be dangerous if attached.
- **Behavior after step 2:** Unable to complete the procedure without an auto-detected battery.
- **Behavior after step 3:** PWM output stays high until PX4 is rebooted.
- **Behavior after step 4:** Calibration uses inconsistent PWM limits of 1000 and 2000us.
- **Behavior after step 5:** Battery connection is not detected, showing zero "valid bricks."

**Expected behavior:**

- **Expected behavior 1:** PWM calibration should allow for aborting the process.
- **Expected behavior 2:** Procedure should not require an auto-detected battery.
- **Expected behavior 3:** Upon ESC calibration timeout, PWM output should return to normal.
- **Expected behavior 4:** Calibration should use consistent PWM limits of 1000 to 2000us.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Tested on Pixhawk 4 mini and identified the battery measurement being seen as present but not connected; added a safety check to abort calibration if current consumption rises.
- **URL of the flight log provided by the user:** Not provided.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Mention made of testing with Oneshot and fixing the PWM range for consistent calibration.
- **Result of the operation after the user adopted suggestion 1:** Mitigation step added to abort calibration based on current measurement, several issues resolved in subsequent PR (#21711).
- **Suggestion 2 provided by developers or other personnel:** Acknowledge unresolved issue with specific board and setup, but considered not a release blocker.
- **Result of the operation after the user adopted suggestion 2:** Continued effort to improve process with UI changes and more reliable battery detection.
**Environment where the bug occurred:**

- **Hardware environment:** Pixhawk 4 mini
- **Software environment:** Not explicitly mentioned
- **Report Time:** May 24, 2023
- **PX4 Autopilot commit version:** Not mentioned

**Steps for bug reproduction:**

- **Step 1:** Test PWM calibration on a Pixhawk 4 mini.
- **Step 2:** Press the PWM calibration button with the battery connected.

**Observed behavior by the user:**
- **Behavior after step 1:** PWM outputs go high immediately after pressing the calibration button, making it dangerous if props are on.
- **Behavior after step 2:** The procedure cannot complete without an auto-detected battery. Upon ESC calibration timeout, the PWM output stays high until PX4 is rebooted.

**Expected behavior:**

- **Expected behavior 1:** Press PWM calibration button or call the corresponding command in shell.
- **Expected behavior 2:** Warning to remove props and instructions to unplug battery (option to abort accessible).
- **Expected behavior 3:** After user confirmation, output exactly 2000us PWM for all motors only.
- **Expected behavior 4:** Instructions for the user to plug in the battery/power ESCs (option to continue immediately accessible).
- **Expected behavior 5:** After user confirmation, output exactly 1000us PWM for all motors.
- **Expected behavior 6:** Wait for 4 seconds.
- **Expected behavior 7:** Return to configured disarmed PWM output.
- **Expected behavior 8:** Inform user about the completed process.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** User tested PWM calibration with Pixhawk 4 mini and found various issues. Mentioned specific functions in the code where the issue might lie.
- **Specific hardware issue:** An issue with the Pixhawk 4 mini ADC not recognizing the battery despite a correct voltage reading.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** None explicitly mentioned.
- **Result of the operation after the user adopted suggestion 1:** Not applicable (no explicit suggestions were provided in the comments).
- **Additional observations by the report author:** The issue seems board-specific, possibly related to the Pixhawk 4 mini setup rather than a broader problem in the software.
