**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned
- **Software environment:** PX4 Autopilot after merging \#16796
- **Report time:** Feb 12, 2021
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**ce552a3

**Steps for bug reproduction:**

- **Step 1:** Execute `make px4_sitl gazebo_rover`.

**Observed behavior by the user:**

- **Behavior after step 1:** The following error message appears repeatedly:
  
  ```bash
  ERROR [parameters] get: param 65535 invalid
  ```

**Expected behavior:**

- **Expected behavior 1:** No error messages related to invalid parameters should appear during the SITL (Software In The Loop) simulation while working on rovers.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Reported the issue and referenced that it occurred after merging a specific commit (\#16796).
- **URL of the flight log provided by the user:** Not provided.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `dagar` indicated that the issue is due to an uninitialized parameter handle and mentioned looking into it.
- **Result of the operation after the user adopted suggestion 1:** N/A (developer acknowledged the issue and planned to address it).

- **Suggestion 2 provided by developers or other personnel:** Not directly provided as part of the comments but was likely addressed in the fix with commit \#16844.
- **Result of the operation after the user adopted suggestion 2:** The problem was ultimately resolved as indicated by the closing of the issue.
