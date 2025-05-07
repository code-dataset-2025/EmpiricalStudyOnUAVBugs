**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned
- **Software environment:** PX4 Autopilot
- **Report Time:** Nov 14, 2019
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**9364393

**Steps for bug reproduction:**

- **Step 1:** Start rover and QGroundControl (QGC).
- **Step 2:** Create and upload a mission, then start the mission.
- **Step 3:** Turn off GPS using `gpssim stop` at any point during the mission.
- **Step 4:** Observe two warning messages in QGC.

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** N/A
- **Behavior after step 3:** The vehicle outputs cruising throttle (PWM 1665) and a zero-degree steering angle (PWM 1492). The roll set point is set to 15 degrees, which has no effect on a rover.
- **Behavior after step 4:** Two warning messages appear:  
  ```bash
  WARN  [commander] Failsafe enabled: no global position  
  WARN  [navigator] Global position failure: fixed bank loiter
  ```

**Expected behavior:**

- **Expected behavior 1:** The rover should stop driving upon GPS loss.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Tested the behavior in Software in the Loop (SITL) simulation environment.
- **URL of the flight log provided by the user:** [Flight log](https://logs.px4.io/plot_app?log=b8a6959a-7e85-4ebb-8473-d9d930775e3e)

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** None explicitly mentioned as suggestions, but comments indicate that the issue was marked as stale due to inactivity.
- **Result of the operation after the user adopted suggestion 1:** N/A (no direct interactions or suggestions for changes were followed by the user).
- **Additional comment by chfriedrich98:** Indicated that the behavior has changed since the issue was opened, and now the rover goes into land/descend mode on GPS loss, stopping as requested.
