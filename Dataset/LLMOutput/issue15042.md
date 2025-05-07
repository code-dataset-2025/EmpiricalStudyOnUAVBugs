**Environment where the bug occurred:**

- **Hardware environment:** Pixracer R14
- **Software environment:** Standard plane configuration on PX4 Autopilot
- **Report Time:** Jun 5, 2020
- **PX4 Autopilot commit version:** not mentioned
- **last commit before the reporting time:**626895e

**Steps for bug reproduction:**

- **Step 1:** Use the Master branch version as of 5.6.2020.
- **Step 2:** Utilize Pixracer R14 hardware.
- **Step 3:** Configure the setup as a standard plane.

**Observed behavior by the user:**

- **Behavior after step 1:** MAV topic SCALED IMU shows very high noise with an amplitude of about 1000.
- **Behavior after step 2:** Unable to calibrate the gyro due to movement detection.

**Expected behavior:**

- **Expected behavior 1:** IMU data should show minimal noise.
- **Expected behavior 2:** Gyro calibration should not detect movement erroneously.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Tested the suggested fixes with different configurations, reduced bus frequency, and disabled MPU9250.
- **URL of the flight log provided by the user:** [Log link1](https://logs.px4.io/plot_app?log=dfc4f4f4-ce6b-4f57-bece-88d0a4f229f7), [Log link2](https://logs.px4.io/plot_app?log=6b1737af-4b6c-4cc0-96ff-0b730dbfd946)

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** 
  - Developer `dagar` suggested trying commit \#15004.
- **Result of the operation after the user adopted suggestion 1:** The problem persisted.
  
- **Suggestion 2 provided by developers or other personnel:** 
  - Developer `dagar` asked to share a log with \#15004 or console output and later recommended cutting the bus frequency and disabling MPU9250.
- **Result of the operation after the user adopted suggestion 2:** The issue remained with similar errors.

- **Suggestion 3 provided by developers or other personnel:**
  - Developer `dagar` proposed increasing the reset time in the configuration.
- **Result of the operation after the user adopted suggestion 3:** Not explicitly mentioned.

- **Suggestion 4 provided by developers or other personnel:**
  - Suggestion to try the current \#15004 again after diagnosing a problem with certain older ICM20608g units.
- **Result of the operation after the user adopted suggestion 4:** The errors were resolved.
