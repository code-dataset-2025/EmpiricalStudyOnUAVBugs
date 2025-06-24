**Environment where the bug occurred:**

- **Hardware environment:** Generic quad-copter with onboard companion computer, Pixhawk 1
- **Software environment:** PX4 Autopilot v10.0.0 with small modifications
- **Report Time:** Feb 10, 2020
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**0d36e50

**Steps for bug reproduction:**

- **Step 1:** Use a quadcopter with onboard companion computer running Pixhawk 1 hardware and PX4 Autopilot firmware version v10.0.0 with user modifications.
- **Step 2:** Perform flights in auto modes (takeoff, loiter, mission).

**Observed behavior by the user:**

- **Behavior after step 1:** Sensor data (e.g., sensor_combined, vehicle_magnetometer) continues to publish normally.
- **Behavior after step 2:** The `ekf2` module stops publishing all messages, causing flight termination. Before it stops, it publishes all messages at the exact same moment with identical timestamps.
- **Behavior before `ekf2` stops:** `CPU` and `RAM` (`cpuload`) also stop publishing messages, as well as `camera_trigger` and `vehicle_land_detected`.

**Expected behavior:**

- **Expected behavior 1:** The `ekf2` module should continue publishing its messages during the flight.
- **Expected behavior 2:** Modules like `cpuload`, `camera_trigger`, and `vehicle_land_detected` should continue functioning without interruption.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** 
  - User added two significant code modifications:
    1. An additional driver for a sensor called `exopulse` (based on the px4flow driver) was created to measure distances via i2c, which integrates with the `landing_target_estimator`.
    2. A new `camera_trigger` interface was created to publish to `actuator_controls_2` for gimbal control.
  - The user added the following code snippet in the `ROMFS/px4fmu_common/init.d/rcS` file:
    ```bash
    \\# Check for irlock sensor - Exo        
    irlock start &        
    \\# Check for exopulse sensor - Exo        
    exopulse start &        
    \\# Start up Landing Target Estimator module - Exo        
    landing_target_estimator start &        
    ```
- **URL of the flight log provided by the user:** Not explicitly provided, but timestamps from the logs were referenced (first log at 17:28, second log at 8:12).

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `bkueng` asked for the changes made to the code to assess the issue and suggested reproducing the problem on the upstream commit.
  - **Result of the operation after the user adopted suggestion 1:** User provided details about the changes, including the added driver and interface.
  
- **Suggestion 2 provided by developers or other personnel:** Developer `bkueng` suggested that the added code might interfere with the system (e.g., potential memory bugs) and recommended either contributing the changes via a pull request for further review or reproducing the issue on the master branch.
  - **Result of the operation after the user adopted suggestion 2:** No explicit follow-up from the user about adopting this suggestion.

