**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned
- **Software environment:** PX4 SITL, Dronecode SDK, QGroundControl (QGC)
- **Report Time:** Apr 5, 2019
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**a3ebe56

**Steps for bug reproduction:**

- **Step 1:** Start PX4 SITL.
- **Step 2:** Open QGroundControl (QGC) and let it connect.
- **Step 3:** Close QGroundControl.
- **Step 4:** Start the Dronecode SDK.<font color='red'>dronecode sdk的使用文档页面丢失，仅有项目页面</font>

**Observed behavior by the user:**

- **Behavior after step 1:** SITL environment starts.
- **Behavior after step 2:** QGC connects to SITL.
- **Behavior after step 3:** QGC disconnects.
- **Behavior after step 4:** Continuous "Data link lost" messages occur.

**Expected behavior:**

- **Expected behavior 1:** The system should maintain a stable data link or gracefully report a temporary loss when switching tools or interfaces.
- **Expected behavior 2:** Consistent behavior regarding data link status should be observed, without frequent toggling between lost and regained.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Adjusted the usage of heartbeats and explored connection types used by the SDK and QGC.
- **URL of the flight log provided by the user:** Not provided.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** LorenzMeier suggested investigating the type of connection used by the SDK and the usage of GCS timeouts.
- **Result of the operation after the user adopted suggestion 1:** Not explicitly given; user julianoes acknowledged the behavior was due to both mavlink instances sending last heartbeat times, causing toggling.

