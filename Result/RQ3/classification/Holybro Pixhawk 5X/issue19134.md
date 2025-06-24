**Environment where the bug occurred:**

- **Hardware environment:** Holybro Pixhawk 5X (fmu-v5x)
- **Software environment:** PX4 Autopilot version v1.12.3
- **Report time:** Feb 5, 2022
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**b4087eb

**Steps for bug reproduction:**

- **Step 1:** Flash v1.12.3 stable.
- **Step 2:** From QGC, reset parameters to default.
- **Step 3:** Set IMU_GYRO_RATEMAX to 250 Hz.
- **Step 4:** Reboot.
- **Step 5:** From the nsh console, run `icm20649 status`.
- **Step 6:** Log `sensor_gyro_0` and `sensor_accel_0` for a minute.

**Observed behavior by the user:**

- **Behavior after step 5:** Several errors show up indicating glitches in the IMU measurements.
- **Behavior after step 6:** Glitches appear on both gyro and accel while the autopilot is fixed on the ground.

**Expected behavior:**

- **Expected behavior 1:** IMU measurements should contain no glitches or discontinuities.
- **Expected behavior 2:** Running `icm20649 status` should show no errors, with gyros reading (0,0,0) and accels reading constant (0,0,-g) when fixed on the ground.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** The user provided detailed steps for reproducing the issue, status command outputs for different IMUs, and tested the issue on the current PX4 master.
- **URL of the flight log provided by the user:** 
  - Log at IMU_GYRO_RATEMAX 250: [Link](https://logs.px4.io/plot_app?log=64ffb368-d808-4687-b811-7b74288e1183)
  - Log at IMU_GYRO_RATEMAX 400: [Link](https://logs.px4.io/plot_app?log=ae0a092a-7756-4e00-b394-129a18e8679c)

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `dagar` suggested to try current PX4 master as icm20649 scheduling was adjusted.
- **Result of the operation after the user adopted suggestion 1:** The user tested with the current master and confirmed the issue did not show up at IMU_GYRO_RATEMAX 250.
- **Suggestion 2 provided by developers or other personnel:** Developer `dagar` mentioned the upcoming v1.13 and possible commits to cherry-pick for v1.12 to fix the issue.
- **Result of the operation after the user adopted suggestion 2:** The user decided to set IMU_GYRO_RATEMAX to 400 Hz on v1.12.3 temporarily to avoid the issue.
