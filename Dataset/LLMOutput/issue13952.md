**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned
- **Software environment:** Latest master on the date of the report
- **Report Time:** Jan 15, 2020
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**d6cff80

**Steps for bug reproduction:**

- **Step 1:** In a Software in the Loop (SITL) environment, use the standard VTOL model.
- **Step 2:** Plan a mission using a VTOL takeoff item.
- **Step 3:** Add a couple of waypoints to be navigated as fixed wing.
- **Step 4:** Add a land waypoint as the last waypoint.

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** N/A
- **Behavior after step 3:** N/A
- **Behavior after step 4:** The vehicle executes the transition and upon completion, starts descending immediately, even without reaching close to the land waypoint.

**Expected behavior:**

- **Expected behavior 1:** The vehicle should complete the back-transition and move toward the landing waypoint while maintaining the current altitude.
- **Expected behavior 2:** The vehicle should only start descending once it has horizontally reached the land waypoint.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Provided a log file URL: [Flight log](https://logs.px4.io/plot_app?log=4769c91c-9c71-4db5-b98b-b580a3efa943)

**Communication between developers or other personnel and the user:**

- No explicit communication or suggestions between developers or other personnel and the user are mentioned in the provided text.
