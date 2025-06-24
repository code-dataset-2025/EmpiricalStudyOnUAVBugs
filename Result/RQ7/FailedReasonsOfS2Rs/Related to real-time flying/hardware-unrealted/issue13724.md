**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned
- **Software environment:** Not explicitly mentioned
- **Report Time:** Dec 10, 2019
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**2b792c0

**Steps for bug reproduction:**

- **Step 1:** Set FMU PWM as main output.<font color='red'>设置FMU PWM为主输入（疑似为实机）</font>
- **Step 2:** Run camera_capture and turn it on.
- **Step 3:** Try to arm the system.

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** N/A
- **Behavior after step 3:** No motor spin when the system is armed.

**Expected behavior:**

- **Expected behavior 1:** Motor should spin when the system is armed.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** The user ran `$ fmu test` and attempted to arm again, which resulted in the motors spinning.
- **URL of the flight log provided by the user:** Not provided

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Comment by `julianoes`: Recommended configuring FMU to use specific pins and running camera_capture on the remaining pins.
- **Result of the operation after the user adopted suggestion 1:** Not mentioned.
- **Suggestion 2 provided by developers or other personnel:** Comment by `stale`: Issue marked as stale due to inactivity.
- **Result of the operation after the user adopted suggestion 2:** Not applicable as it was an automatic action rather than a user query.
- **Suggestion 3 provided by developers or other personnel:** Comment by `julianoes`: Followed up with a query asking for updates or responses.
- **Result of the operation after the user adopted suggestion 3:** Not mentioned.
