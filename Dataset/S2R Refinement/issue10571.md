**Environment where the bug occurred:**

- **Hardware environment:** Pixhawk 2.1
- **Software environment:** PX4 Autopilot (firmware version not mentioned)
- **Report Time:** Sep 26, 2018
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**45cf4d4

**Steps for bug reproduction:**

- **Step 1:** Switch off and on the transmitter multiple times.
- **Step 2:** Check the SBUS frames before and after the frames having the failsafe flag on.

**Observed behavior by the user:**

- **Behavior after step 1:** The failsafe flag of the SBUS frame is cleared, but data values of some channels show 0 instead of the correct channel value.

**Expected behavior:**

- **Expected behavior 1:** SBUS frames with incorrect data should be dropped.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** The issue was initially observed with Ardupilot and later tested with the receiver only on the table.
- **URL of the flight log provided by the user:** None provided, but a reference to the ArduPilot fix: [ArduPilot/ardupilot#10216](https://github.com/ArduPilot/ardupilot/pull/10216).
  

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `dagar` asked which flight controller and firmware version were used.
- **Result of the operation after the user adopted suggestion 1:** User `mijarck` confirmed the hardware used and the initial tests on Ardupilot.
- **Suggestion 2 provided by developers or other personnel:** No further suggestions were made; the issue was closed automatically due to inactivity.
