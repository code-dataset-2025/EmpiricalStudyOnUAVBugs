**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned
- **Software environment:** PX4 Autopilot v1.11.0-rc1 with tiltrotor simulation model
- **Report Time:** Aug 6, 2020
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**f950fe8

**Steps for bug reproduction:**

- **Step 1:** Start simulation with the tiltrotor model.
- **Step 2:** Upload mission with a VTOL Takeoff Mission item.
- **Step 3:** Start mission.
- **Step 4:** Observe the motor PWM outputs.

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** N/A
- **Behavior after step 3:** N/A
- **Behavior after step 4:** The motors which are not used (turned off with the parameter VT_FW_MOT_OFFID) initially set to a PWM value of 900, but then unexpectedly increase to a PWM value of 1000.

**Expected behavior:**

- **Expected behavior 1:** The turned-off motors should remain at a PWM value of 900 during the whole fixed-wing mode.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** User noticed the behavior differing from standard VTOL model and questioned the rationale behind the PWM change.
- **URL of the flight log provided by the user:** Not provided.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** None explicitly mentioned; however, there was a note by user `stale` marking the issue as stale due to inactivity.
- **Result of the operation after the user adopted suggestion 1:** N/A, as suggestion was only marking inactivity.
- **Suggestion 2 provided by developers or other personnel:** User `sfuhrer` mentioned they were unable to reproduce the issue on the current master and SITL environment, where MC motors behaved as expected.
- **Result of the operation after the user adopted suggestion 2:** N/A, as suggestion was feedback after reproduction attempts by the developer.
