**Environment where the bug occurred:**

- **Hardware environment:** PixRacer hardware version 4 with ESCs Favourite Little Bee 30A, and Motors Emax cooling MT2206 II 1900KV.
- **Software environment:** PX4 Autopilot
- **Report Time:** Jun 22, 2017
- **PX4 Autopilot commit version:** ca480ff

**Steps for bug reproduction:**

- **Step 1:** Plug in the battery and USB cable.
- **Step 2:** Start QGroundControl.
- **Step 3:** Unplug the USB cable.

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** N/A
- **Behavior after step 3:** Motors spin when the USB cable is unplugged if QGroundControl has communicated with the PX4.

**Expected behavior:**

- **Expected behavior 1:** Motors should not spin when the USB cable is unplugged.
- **Expected behavior 2:** PX4 should reset without causing the motors to spin upon USB disconnection.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** User `lericson` provided a workaround by suggesting to place `board_on_reset(0);` before the existing `usleep()` in the source code to stop the motors.
- **Images:** User observed PWM signals with an oscilloscope, but they were not very telling.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `davids5` suggested testing PR #7459 to address the issue.
- **Result of the operation after the user adopted suggestion 1:** User `ndepal` initially found that PR #7459 did not fix the issue.
  
- **Suggestion 2 provided by developers or other personnel:** `davids5` provided specific testing suggestions, like commenting out `usleep` and adding delays to identify the problem.
- **Result of the operation after the user adopted suggestion 2:** User `ndepal` confirmed the motors still spun with initial tests but identified that adding `board_on_reset(0);` with a long enough `usleep()` resolved the issue.
  
- **Final outcome:** After further updates to PR #7459, user `ndepal` confirmed the issue was resolved. Developer `davids5` updated others and verified the fix.
