**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned
- **Software environment:** PX4 Autopilot
- **Report Time:** May 30, 2023
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**70178b6

**Steps for bug reproduction:**

- **Step 1:** Set the `windVelocityMean` to 18 in `windy.world` (at the specified line in the GitHub repository).
- **Step 2:** Run SITL with the plane model using the command `make px4_sitl gazebo-classic_plane__windy`.
- **Step 3:** In the PX4 shell, type in the command `commander takeoff`.
- **Step 4:** Observe the error.
- **Step 5:** Vehicle crashes into the ground.

**Observed behavior by the user:**

- **Behavior after step 1:** Wind condition set.
- **Behavior after step 2:** Simulation environment prepared.
- **Behavior after step 3:** Attempted takeoff command given.
- **Behavior after step 4:** Preflight check fails during flight.
- **Behavior after step 5:** Vehicle crashes.

**Expected behavior:**

- **Expected behavior 1:** NPFG should handle high wind cases as long as the airspeed sensor is working.
- **Expected behavior 2:** Airspeed sensor should not be invalidated.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Initiated a takeoff command after setting wind conditions.
- **URL of the flight log provided by the user:** Not explicitly provided.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Suggested that a high wind scenario requires adjustments like covering the pitot and turning off certain preflight checks.
- **Result of the operation after the user adopted suggestion 1:** N/A, it was more of a discussion about handling high wind scenarios.
- **Suggestion 2 provided by developers or other personnel:** Mentioned that the range of acceptable airspeeds was extended, and highlighted an interest in false positives during high wind.
- **Result of the operation after the user adopted suggestion 2:** N/A, as it was more of a feedback mechanism.
- **Suggestion 3 provided by developers or other personnel:** Suggested trying to take off in headwind as a more realistic scenario, highlighting possible issues with wind estimator initialization.
- **Result of the operation after the user adopted suggestion 3:** N/A, provided as a theoretical improvement suggestion.
- **Suggestion 4 provided by developers or other personnel:** Improvement expected with a related issue (\#21764).
- **Result of the operation after the user adopted suggestion 4:** N/A, anticipated future improvement.
