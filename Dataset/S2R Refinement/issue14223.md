Here’s the structured output based on your provided details:

---

# Basic Information:
### Title: EKF does not switch to secondary GPS if main fails #14223
### Issue status: Closed
### Author: CarlOlsson
### Issue open time: Feb 24, 2020
### Fixed by: #14278

# Report
### Report author: CarlOlsson
### Report Time: Feb 24, 2020
### Report Content:
**Describe the bug:**  
If a vehicle has two GPS modules connected and the main one fails while it has a higher fix type than the secondary GPS, the EKF will not switch to only use the secondary GPS but will stop fusing GPS completely.

**Steps to reproduce:**  
1. Collect a replay logfile with a vehicle using two GPS modules.  
2. Stop publishing from the first GPS module when it has a higher fix type than the secondary GPS.

**Expected behavior:**  
- The EKF should switch to only use the secondary GPS.

**Additional context:**  
- The issue arises because `_gps_state[0].fix_type` is never updated after the GPS failure, so `_gps_select_index` is never set to `1`.  
- Relevant code snippet: [Link](https://github.com/PX4/Firmware/blob/f3fefd7d9372ec98d404e2e99da2e251114a2d7e/src/modules/ekf2/ekf2_main.cpp#L953-L988)

# Comment
## Comment1
### Comment author: CarlOlsson
### Comment Time: Feb 24, 2020
### Comment Content:  
It also happens the other way around, and even if the GPS modules have the same fix type.

## Comment2
### Comment author: julianoes
### Comment Time: Mar 2, 2020
### Comment Content:  
FYI @DanielePettenuzzo  

## Comment3
### Comment author: CarlOlsson
### Comment Time: Mar 10, 2020
### Comment Content:  
Solved by #14278.

---

**Environment where the bug occurred:**
- **Hardware environment:** Not explicitly mentioned.
- **Software environment:** Not explicitly mentioned.
- **Report Time:** Feb 24, 2020.
- **PX4 Autopilot commit version:** Not mentioned.
- **last commit before the reporting time:**f3fefd7

**Steps for bug reproduction:**
- **Step 1:** Collect a replay logfile with a vehicle using two GPS modules.<font color='red'>需要2个GPS设备</font>
- **Step 2:** Stop publishing data from the first GPS module when it has a higher fix type than the secondary GPS.

**Observed behavior by the user:**
- **Behavior after step 1:** N/A.
- **Behavior after step 2:** EKF stops fusing GPS completely and does not switch to the secondary GPS.

**Expected behavior:**
- **Expected behavior 1:** The EKF should switch to only use the secondary GPS.

**Additional information provided by the user for bug investigation:**
- **Actions taken by the user:** Provided details on the bug cause (lack of `_gps_state[0].fix_type` update) and relevant code snippet.
- **URL of the flight log provided by the user:** Not provided.

**Communication between developers or other personnel and the user:**
- **Suggestion 1 provided by developers or other personnel:** Developer `julianoes` notified another developer (`DanielePettenuzzo`) for further investigation.
- **Result of the operation after the user adopted suggestion 1:** N/A.
- **Suggestion 2 provided by developers or other personnel:** Developer `CarlOlsson` confirmed the issue was resolved with commit `#14278`.
- **Result of the operation after the user adopted suggestion 2:** Bug fixed.

---
