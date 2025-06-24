**Environment where the bug occurred:**

- **Hardware environment:** Pixhawk 2 (The Cube), Frame - DJI F450
- **Software environment:** PX4 Autopilot Master branch (commit e25db01), attempted PR 12650 and the Stable version v1.9.2 (1069058)
- **Report Time:** Aug 13, 2019
- **PX4 Autopilot commit version:** e25db01 & PR Pull12650

**Steps for bug reproduction:**

- **Step 1:** Power on the Drone.
- **Step 2:** Upload mission.
- **Step 3:** Arm vehicle and Takeoff.
- **Step 4:** Observe error message: "Preflight Fail: Compass trying to build PX4 Firmware on OSX 10.7 #2 uncalibrated".
- **Step 5:** Calibrate vehicle.
- **Step 6:** Encounter error message: "Gyro 1 no matching uORB devid".
- **Step 7:** Unable to calibrate the vehicle on Master.

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** N/A
- **Behavior after step 3:** The vehicle displays a "Compass not found" message.
- **Behavior after step 4:** Error message encountered regarding compass uncalibrated.
- **Behavior after step 5:** Attempt to calibrate the vehicle.
- **Behavior after step 6:** Calibration fails with gyro-related error.
- **Behavior after step 7:** Unable to calibrate further.

**Expected behavior:**

- **Expected behavior 1:** The compass should be detected and function properly on arming.
- **Expected behavior 2:** The vehicle should calibrate successfully without errors.
- **Expected behavior 3:** The vehicle should be operable with correct navigation and flight capabilities.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Attempted calibration, compared behavior across different software versions, including the Stable version which functioned correctly.
- **URL of the flight log provided by the user:**
  - [Master log](https://review.px4.io/plot_app?log=13cc9db5-4a03-41ff-a9e2-b80013d3e104)
  - [Stable v1.9.2 log](https://logs.px4.io/plot_app?log=71a782cc-7979-4ff1-a6e8-f3d8f4757f55)
  - [PR 12650 log](https://review.px4.io/plot_app?log=18094d44-f808-4b67-b7d6-8ef0df7f4f05)

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `dagar` suspects the issue with the icm20948 driver and plans to investigate further.
- **Result of the operation after the user adopted suggestion 1:** No immediate resolution mentioned in the initial comments.
  
- **Suggestion 2 provided by developers or other personnel:** `JacobCrabill` suggested the issue might be fixed by a related pull request #14345.
- **Result of the operation after the user adopted suggestion 2:** Request for verification by `mrpollo`, later confirmed by `FlavioTonelli` and `JacobCrabill` potentially resolved in newer updates.
  
- **Final outcome:** According to `LorenzMeier`, the issue was solved a long time ago, suggesting a fix was implemented in subsequent software releases.
