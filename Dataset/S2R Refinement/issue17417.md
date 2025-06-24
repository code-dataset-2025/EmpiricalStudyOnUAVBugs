**Environment where the bug occurred:**

- **Hardware environment:** Omnibus F4, Pixracer, X2.1-777, various Fcs and Airframes
- **Software environment:** PX4 Autopilot
- **Report Time:** Apr 17, 2021
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**38bc46f

**Steps for bug reproduction:**

- **Step 1:** Flash any affected FCs with the current master or beta version.
- **Step 2:** Measure the output pulse rate with an oscilloscope.
- **Step 3:** Observe the behavior of connected servos and ESCs.

**Observed behavior by the user:**

- **Behavior after step 1:** The default rate is displayed as 0 Hz.
- **Behavior after step 2:** The pulse rate is 8 times higher than expected (measured at 3.2 KHz instead of 400 Hz).
- **Behavior after step 3:** All servos on FMU immediately move to the end stop, and the ESCs give Error beep.

**Expected behavior:**

- **Expected behavior 1:** 400 Hz PWM rate should provide 400 Hz pulses.
- **Expected behavior 2:** 50 Hz default rate should provide 50 Hz pulses.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Monitored pulse rates with oscilloscope and attempted various settings including previous stable versions. 
- **URL of the flight log provided by the user:** Not provided.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `dagar` asked for details like airframe selected (SYS_AUTOSTART) and the output status.
- **Result of the operation after the user adopted suggestion 1:** User mentioned it’s a widespread issue affecting multiple airframes and checked frequency settings.
  
- **Suggestion 2 provided by developers or other personnel:** Developer `dagar` mentioned understanding the PWM rate configuration issue and working on a short-term fix.
- **Result of the operation after the user adopted suggestion 2:** User confirmed the fix worked for PWM issue with a specific commit #17427 but noted issues when switching between modes.
