**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned
- **Software environment:** Not explicitly mentioned
- **Report Time:** Nov 4, 2019
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**7b83da7

**Steps for bug reproduction:**

- **Step 1:** Make a mission with several waypoints in a straight line, spaced apart.
- **Step 2:** Have a 'hold' specified at one of the middle waypoints for several seconds.<font color='red'>第一次运行成功，但在应当hold的点位没有停留，第二次编译后QGC显示电池错误</font>

**Observed behavior by the user:**
- **Behavior after step 1:** N/A
- **Behavior after step 2:** The vehicle overshoots the waypoint by arriving too fast, then has to backtrack back to the waypoint.

**Expected behavior:**
- **Expected behavior 1:** The vehicle should smoothly stop at the middle waypoint specified.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Not explicitly mentioned
- **URL of the flight log provided by the user:** Not provided

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** None explicitly mentioned in the provided document
- **Result of the operation after the user adopted suggestion 1:** N/A
