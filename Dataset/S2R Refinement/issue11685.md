**Environment where the bug occurred:**

- **Hardware environment:** Generic quadrotor
- **Software environment:** PX4 Autopilot with Firmware version: stable v1.8.2
- **Report Time:** Mar 20, 2019
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**a08b168

**Steps for bug reproduction:**

- **Step 1:** Switch drone into 'ARMING' State using Safety switch button.
- **Step 2:** In QGroundControl (QGC) go to Params->Tools->Reboot.
- **Step 3:** Wait until the controller starts to boot.
  

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** N/A
- **Behavior after step 3:** Propellers will turn for a small period of time (corresponds to ~30 degrees).

**Expected behavior:**

- **Expected behavior 1:** The propellers should not spin at all during the reboot process.
- **Expected behavior 2:** The copter should disarm either during the execution of the reboot command or during booting.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Reported the issue and tested with the latest master branch version.
- **URL of the flight log provided by the user:** Not provided.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `dagar` asked the user to try again with the recent master branch to see if the issue persists.
- **Result of the operation after the user adopted suggestion 1:** User `fpvaspassion` confirmed that with the latest master, there was no spinning at all on reboot.
