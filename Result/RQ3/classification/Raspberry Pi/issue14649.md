**Environment where the bug occurred:**

- **Hardware environment:** Raspberry Pi 4B + Navio2
- **Software environment:** PX4 Autopilot
- **Report Time:** April 12, 2020
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**66eacd2

**Steps for bug reproduction:**

- **Step 1:** Calibrate e.g., mpu9250 gyroscope.
- **Step 2:** Restart PX4 or reload parameters.
- **Step 3:** Observe how CAL_GYRO0_ID gets changed.

**Observed behavior by the user:**
- **Behavior after step 1:** Calibration is successfully performed.
- **Behavior after step 2:** Calibration disappears.
- **Behavior after step 3:** CAL_GYRO0_ID is changed, indicating loss of calibration.

**Expected behavior:**
- **Expected behavior 1:** "param_modify_on_import" should not change CAL_XXX_ID parameters.
- **Expected behavior 2:** Calibration should persist after reboot or parameter reload.

**Additional information provided by the user for bug investigation:**
- **Actions taken by the user:** Traced the issue to the function "param_modify_on_import."
- **URL of the flight log provided by the user:** Not provided.

**Communication between developers or other personnel and the user:**
- **Suggestion 1 provided by developers or other personnel:** Developer `bkueng` suggested testing fix \#14664.
- **Result of the operation after the user adopted suggestion 1:** User `navioglider` confirmed that the fix resolved the issue.
