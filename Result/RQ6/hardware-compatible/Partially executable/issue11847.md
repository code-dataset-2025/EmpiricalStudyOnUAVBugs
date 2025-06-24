**Environment where the bug occurred:**

- **Hardware environment:** Pixhawk 4
- **Software environment:** PX4 Autopilot
- **Report time:** Apr 14, 2019
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**d36b06f

**Steps for bug reproduction:**

- **Step 1:** Set EKF2_MAG_TYPE to "None" or "MC Custom".
- **Step 2:** Reboot the system.
- **Step 3:** Look at the heading estimate.<font color='red'>现象需要实际飞行才能获取</font>

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** N/A
- **Behavior after step 3:** Significant yaw drift is observed without magnetometer fusion enabled.

**Expected behavior:**

- **Expected behavior 1:** Drift lower than the order of degrees per second.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Tried inhibiting IMU bias estimation; however, it didn't have much effect.
- **URL of the flight log provided by the user:** 
  - EKF2_MAG_TYPE = None: [Log Link](https://logs.px4.io/plot_app?log=edb5aada-9f19-424b-958d-9f932517fa9f)
  - EKF2_MAG_TYPE = None, EKF2_AID_MASK with inhibit imu bias estimation: [Log Link](https://logs.px4.io/plot_app?log=074aab41-8e42-41a8-a83e-9bd0430743a0)
  - EKF2_MAG_TYPE = MC Custom: [Log Link](https://logs.px4.io/plot_app?log=53912bb1-dd88-4168-b7a0-988edd0afa1b)
  - EKF2_MAG_TYPE = MC Custom, EKF2_AID_MASK with inhibit imu bias estimation: [Log Link](https://logs.px4.io/plot_app?log=6b17e1d2-6d03-4c29-8c01-ec087c4faf9a)

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** @priseborough mentions parameters like EKF2_ABIAS_INIT and others need retuning, especially for high-quality IMUs, and suggests using replay for tuning.
- **Result of the operation after the user adopted suggestion 1:** No explicit result mentioned, though @mhkabir acknowledged and asked for guidance on replay tuning.
- **Suggestion 2 provided by developers or other personnel:** @bresch notes that for drones undergoing acceleration, yaw drift will be bounded.
- **Result of the operation after the user adopted suggestion 2:** No explicit feedback given by the user, but discussions continued on potential tuning for better results.
