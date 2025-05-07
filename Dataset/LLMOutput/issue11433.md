**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned
- **Software environment:** PX4 Autopilot using LPE estimator with external vision and yaw data fusion in Q Estimator
- **Report time:** Feb 11, 2019
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**f1d17c9

**Steps for bug reproduction:**

- **Step 1:** Use PX4 with LPE estimator, external vision estimator, and external vision yaw fused in Q Estimator.<font color='red'>需要额外的传感器</font>
- **Step 2:** Turn off mag sensor.
- **Step 3:** Let the ATTITUDE.yaw converge to VISION_POSITION_ESTIMATE.yaw.
- **Step 4:** Turn off the external vision system.
- **Step 5:** Rotate the autopilot 90 degrees.
- **Step 6:** Watch ATTITUDE.yaw converge back to the last data reported by the external vision system.

**Observed behavior by the user:**
- **Behavior after step 3:** ATTITUDE.yaw converges to VISION_POSITION_ESTIMATE.yaw as expected.
- **Behavior after step 4:** N/A
- **Behavior after step 5:** ATTITUDE.yaw converges back to the last data reported by the external vision system instead of reflecting the 90-degree rotation.

**Expected behavior:**
- **Expected behavior 1:** The Q estimator should stop using external vision data if the last message is too old, allowing the actual yaw change after rotation to be accurately reflected.

**Additional information provided by the user for bug investigation:**
- **Actions taken by the user:** Identified the issue and prepared a fix for testing.
- **URL of the flight log provided by the user:** Not provided.

**Communication between developers or other personnel and the user:**
- **Suggestion 1 provided by developers or other personnel:** Developer `TSC21` encouraged the user to submit a pull request (PR) with the fix.
- **Result of the operation after the user adopted suggestion 1:** User `ArkadiuszNiemiec` tested the fix with PR #11437 and reported that it worked perfectly.

