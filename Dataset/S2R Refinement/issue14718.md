Here is the extracted information in the requested format for the PX4 Autopilot bug report:

**Environment where the bug occurred:**

- **Hardware environment:** SITL standard VTOL on Gazebo
- **Software environment:** PX4 Autopilot on master from 20.04.2020
- **Report Time:** Apr 21, 2020
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**c5eefc6

**Steps for bug reproduction:**

- **Step 1:** Run SITL: `make px4_sitl gazebo_standard_vtol`.
- **Step 2:** Launch a mission with a VTOL takeoff and transition waypoint.
- **Step 3:** Observe the behavior of the drone during the front transition.

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** N/A
- **Behavior after step 3:** The drone rolls into the wrong direction and deviates from the expected path.

**Expected behavior:**

- **Expected behavior 1:** The drone should face the front transition waypoint.
- **Expected behavior 2:** The drone should fly towards the front transition waypoint.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Mentioned reviewing code changes related to issue #14405 and observed a hardcoded limit that could be improved by being parameterized. Also noticed potential issues with yaw alignment during transition.
- **URL of the flight log provided by the user:** [Log file](https://logs.px4.io/plot_app?log=af78e5c4-99fc-46fb-924c-c706a9fe6964)

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `RomanBapst` suggested reviewing their pull request (PR) that should fix the issue.
- **Result of the operation after the user adopted suggestion 1:** Information not provided in the document.
