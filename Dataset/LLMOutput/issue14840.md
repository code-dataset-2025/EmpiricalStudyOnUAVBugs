**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned
- **Software environment:** PX4 Autopilot
- **Report Time:** May 6, 2020
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**7207301

**Steps for bug reproduction:**

- **Step 1:** Start sending External Vision (EV) yaw data.
- **Step 2:** Check QGroundControl (QGC); EKF yaw estimate looks fine and matches EV.
- **Step 3:** Stop sending EV data.
- **Step 4:** Check QGC; EKF yaw estimate is spinning out of control.
- **Step 5:** Start sending EV data again.
- **Step 6:** Check QGC; EKF yaw resets to correct EV value, but then continues spinning out of control.

**Observed behavior by the user:**

- **Behavior after step 1:** EKF yaw estimate matches EV data.
- **Behavior after step 3:** EKF yaw estimate spins out of control.
- **Behavior after step 6:** EKF yaw resets to EV value but continues to spin out of control.

**Expected behavior:**

- **Expected behavior 1:** The yaw estimate falls back to compass after EV data stops.
- **Expected behavior 2:** The yaw estimate follows the external vision data after EV restarts.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** The user ran hand/bench tests to reproduce the issue.
- **URL of the flight log provided by the user:** [https://logs.px4.io/plot_app?log=c0a43438-fb28-45fd-9a5b-92329748fb93](https://logs.px4.io/plot_app?log=c0a43438-fb28-45fd-9a5b-92329748fb93)

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** @kamilritz suggested using `resetMagHeading` as a quick hack and mentioned handling the case in `mag_control.cpp`.
- **Result of the operation after the user adopted suggestion 1:** Not explicitly mentioned.
- **Suggestion 2 provided by developers or other personnel:** @kamilritz recommended that the issue might be better addressed in ECL (Estimator Class Library).
- **Result of the operation after the user adopted suggestion 2:** @mhkabir acknowledged the issue and mentioned attempting a proper fix within 1-2 days.
- **Additional communication:** The issue was eventually marked stale due to a lack of recent activity.
