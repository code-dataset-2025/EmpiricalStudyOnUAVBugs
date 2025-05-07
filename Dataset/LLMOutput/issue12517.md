**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned
- **Software environment:** Not explicitly mentioned
- **Report Time:** Jul 18, 2019
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**aaad71f

**Steps for bug reproduction:**

- **Step 1:** Run SITL and start a mission while streaming position setpoints through MAVROS with setpoint_raw messages to take off and loiter.<font color='red'>MAVROS</font>
- **Step 2:** After takeoff, switch the vehicle to offboard mode.

**Observed behavior by the user:**

- **Behavior after step 1:** The fixed wing position controller reads from the setpoints in global coordinates instead of local coordinates.
- **Behavior after step 2:** Once in offboard mode, the vehicle simply flies straight instead of following the position setpoints.

**Expected behavior:**

- **Expected behavior 1:** The desired behavior is for the L1 position controller to use the streamed position setpoints as a reference.
- **Expected behavior 2:** The vehicle should follow the position setpoints accurately in offboard mode.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** The user identified the issue with how the fixed wing position controller reads global coordinates instead of local coordinates from the position_setpoint_triplets.
- **URL of the flight log provided by the user:** [Flight log link](https://review.px4.io/plot_app?log=f6204199-f876-4253-8d12-cb454c1e816b)

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** The suggestion for investigating and potentially implementing a L1-like path tracking controller on the companion side to address the issue of streaming position setpoints in fixed wing drones.
- **Result of the operation after the user adopted suggestion 1:** Not mentioned.
