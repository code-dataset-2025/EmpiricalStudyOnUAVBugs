**Environment where the bug occurred:**

- **Hardware environment:** FMUv5, Graupner MZ-12 with Falcon 12 receiver
- **Software environment:** PX4 Autopilot firmware version 1.9
- **Report time:** Jan 11, 2019
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**2e3fa30

**Steps for bug reproduction:**

- **Step 1:** Connect SUMD RC receiver to Pixhawk.
- **Step 2:** Power on Pixhawk.
- **Step 3:** Observe noisy channels on Channel monitor in QGroundControl.

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** N/A
- **Behavior after step 3:** Channels display spikes and noise around a constant sent value of 1500; subsequent crash of entire SUMD input observed.

**Expected behavior:**

- **Expected behavior 1:** Subscribers of RCInput should receive the correctly decoded SUMD signal without noise.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Supplied multiple logs for observing noise and potential crash; compared hardware functionality using ArduPilot firmware where no issues were experienced.
- **URLs of the flight log provided by the user:** `px4_sumd_bug.zip`, `px4_sumd_bug_with_crash.zip`

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Capture a corresponding log file (.ulg) to assist in diagnosis.
- **Result of the operation after the user adopted suggestion 1:** User provided logs but did not capture a crash event in initial files.
- **Suggestion 2 provided by developers or other personnel:** Query about the hardware specifics to potentially replicate issue. Developer indicates equipment acquisition for testing.
- **Result of the operation after the user adopted suggestion 2:** Logs and hardware specifications provided; further query about reconstruction efficacy.
- **Suggestion 3 provided by developers or other personnel:** Investigate common themes with other reported RC issues in version 1.9 and hardware testing.
- **Result of the operation after the user adopted suggestion 3:** User reiterated hardware specifics and issue persistence; further technical insights discussed among developers.
