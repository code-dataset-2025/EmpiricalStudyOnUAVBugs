**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned
- **Software environment:** SITL Gazebo Iris setup within PX4 Autopilot 
- **Report Time:** Aug 29, 2022
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**e780a58

**Steps for bug reproduction:**

- **Step 1:** Run the command `roslaunch px4 mavros_posix_sitl.launch`.
- **Step 2:** Open QGroundControl and change parameters `MPC_XY_VEL_MAX` to 50m/s and `MPC_XY_CRUISE` to 40m/s.
- **Step 3:** Send the drone to a distant location.

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** N/A
- **Behavior after step 3:** The drone's maximum speed is limited to 20m/s instead of the expected 40m/s.

**Expected behavior:**

- **Expected behavior 1:** The flight controller should adjust the maximum allowed speed according to the parameter change to above 20m/s.
- **Expected behavior 2:** The drone should be able to cruise at speeds closer to 40m/s as configured.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Suggested editing `gazebo_motor_model.cpp` at line 222 to modify speed limitation.
- **URL of the flight log provided by the user:** Not provided.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** andreykanevskoi noted that according to the maximum allowed speed in the documentation, it can't be increased.
- **Result of the operation after the user adopted suggestion 1:** Not applicable as no direct resolution was offered in this suggestion.
- **Suggestion 2 provided by developers or other personnel:** Edekheh proposed directly modifying the source code to increase speed potential up to 35-40 m/s.
- **Result of the operation after the user adopted suggestion 2:** Not explicitly mentioned, but the implication is that it allowed higher speed as per user experience.
- **Suggestion 3 provided by developers or other personnel:** andreykanevskoi mentioned issues replicating in AirSim and MavLink setup.
- **Result of the operation after the user adopted suggestion 3:** Not applicable in context as it's more of a comment highlighting challenges in a different simulator environment.
