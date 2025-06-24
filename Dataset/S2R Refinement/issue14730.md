需求：step2需要garmin激光雷达

**Environment where the bug occurred:**

- **Hardware environment:** PixHawk 4
- **Software environment:** PX4 Autopilot v1.11.0-beta1
- **Report Time:** Apr 22, 2020
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**172e435

**Steps for bug reproduction:**

- **Step 1:** Flash PixHawk 4 with v1.11.0-beta1 firmware.
- **Step 2:** Connect a Garmin LidarLite on the I2C A port.
- **Step 3:** Use QGC's mavlink console, and run `ll40ls start -X -b 4`.
- **Step 4:** Observe the system's response.

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** N/A
- **Behavior after step 3:** N/A
- **Behavior after step 4:** The Garmin LidarLite does not start when the command `ll40ls start -X -b 4` is executed (unexpected behavior).

**Expected behavior:**

- **Expected behavior 1:** The driver should start and begin producing distance_sensor data.

**Additional information provided by the user for bug investigation:**

- Attempts and observations for various command executions:
  - `ll40ls start -X` starts the driver on bus 2 and 4.
  - `ll40ls start -X -b 2` starts the driver on bus 2, as expected.
  - `ll40ls start -X -b 4` fails to start the driver, unexpectedly.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** bkueng suggested using `ll40ls start -X -b 1`, indicating external buses should match the label.
- **Result of the operation after the user adopted suggestion 1:** Mortefyhn confirmed using `-b 1` works perfectly.
  
- **Suggestion 2 provided by developers or other personnel:** Discussion around potentially modifying the `ll40ls` help output to clarify bus numbering.
- **Result of the operation after the user adopted suggestion 2:** Suggested that output clarification is useful, but changes not yet implemented at the time.   

- **Final resolution:** bkueng confirmed a change would be made to improve clarity [(evidence in comment 13)].
