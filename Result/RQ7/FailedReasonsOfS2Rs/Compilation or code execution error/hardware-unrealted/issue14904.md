**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned
- **Software environment:** PX4 Autopilot, presumably affected by commit referenced in Comment1 (`\#11878`)
- **Report Time:** May 14, 2020
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**19bbea7

**Steps for bug reproduction:**

- **Step 1:** Run SITL (Software In The Loop).
- **Step 2:** Execute the following commands to build and run the MAVSDK integration test:
  
  ```bash
  cmake -DCMAKE_BUILD_TYPE=Debug -Bbuild/debug -S.
  cmake --build build/debug -j8
  build/debug/src/integration_tests/integration_tests_runner --gtest_filter="SitlTest.MissionAddWaypointsAndFly"
  ```
  
  <font color='red'>执行后找不到integration_tests文件夹</font>

**Observed behavior by the user:**

- **Behavior after step 2:**  
  - The mission fails with the error: "Distance between waypoints too close: 0 meters".
  - Test output log indicates failures in the integration test, with specific lines not meeting expected success conditions.

**Expected behavior:**

- **Expected behavior 1:** The mission should complete successfully as it did previously.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** User linked the change to a previous commit (`\#11878`) and explained why MAVSDK sends identical waypoints. 
- **URL of the flight log provided by the user:** Not provided.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:**  
  - *LorenzMeier* proposed that the issue with mission geometry could be simplified by adding `NAV_DELAY` instead of allowing overlapping waypoints.
  - *LorenzMeier* added that `NAV_DELAY` is already supported in PX4 and suggested updating MAVSDK's mission generation accordingly.
  - The issue was closed and moved to MAVSDK discussion, emphasizing that the autopilot should not support overlapping waypoints.

- **Result of the operation after the user adopted suggestion 1:**  
  - *julianoes* acknowledged that while `NAV_DELAY` is now confirmed to exist, it doesn't work as intended, citing related issue `\\\\\\#14909`. Also raised concerns about backwards compatibility with existing MAVSDK implementations (`\\\\\\#14910`).

- **Additional suggestions and follow-up:**
  - *dayjaby* inquired about best practices for waypoint commands, specifically `NAV_WAYPOINT` and `NAV_DELAY`.
  - *julianoes* indicated a temporary fix was made (`\\\#14921`), but highlighted that longer-term decisions are needed regarding waypoint distance checks.
