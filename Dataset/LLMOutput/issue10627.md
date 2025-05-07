Here is the extracted information from the provided markdown document:

**Environment where the bug occurred:**

- **Hardware environment:** NXPhlite - S500
- **Software environment:** Not explicitly mentioned
- **Report Time:** Oct 2, 2018
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**e73c50a

**Steps for bug reproduction:**

- **Step 1:** Run with SDCARD installed.
- **Step 2:** Look on Spectrum analyser at 148Mhz near SDCARD.
- **Step 3:** Remove SDCARD to observe interference change.

**Observed behavior by the user:**

- **Behavior after step 1:** Interference observed.
- **Behavior after step 2:** Interference is present at 148Mhz.
- **Behavior after step 3:** Interference is gone when SDCARD is removed.

**Expected behavior:**

- **Expected behavior 1:** Quiet Spectrum - or at least below FCC/CE limits.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Problem resolved by setting the slew rate on the SD_CLOCK pin to low. A specific brand of SDCARD failed the sd_bench with the new setting. David S updated the code with the latest PR and they are validating various SDCARDs and GPS response for a new pre-scan. A new hardware revision will address shielding and tuning resistor issues.
- **URL of the flight log provided by the user:** Not provided.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** The bug report was marked as stale due to inactivity.
- **Result of the operation after the user adopted suggestion 1:** No further activity; the issue was closed as stale.
