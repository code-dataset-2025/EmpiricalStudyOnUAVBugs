**Environment where the bug occurred:**

- **Hardware environment:** Snapdragon flight
- **Software environment:** PX4 Autopilot version 1.8 (likely affecting the master branch as well according to the report)
- **Report Time:** Feb 4, 2020
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**a82428c

**Steps for bug reproduction:**

- **Step 1:** Do not start the barometer when starting PX4.
- **Step 2:** Use EKF2 enabling External Vision and disabling the barometer with the following parameters:
  ```bash
  param set EKF2_AID_MASK 24
  param set EKF2_HGT_MODE 3
  param set SYS_MC_EST_GROUP 2
  param set SYS_HAS_BARO 0
  ```
- **Step 3:** Launch PX4. 

**Observed behavior by the user:**
- **Behavior after step 1:** N/A
- **Behavior after step 2:** N/A
- **Behavior after step 3:** EKF2 does not start.

**Expected behavior:**
- **Expected behavior 1:** EKF2 should start when `SYS_HAS_BARO` is set to 0, even if there is no incoming barometer data.

**Additional information provided by the user for bug investigation:**
- **Actions taken by the user:** Investigated the issue and found that the function `initialiseFilter()` returns false due to not having enough initial barometer measurements, preventing EKF2 from executing.
- **URL of the flight log provided by the user:** Not provided.

**Communication between developers or other personnel and the user:**
- **Suggestion 1 provided by developers or other personnel:** LorenzMeier suggested submitting a pull request with the required changes since it's a feature request for a specific use case.
- **Result of the operation after the user adopted suggestion 1:** The user expressed willingness to make changes and test on version 1.8.0, highlighting that it may require testing on the master branch as well.
- **Suggestion 2 provided by developers or other personnel:** User marcelino-pensa suggested moving the issue to the ECL repository.
- **Result of the operation after the user adopted suggestion 2:** Not explicitly mentioned, but it seems to be indicated that the issue may also exist in PX4/PX4-ECL#800 per bresch's comment.
- **Additional communication:** A comment from `stale` marked the issue as stale due to inactivity by May 13, 2020.
