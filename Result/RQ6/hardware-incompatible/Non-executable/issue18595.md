**Environment where the bug occurred:**

- **Hardware environment:** X-UAV Talon (1.7 m wingspan), Pixhawk 4 mini, GPS puck, Lidar Lite v3.
- **Software environment:** Not mentioned
- **Report Time:** Nov 9, 2021
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**da51177

**Steps for bug reproduction:**

- **Step 1:** Fly the fixed-wing aircraft in mission mode.
- **Step 2:** Observe the aircraft's behavior when exiting the landing loiter for the final approach.<font color='red'>现象需要实机飞行</font>
- **Step 3:** Note the loiter direction setting (clockwise or counter-clockwise).

**Observed behavior by the user:**

- **Behavior after step 1:** The aircraft tracks the planned path until it exits the landing loiter.
- **Behavior after step 2:** The aircraft makes a turn to the right and lands on a new path, diverging from the planned landing direction.
- **Behavior after step 3:** Reproducible divergence with counter-clockwise loiter set in SITL. Better performance with a clockwise loiter in real flight tests.

**Expected behavior:**

- **Expected behavior 1:** The aircraft should follow the planned landing direction towards the landing waypoint.
- **Expected behavior 2:** The aircraft should not veer off the planned path during landing.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Attempted simulations in SITL with different loiter directions and successfully implemented a workaround using clockwise loiter in real flights.
- **URL of the flight log provided by the user:**
  - Original log: https://logs.px4.io/plot_app?log=eea3a1e0-be68-470d-98ab-3730bf357679
  - Additional example: https://logs.px4.io/plot_app?log=63428e7b-2bd6-490b-9d14-e347effb02a4

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `sfuhrer` noted that the issue was reproducible in SITL and identified a potential problem with the `bearing_lastwp_currwp` calculation.
- **Result of the operation after the user adopted suggestion 1:** The user acknowledged the issue with counter-clockwise loiter and confirmed the workaround using clockwise loiter in real flights.
- **Suggestion 2 provided by developers or other personnel:** Developer `ryanjAA` suggested that the proximity and L1 and acceptable radius settings might affect the landing trajectory.
- **Result of the operation after the user adopted suggestion 2:** It was mentioned that moving the landing point by 30-40m could influence landing accuracy under different loiter conditions.
- **Suggestion n provided by developers or other personnel:** Developer `sfuhrer` and `LorenzMeier` noted ongoing efforts to rework runway support, indicating that changes were being made that may address the issue.
- **Result of the operation after the user adopted suggestion n:** Final confirmation of fix status unclear, but ongoing improvements suggest potential resolution.
