需求：遥控器

**Environment where the bug occurred:**

- **Hardware environment:** Pixhawk4 + GPS Pixhawk 4 + Holybro telemetry
- **Software environment:** PX4 Autopilot version v1.11.0-beta1
- **Report Time:** Apr 15, 2020
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**d67ecc9

**Steps for bug reproduction:**

- **Step 1:** Press the pre-arm button at the GPS to prepare the vehicle for arming, then arm the vehicle in multirotor state via the RC transmitter. Motors spin up at idle PWM.
- **Step 2:** Zero the RC throttle, then activate the transition switch to fixed-wing mode. Motors stop spinning, and tilt-servos move down to a horizontal position.
- **Step 3:** In the fixed-wing state, press the "pre-arm button again" to disarm the vehicle.

**Observed behavior by the user:**

- **Behavior after step 1:** Motors spin up at idle PWM.
- **Behavior after step 2:** Motors stop spinning, and tilt-servos move to a horizontal position.
- **Behavior after step 3:** The user hears a "disarming tone as double short beep" followed by an "arming warning tone as long beep" suddenly. No motor spinning, and tilt-servos return to disarm position (vertical).

**Expected behavior:**

- **Expected behavior 1:** After pressing the pre-arm button to disarm the vehicle in fixed-wing mode, only the "double short beep" should sound to indicate the vehicle is going to be in disarm state.
- **Expected behavior 2:** No "arm tone" should sound until the vehicle is armed by the RC transmitter or QGroundControl (QGC).

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** User planned to test again to obtain the boot log.
- **URL of the flight log provided by the user:** Not provided, but a video link was included: [video link](https://drive.google.com/file/d/13HWmceGjHeR9kE2br4Sv5yqyTqhRS3Sb/view?usp=sharing).

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `dagar` requested the user to share a log file (.ulg) from boot (SDLOG_PROFILE) showing the problem.
- **Result of the operation after the user adopted suggestion 1:** The user agreed to test again to get the log file.
- **Suggestion 2 provided by developers or other personnel:** Issue was later marked as stale due to inactivity.
- **Result of the operation after the user adopted suggestion 2:** N/A.
- **Suggestion 3 provided by developers or other personnel:** Developer `LorenzMeier` mentioned that the issue had been reworked and closed the issue.
- **Result of the operation after the user adopted suggestion 3:** Issue was closed as it was addressed in a future release.
