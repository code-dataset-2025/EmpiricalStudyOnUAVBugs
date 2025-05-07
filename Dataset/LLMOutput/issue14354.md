**Environment where the bug occurred:**

- **Hardware environment:** Control Zero with USB cable, SDCard inserted
- **Software environment:** PX4 Autopilot
- **Report Time:** Mar 10, 2020
- **PX4 Autopilot commit version:** e0f016c2b3db160284bbaaadaf70bef84592d81e

**Steps for bug reproduction:**

- **Step 1:** Loaded stable/mro_ctrl-zero-f7_default.px4 and board boots up fine.
- **Step 2:** Connect via QGroundControl (QGC).
- **Step 3:** Set frame type to generic quad and reboot.

**Observed behavior by the user:**

- **Behavior after step 1:** Board boots up fine.
- **Behavior after step 2:** N/A
- **Behavior after step 3:** Board locks up in the middle of playing the startup tone.

**Expected behavior:**

- **Expected behavior 1:** The board should complete the startup sequence without locking up.
- **Expected behavior 2:** The board should be fully operational after setting the frame type and rebooting.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** User noticed that the MCU on the board is actually the STM32F777IIK6 and provided console output logs.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `dagar` suggested trying the current master version (soon to be v1.11).
- **Result of the operation after the user adopted suggestion 1:** User `pkocmoud` found that the master version was better, with no more lockup.
- **Suggestion 2 provided by developers or other personnel:** Discussion on support for AK09916 compass inside ICM-20948.
- **Result of the operation after the user adopted suggestion 2:** Ongoing work and adjustments to the driver support, with `pkocmoud` confirming that the I2C issue was fixed and awaiting the ICM20948 driver.
- **Suggestion n provided by developers or other personnel:** Developer `lorenzmeier` suggested testing the current configuration to establish a baseline.
- **Result of the operation after the user adopted suggestion n:** `dagar` confirmed that everything was resolved.
