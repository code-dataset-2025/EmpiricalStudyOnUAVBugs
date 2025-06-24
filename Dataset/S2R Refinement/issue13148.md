**Environment where the bug occurred:**

- **Hardware environment:** CUAV Nano, F450 frame, GPS- NEO V2
- **Software environment:** QGC (version not mentioned)
- **Report Time:** Oct 9, 2019
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**ea35923

**Steps for bug reproduction:**

- **Step 1:** Drone switched on.
- **Step 2:** Uploaded mission.
- **Step 3:** Takeoff in Position Mode.
- **Step 4:** Switch from Position mode to Mission mode.
- **Step 5:** See altitude reading on QGC.

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** N/A
- **Behavior after step 3:** N/A
- **Behavior after step 4:** N/A
- **Behavior after step 5:** Altitude reading on QGC is off by approximately 10 to 13 meters.

**Expected behavior:**

- **Expected behavior 1:** Correct and accurate altitude reading in QGC.
- **Expected behavior 2:** Consistent altitude display as per actual drone's position and mission data.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** No specific actions taken by the user beyond reporting.
- **URL of the flight log provided by the user:** [Log Nano V5](https://review.px4.io/plot_app?log=e3d7bc0a-891d-4ecf-8ebd-01afb7630ab7)

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** MaEtUgR showed interest in reproducing the issue using multiple CUAV V5 nano boards.
- **Result of the operation after the user adopted suggestion 1:** No concrete reproduction of the issue was reported.
- **Suggestion 2 provided by developers or other personnel:** Investigate the barometer's behavior as potential cause of altitude drift.
- **Result of the operation after the user adopted suggestion 2:** Further logs and analysis by MaEtUgR and kamiliritz indicated barometer-induced altitude drift.
- **Suggestion 3 provided by developers or other personnel:** Issue possibly rectified through improvements related to accelerometer bias and height fusing algorithms mentioned by MaEtUgR, no further action required unless issue resurfaces.
- **Result of the operation after the user adopted suggestion 3:** Tony3dr confirmed that the altitude issue no longer persists and agreed to close the issue.
