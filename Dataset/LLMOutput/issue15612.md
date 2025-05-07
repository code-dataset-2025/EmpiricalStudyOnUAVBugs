**Environment where the bug occurred:**

- **Hardware environment:** 
  - **Flight 1:** Quadrotor Tarot T650 with Pixhawk 4
  - **Flight 2:** Custom coaxial octarotor with Pixhawk 2.1 Cube
- **Software environment:** PX4 Autopilot v1.10.1
- **Report Time:** Aug 25, 2020
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**60a7f7f

**Steps for bug reproduction:**

- **Step 1:** Conduct manual flight indoors with the drone at approximately 5m height above the floor.<font color='red'>步骤中需求在室内5m高度实际飞行无人机</font>
- **Step 2:** Observe any attitude drift in roll and pitch angles or unexpected tilting during the flight.

**Observed behavior by the user:**

- **Behavior after step 1:** After approximately 30s of manual indoor flight, the estimated attitude began to drift significantly in the roll angle, leading to a crash.
- **Behavior after step 2:** Inconsistent attitude estimation resulting in uncontrollable tilting and crashes, despite no signal loss or issues with RC trims.

**Expected behavior:**

- **Expected behavior 1:** Stable attitude estimation throughout the flight with no significant drift.
- **Expected behavior 2:** Drone should maintain a hover state as desired by the pilot.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Attempted to reproduce the issue at lower heights and checked the calibration of sensors.
- **URL of the flight log provided by the user:** Attached log files for Flight 1, Flight 2, and an OK flight where no issues were observed.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `dagar` suggested testing with v1.11.0-rc3 to see if the issue persists, mentioning improvements in the estimator and sensor pipeline.
- **Result of the operation after the user adopted suggestion 1:** User `petrlmat` confirmed plans to try v1.11.0 in future flights but expressed caution due to the risks involved with carrying expensive equipment.
