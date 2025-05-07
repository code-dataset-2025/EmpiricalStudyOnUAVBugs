**Environment where the bug occurred:**

- **Hardware environment:** FunCub VTOL airframe, Pixhawk4
- **Software environment:** PX4 Autopilot
- **Report Time:** Apr 3, 2019
- **PX4 Autopilot commit version:** Last tested commit: b6120f3

**Steps for bug reproduction:**

- **Step 1:** Power the drone.
- **Step 2:** Engage kill switch.
- **Step 3:** Power cycle the drone while kill switch is engaged (reboot via QGC does not work to reproduce).
- **Step 4:** Once autopilot finished booting, disengage kill switch.

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** N/A
- **Behavior after step 3:** N/A
- **Behavior after step 4:** Pusher goes to 1500PWM.

**Expected behavior:**

- **Expected behavior 1:** Pusher should not start or output unexpected PWM when the kill switch is disengaged after booting.
- **Expected behavior 2:** The ESC calibration should not affect pusher behavior upon disengaging the kill switch.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Compared PWM outputs in different scenarios.
- **URL of the flight log provided by the user:** [Flight log](https://logs.px4.io/plot_app?log=8185cee6-3a7d-43ec-8a2a-ed5da3d5dcfa)

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** `dagar` asked if the issue persists with a newer master (after April 4th).
- **Result of the operation after the user adopted suggestion 1:** The user reported that the issue still exists on the latest master.
- **Suggestion 2 provided by developers or other personnel:** Not explicitly mentioned, but `RomanBapst` suspected the issue might be related to the specific ESC used.
- **Result of the operation after the user adopted suggestion 2:** Tested with a different ESC on another VTOL and found no issues, regardless of the kill switch position.
