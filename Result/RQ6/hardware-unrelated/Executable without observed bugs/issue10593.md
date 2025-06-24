**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned
- **Software environment:** Not explicitly mentioned
- **Report Time:** Sep 28, 2018
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**066ca50

**Steps for bug reproduction:**

- **Step 1:** Execute `land_detector stop`
- **Step 2:** Execute `land_detector start multicopter`

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** Modules such as `navigator` do not successfully subscribe to the `vehicle_land_detected` message.

**Expected behavior:**

- **Expected behavior 1:** Position mode should not fail.
  

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Suggested a fix involving uORB message cleanup in the destructor.

  ```cpp
  LandDetector::~LandDetector()
  {
      perf_free(_cycle_perf);
      orb_unadvertise(_landDetectedPub);
  }
  ```

- **URL of the flight log provided by the user:** Not provided.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `bkueng` acknowledged the bug report and pointed to fix #10595.
- **Result of the operation after the user adopted suggestion 1:** N/A (the acknowledgment of the fix did not require action from the user).
