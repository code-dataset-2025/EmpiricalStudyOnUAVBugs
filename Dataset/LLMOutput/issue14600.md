**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned
- **Software environment:** PX4 Autopilot
- **Report Time:** Apr 5, 2020
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**0257992

**Steps for bug reproduction:**

- **Step 1:** Plug in the battery.
- **Step 2:** Attempt to arm the device; observe for red flashing LED.
- **Step 3:** Open the lid and plug USB into a phone.
- **Step 4:** Check messages for previous attempts and compass inconsistencies.
- **Step 5:** Correct the lid's orientation until compass inconsistency resolves.
- **Step 6:** Reboot and attempt to arm again.
- **Step 7:** Switch to stabilized mode.
- **Step 8:** Unplug the phone and attempt to switch mode/disarm.

**Observed behavior by the user:**

- **Behavior after step 1:** Could not arm the device (red flashing LED).
- **Behavior after step 2:** Not disarmed automatically despite red flashing LED.
- **Behavior after step 3:** Receives messages about compass inconsistency.
- **Behavior after step 4:** Compass inconsistency persists.
- **Behavior after step 5:** Accelerometer bias is too high.
- **Behavior after step 6:** Device arms successfully.
- **Behavior after step 7:** Stabilized mode switches successfully.
- **Behavior after step 8:** Unable to switch modes or disarm after unplugging USB.

**Expected behavior:**

- **Expected behavior 1:** Device should arm without needing USB connection.
- **Expected behavior 2:** Compass should remain consistent.
- **Expected behavior 3:** Mode switching and disarming should function without USB connection.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** User attempted multiple arming configurations, recalibrated compasses, and verified control surfaces and flight modes.
- **URL of the flight log provided by the user:** https://logs.px4.io/plot_app?log=0e19ad39-ed6d-4680-95b1-e74184f7cf74

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Investigate potential issues with mavlink receiver sleep removal and insights from NuttX USB CDC ACM related considerations.
- **Result of the operation after the user adopted suggestion 1:** Not explicitly mentioned.

- **Suggestion 2 provided by developers or other personnel:** Confirmation needed if USB was connected during operation.
- **Result of the operation after the user adopted suggestion 2:** Confirmed USB connection by MaEtUgR causing specific functional behavior.
