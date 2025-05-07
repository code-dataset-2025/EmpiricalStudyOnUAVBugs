**Environment where the bug occurred:**

- **Hardware environment:** CUAV Nora
- **Software environment:** PX4 Autopilot on master branch
- **Report Time:** Feb 10, 2021
- **PX4 Autopilot commit version:** d03d46b initially, later tested on ef444da and 82d6cc3

**Steps for bug reproduction:**

- **Step 1:** Use CUAV Nora on the master branch of PX4 Autopilot.
- **Step 2:** Attempt to calibrate the magnetometer using QGroundControl (QGC).
- **Step 3:** Observe for errors during or after the calibration process.

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** N/A
- **Behavior after step 3:** The autopilot reboots itself during or after the magnetometer calibration, leading to loss of calibration data.

**Expected behavior:**

- **Expected behavior 1:** The magnetometer calibration process should complete without causing the autopilot to reboot.
- **Expected behavior 2:** The calibrated values should be saved correctly after the calibration process is completed.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** The user tried using a debugger and mentioned the possibility of bisecting to find the commit causing the issue.
- **URL of the flight log provided by the user:** No flight log provided as the issue was observed without actual flight.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** LorenzMeier asked for the specific master commit version experiencing the issue.
- **Result of the operation after the user adopted suggestion 1:** The user provided commit d03d46b.
  
- **Suggestion 2 provided by developers or other personnel:** MaEtUgR suggested running the calibration on branch \\\#17439 with boot logging to help identify if the stack is running out of space.
- **Result of the operation after the user adopted suggestion 2:** The issue appeared resolved after using branch \\\#17439, and the user closed the issue, noting it would be reopened if the problem reappeared during further testing.
