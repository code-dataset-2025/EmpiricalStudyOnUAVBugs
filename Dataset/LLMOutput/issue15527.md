**Environment where the bug occurred:**

- **Hardware environment:** MRO X2.1-777
- **Software environment:** PX4 Autopilot with FW version 1.11.0
- **Report Time:** Aug 10, 2020
- **PX4 Autopilot commit version:** 97fc1db768b2ac8fe4121551402912ac57369e1f

**Steps for bug reproduction:**

- **Step 1:** Refer to issue \#15521 for booting and usb-mavlink issues.
- **Step 2:** Set `sys_use_io` to 0 and observe behavior.
- **Step 3:** Set `sys_use_io` to 1 and observe behavior.

**Observed behavior by the user:**

- **Behavior after step 1:** Issues related to booting and usb-mavlink are resolved.
- **Behavior after step 2:** PWM out starts.
- **Behavior after step 3:** IO doesn't start, gets no firmware, and fails to initialize the MTD driver.

**Expected behavior:**

- **Expected behavior 1:** 8 PWM outputs should be available with `sys_use_io` set to 1.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** 
  - Attempted manual connection of safety button contacts and forced firmware update.
  - Tried flashing io with St-Link V2 by SWD.
  - Mentioned that IO now works with the master from September 5th after SWD flashing.
  - Reported that 8 PWM outs, Spektrum rc input, and wifi telemetry 1 work after specific steps.
- **URL of the flight log provided by the user:** Not provided.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `dagar` asked if the safety button was connected and suggested holding it while powering to force px4io upgrade.
- **Result of the operation after the user adopted suggestion 1:** User reported forced firmware update did not work and provided specific error messages.
- **Suggestion 2 provided by developers or other personnel:** N/A
- **Result of the operation after the user adopted suggestion 2:** N/A
