**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned
- **Software environment:** Not explicitly mentioned
- **Report Time:** Feb 13, 2019
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**197ddd3

**Steps for bug reproduction:**

- **Step 1:** Set the drone to position control mode (using a smoothing FlightTask with low vertical acceleration and jerk).
- **Step 2:** Set the throttle stick to low.<font color='red'>需要控制器</font>
- **Step 3:** Arm the drone and wait a few seconds.
- **Step 4:** Raise the throttle stick above 50%.

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** N/A
- **Behavior after step 3:** N/A
- **Behavior after step 4:** The drone takes time to take off after the throttle stick is raised above 50%.

**Expected behavior:**

- **Expected behavior 1:** The drone should not generate a downward setpoint while on the ground.
- **Expected behavior 2:** The drone should take off as soon as the throttle stick is raised above 50%.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:**
  - Proposed two potential solutions:
    1. Make the FlightTask aware of the current state (so it does not output a downward setpoint while on the ground).
    2. Modify the constraint in `mc_pos_control` and feed it back to the FlightTask.
  - Attempted solution 2 (limited the downward velocity constraint while the vehicle is on the ground).
- **URL of the flight log provided by the user:** Not provided.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `Stifael` suggested reactivating the FlightTask when the vehicle is landed and not in smooth-takeoff mode.
- **Result of the operation after the user adopted suggestion 1:** N/A (no indication that the user adopted this suggestion).
  
- **Suggestion 2 provided by developers or other personnel:** Developer `Stifael` suggested resetting the smoothing behavior during reactivation.
- **Result of the operation after the user adopted suggestion 2:** N/A (no indication that the user adopted this suggestion).

- **Suggestion 3 provided by developers or other personnel:** User `bresch` proposed adding a condition for smooth takeoff on the jerk setpoint.
- **Result of the operation after the user adopted suggestion 3:** N/A (no confirmation if this was implemented or tested).
