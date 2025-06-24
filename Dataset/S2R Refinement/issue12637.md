**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned
- **Software environment:** PX4 Autopilot
- **Report Time:** Aug 5, 2019
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**f21dc82

**Steps for bug reproduction:**

- **Step 1:** Build and Flash https://github.com/AlexandreBorowczyk/Firmware/tree/bug/output_scaler
- **Step 2:** Select X-UAV mini Talon configuration
- **Step 3:** Arm the vehicle
- **Step 4:** Observe PWM output of channel 1

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** N/A
- **Behavior after step 3:** N/A
- **Behavior after step 4:** PWM output of channel 1 does not have an offset.

**Expected behavior:**

- **Expected behavior 1:** Output of the channel should have an offset as specified in the simple mixer configuration.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** The user built and flashed a specific branch, selected a configuration, and observed the PWM outputs.
- **Log Files and Screenshots:** Provided log outputs showing the mixer loading correctly but displaying the error "PWM_SERVO_SET_SELECT_UPDATE_RATE" and lack of offset application in PWM outputs.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Julianoes asked RomanBapst if he had experience with this issue.
- **Result of the operation after the user adopted suggestion 1:** No direct solution provided in response.
- **Comment Periodic Reminder:** The issue was marked as stale due to inactivity.
- **User Re-investigation:** Farzadsw mentioned facing a similar issue and identified that the offset in mixers was being overridden by `PWM_MAIN_TRIMx` parameters in the code.
- **Developer Note:** Bkueng noted that mixers were subsequently removed in a later update (\#19990).
