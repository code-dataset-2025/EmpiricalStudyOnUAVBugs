**Environment where the bug occurred:**

- **Hardware environment:** Pixhawk 4
- **Software environment:** QGC v4.2.3
- **Report Time:** Dec 15, 2022
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**52c0cba

**Steps for bug reproduction:**

- **Step 1:** In QGC, set the Airframe to SIH Quadcopter X.
- **Step 2:** After rebooting, observe the sensor status in QGC.<font color='red'>将该版本固件刷入飞控后，在QGC中选择完机架并将飞控断电重启，没有出现该报错信息</font>

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** QGC reports "barometer 0 missing" and "compass sensor 0 missing," and the drone won't fly due to pre-flight checks.

**Expected behavior:**

- **Expected behavior 1:** Ability to arm and fly the drone.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Mentioned the specific hardware (Pixhawk 4) and software (QGC v4.2.3) in use.
- **URL of the flight log provided by the user:** Not provided.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `dagar` asked about the board being used.
- **Result of the operation after the user adopted suggestion 1:** The user (`wluker`) responded that they are using Pixhawk 4 and specified the QGC version.
- **Suggestion 2 provided by developers or other personnel:** `TompsonTan` suggested starting `sensor_gps_sim` by adding `sensor_gps_sim start` to rcs.
- **Result of the operation after the user adopted suggestion 2:** The result wasn't explicitly stated, but another user, `bresch`, indicated that they pushed a fix for the issue.
