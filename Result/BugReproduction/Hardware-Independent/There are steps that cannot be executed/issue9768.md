**Environment where the bug occurred:**

- **Hardware environment:** Gazebo Deltaquad
- **Software environment:** PX4 Autopilot
- **Report Time:** Jun 26, 2018
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**dfcdf22

**Steps for bug reproduction:**

- **Step 1:** Create a "multicopter" mission with Deltaquad in Gazebo (e.g., at a 30m altitude).<font color='red'>缺少deltaquad这个模型，使用默认模型执行，第二步的参数设置为默认不会触发错误</font>
- **Step 2:** Ensure reasonable values for MPC_LAND_SPEED, MPC_Z_VEL_MAX_DN, MPC_LAND_ALT1, MPC_LAND_ALT2.
- **Step 3:** Start the mission.

**Observed behavior by the user:**
- **Behavior after step 1:** N/A
- **Behavior after step 2:** N/A
- **Behavior after step 3:** The vehicle descends with MPC_LAND_SPEED the entire way, instead of initially with MPC_Z_VEL_MAX_DN to MPC_LAND_ALT1, then ramping down to MPC_LAND_SPEED.

**Expected behavior:**
- **Expected behavior 1:** The vehicle should initially descend with MPC_Z_VEL_MAX_DN until it reaches MPC_LAND_ALT1.
- **Expected behavior 2:** After reaching MPC_LAND_ALT1, the vehicle should ramp down to MPC_LAND_SPEED.

**Additional information provided by the user for bug investigation:**
- **Actions taken by the user:** Observed similar behavior in real flights.
- **URL of the flight log provided by the user:** [Flight log](https://logs.px4.io/plot_app?log=70e15793-db80-4ec7-91d8-d1b6af522e70)

**Communication between developers or other personnel and the user:**
- **Suggestion 1 provided by developers or other personnel:** @dagar tagged other developers for input.
- **Result of the operation after the user adopted suggestion 1:** N/A
- **Suggestion 2 provided by developers or other personnel:** Comment by `dagar` suggests the issue may relate to the multicopter position controller rather than VTOL specific.
- **Result of the operation after the user adopted suggestion 2:** N/A
- **Suggestion 3 provided by developers or other personnel:** Reference made by `dakejahl` to see issue #9772.
- **Result of the operation after the user adopted suggestion 3:** N/A
- **Suggestion 4 provided by developers or other personnel:** Comment by `stale` that issue would be marked as stale and closed due to inactivity.
- **Result of the operation after the user adopted suggestion 4:** Issue closed due to inactivity.
