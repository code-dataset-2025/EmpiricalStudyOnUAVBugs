Here is the reformatted document based on your template and the information provided:

---

# Basic Information:
### Title: Divide by zero when calculating IMU integration interval #19760
### Issue status: Closed
### Author: davegelwan
### Issue open time: Jun 2, 2022
### Fixed by: #19765

# Report
### Report author: davegelwan
### Report Time: Jun 2, 2022
### Report Content:   
**Describe the bug:**  
Divide by zero occurs in the `VehicleIMU::ParametersUpdate` method in `VehicleIMU.cpp` when `IMU_GYRO_RATEMAX` is set to zero. This causes the estimator to fail and results in complete loss of control of the drone.  

**To Reproduce:**  
1. Use a fixed-wing drone with software version `v1.13.0-alpha1-4403-g5717434e93`.  
2. Set `IMU_GYRO_RATEMAX` to zero (default in QGroundControl).  
3. Takeoff the drone.  
4. Trigger the `VehicleIMU::ParametersUpdate` method by changing a parameter.  
5. Observe complete loss of control of the drone.  

**Expected behavior:**  
A divide macro should be implemented to check for zero before dividing, preventing crashes.

**Log Files and Screenshots:**  
- VehicleIMU::ParametersUpdate method annotated: Provided.  
- `IMU_GYRO_RATEMAX` default in QGroundControl: 0 for fixed-wing vehicles.  

**Link to problematic commit:**  
`aa64789`  

**Drone Information:**  
- Hardware environment: Fixed-wing drone.  
- Software environment: PX4-Autopilot `v1.13.0-alpha1-4403-g5717434e93`, QGroundControl defaults.  

---

# Detailed Analysis

**Environment where the bug occurred:**

- **Hardware environment:** Fixed-wing drone.  
- **Software environment:** PX4 Autopilot `v1.13.0-alpha1-4403-g5717434e93`, QGroundControl.  
- **Report Time:** Jun 2, 2022.  
- **PX4 Autopilot commit version:** `aa64789`.  

**Steps for bug reproduction:**

1. Use a fixed-wing drone with PX4 Autopilot software version `v1.13.0-alpha1-4403-g5717434e93`.  
2. Set `IMU_GYRO_RATEMAX` to zero (default configuration in QGroundControl).  
3. Take off the drone.  
4. Trigger the `VehicleIMU::ParametersUpdate` method by modifying a parameter.  

**Observed behavior by the user:**

- **Behavior after step 1:** Normal operation.  
- **Behavior after step 2:** Normal until parameters are modified.  
- **Behavior after step 4:** Complete loss of control of the drone due to a divide-by-zero error.  

**Expected behavior:**

- **Expected behavior 1:** A macro to check for zero before performing division.  
- **Expected behavior 2:** The drone should retain control and function normally when `IMU_GYRO_RATEMAX` is zero.  

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:**  
   Provided annotated source code and linked the problematic commit.  

- **URL of the flight log provided by the user:** Not provided.  

---

# Communication between developers or other personnel and the user:

### Suggestion 1 provided by developers or other personnel:
- **Developer:** `dagar`  
- **Time:** Jun 4, 2022  
- **Content:**  
  "Sorry to hear about the crash. Within `VehicleIMU`, the actual intervals are calculated from actual data publication rates, so I think it might be easier to skip the `IMU_GYRO_RATEMAX` constraint in the first place. The `IMU_GYRO_RATEMAX` default is no longer 0. Can you review #19765?"  

### Result of the operation after the user adopted suggestion 1:
- The issue was fixed by pull request `#19765`, which removed the zero constraint.  

--- 

Let me know if any additional refinements are required!
