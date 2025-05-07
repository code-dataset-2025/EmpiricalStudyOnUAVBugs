**Environment where the bug occurred:**

- **Hardware environment:** pixhawk 2 fmuv2
- **Software environment:** PX4 Pro, Version 1.10.0
- **Report Time:** Apr 21, 2020
- **PX4 Autopilot commit version:** Git Revision: 4f6faac2c8000000

**Steps for bug reproduction:**

- **Step 1:** Set VTOL DeltaQuad airframe and enable thermal calibration.
- **Step 2:** Perform the thermal calibration.
- **Step 3:** Calibrate accelerometers and observe incorrect roll on the horizon.
- **Step 4:** Do the level horizon calibration and observe the corrected horizon.
- **Step 5:** Calibrate accelerometers again and encounter an error indicating wrong direction detected.

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** N/A
- **Behavior after step 3:** Horizon displays an incorrect roll (about 15 degrees).
- **Behavior after step 4:** The horizon appears correct, but further calibration attempts result in errors.
- **Behavior after step 5:** An error is encountered: "wrong direction detected."

**Expected behavior:**

- **Expected behavior 1:** Thermal calibration should not corrupt accelerometer data.
- **Expected behavior 2:** Successful calibration of sensors without encountering direction errors.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Removed LSM303D sensor and successfully observed better results from thermal calibration.
- **URL of the flight log provided by the user:** [Params with thermal calibration done](https://we.tl/t-5RIMulHMc5); logs and parameters provided later during troubleshooting: [WeTransfer Link](https://we.tl/t-3FQiUReeao).

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `dagar` asked for the thermal calibration log and suggested performing offboard calibration as per the provided documentation link.
- **Result of the operation after the user adopted suggestion 1:** User performed offboard calibration, but the result was the same as before; logs and parameters were provided for troubleshooting.

- **Suggestion 2 provided by developers or other personnel:** Developer `dagar` suggested zeroing out large board offsets before recalibrating.
- **Result of the operation after the user adopted suggestion 2:** User noted offsets and further speculated issues were due to sensor data acquisition (suspected issues merging data between sensors).

- **Suggestion 3 provided by developers or other personnel:** Update build to px4_fmu-v3_default.px4 to ensure TC parameters were present.
- **Result of the operation after the user adopted suggestion 3:** Calibration of accelerometers was successful with new firmware, and situation improved.

- **Suggestion 4 provided by developers or other personnel:** Developer `dagar` requested a full log with corrected accel data shown in the estimator.
- **Result of the operation after the user adopted suggestion 4:** The issue was resolved; user verified arming worked correctly with updated PX4 master and successful sensor calibration.

- **Final feedback from the user:** After further testing, thermal calibration successfully worked post all updates, and the issue was confirmed as fixed following six successful flights.
