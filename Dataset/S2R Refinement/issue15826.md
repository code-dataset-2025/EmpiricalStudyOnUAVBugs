**Environment where the bug occurred:**

- **Hardware environment:** Holybro Kakute F7
- **Software environment:** PX4 Autopilot Release 1.11.0
- **Report Time:** Sep 27, 2020
- **PX4 Autopilot commit version:** 71db090

**Steps for bug reproduction:**

- **Step 1:** Install Firmware 1.10 and run "motor_test iterate." Observe all 4 motors spinning.
- **Step 2:** Install Firmware 1.11 and run "motor_test iterate." Observe motors 0 and 1 not spinning.

**Observed behavior by the user:**

- **Behavior after step 1:** All 4 motors spin as expected.
- **Behavior after step 2:** Motors 0 and 1 do not spin.

**Expected behavior:**

- **Expected behavior 1:** All 4 motors should be operational and spinning.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** The user has provided a detailed log with error messages, hardware architecture information, and firmware details.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `dagar` inquired if the motors worked at all and if they spun when the drone was armed.
- **Result of the operation after the user adopted suggestion 1:** The user confirmed that two motors started spinning when the drone was armed.
  
- **Suggestion 2 provided by developers or other personnel:** Developer `bkueng` confirmed seeing the same issue but noted that DShot worked.
- **Result of the operation after the user adopted suggestion 2:** N/A (no specific action to be taken from this information).
  
- **Suggestion 3 provided by developers or other personnel:** `bkueng` requested the user to test a fix provided in PR \#15867.
- **Result of the operation after the user adopted suggestion 3:** The user tested the fix and confirmed that it resolved the problem.
