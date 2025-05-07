**Environment where the bug occurred:**

- **Hardware environment:** Pixhawk
- **Software environment:** PX4 Autopilot release 1.13.0
- **Report Time:** Jul 1, 2022
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**7f76761

**Steps for bug reproduction:**

- **Step 1:** Use a minimal setup with a Pixhawk connected to a companion computer sending odometry messages.
- **Step 2:** Ensure odometry messages are received properly with `MAV_ODOM_LP = 1` on the MAVLink inspector.
- **Step 3:** Set EKF2 parameters (`EKF2_AID_MASK`, `EKF2_HGT_MODE`, `EKF2_MAG_TYPE`, `EKF2_EV_DELAY`) as specified.
- **Step 4:** Perform basic motions with the setup and observe the behavior in the logs.

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** Odometry messages seem to be properly received.
- **Behavior after step 3:** N/A
- **Behavior after step 4:** Local position estimates drift back to (0,0), and the z estimate is incorrect. The speed estimate appears accurate.

**Expected behavior:**

- **Expected behavior 1:** EKF2 filter should match the output of the external vision system closely.
- **Expected behavior 2:** Position should not drift to (0,0) and should accurately reflect external vision input.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Followed documentation, adjusted EKF2 parameters, checked logs, and confirmed odometry accuracy.
- **URL of the flight log provided by the user:** https://logs.px4.io/plot_app?log=1a9e5106-c592-48e4-aa23-d93627b1357d

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Check EKF2 solution status as it seems to reject vision position data.
- **Result of the operation after the user adopted suggestion 1:** Confirmed that the control_mode_flags indicate that vision is only used for height fusion. The issue persisted despite increasing vision gates.
  
- **Suggestion 2 provided by developers or other personnel:** Ensure EV noise is not set to 0 and check the source of EKF2_EV_DELAY.
- **Result of the operation after the user adopted suggestion 2:** User acknowledged that logs might have been incorrect and provided new logs. The problem persisted.

- **Suggestion 3 provided by developers or other personnel:** Align yaw source for EV vel/pos to start and try other parameters.
- **Result of the operation after the user adopted suggestion 3:** User attempted with recommended parameters and planned to report back with new logs. Eventually found a solution by aligning the heading source and correcting EKF2_EV_DELAY.

- **Suggestion 4 provided by developers or other personnel:** Consult on PX4 Slack for faster iterations.
- **Result of the operation after the user adopted suggestion 4:** User closed the issue after solving it with the help of `dagar`.

    
