**Environment where the bug occurred:**

- **Hardware environment:** Not mentioned
- **Software environment:** PX4 Autopilot
- **Report time:** Jan 9, 2017
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**71baa4b

**Steps for bug reproduction:**

- **Step 1:** Run simulation using `posix_sitl_ekf2` with `gazebo_iris_opt_flow`.
- **Step 2:** Switch to ALTCTL mode.
- **Step 3:** ARM and takeoff to 3 meters using a joystick.
- **Step 4:** Switch to POSCTL mode.
- **Step 5:** Move the drone outside a textured zone (e.g., asphalt).
- **Step 6:** Move back to a textured zone.
- **Step 7:** Attempt to switch back to POSCTL mode.

**Observed behavior by the user:**

- **Behavior after step 1:** The simulation runs.
- **Behavior after step 2:** The vehicle is in Altitude Control mode.
- **Behavior after step 3:** The vehicle takes off to 3 meters.
- **Behavior after step 4:** The vehicle switches to Position Control mode.
- **Behavior after step 5:** The system fails back to ALTCTL mode once moved outside the textured zone.
- **Behavior after step 6:** The vehicle returns to the textured zone.
- **Behavior after step 7:** Unable to switch back to POSCTL mode.

**Expected behavior:**

- **Expected behavior 1:** POSCTL mode should work even after re-entering a textured zone.
- **Expected behavior 2:** System should allow switching to POSCTL if the flow data is good.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** User removed the 20Hz check in `EstimatorInterface::setOpticalFlowData`, allowing POSCTL to work after a manual takeoff. Reported behavior upon losing focus and returning back to textured area.
  

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** @priseborough explained the choice of limiting the rate of optical flow.
- **Result of the operation after the user adopted suggestion 1:** No specific operation conducted as it was more of an explanation than a direct action to be taken.

- **Suggestion 2 provided by developers or other personnel:** @ChristophTobler suggested modifying the flow message publishing strategy to aggregate data over several frames.
- **Result of the operation after the user adopted suggestion 2:** The discussion led to acknowledging the incorrect hard-coded rate limits but did not result in an immediate fix.

- **Suggestion n provided by developers or other personnel:** Discussion continued on implementing parameterization instead of hardcoding values.
- **Result of the operation after the user adopted suggestion n:** Led to planned updates and improvements but required additional development work.
