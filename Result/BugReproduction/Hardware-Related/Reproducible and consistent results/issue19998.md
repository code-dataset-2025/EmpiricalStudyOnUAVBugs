**Environment where the bug occurred:**

- **Hardware environment:** Pixhawk 4 and Pixhawk 6X
- **Software environment:** QGroundControl (daily build), tested on PX4 Autopilot Main and Developer branches, v1.13.0 Stable or Beta
- **Report Time:** Aug 2, 2022
- **PX4 Autopilot commit version:** c5f72fb (also tested Main from August 1)

**Steps for bug reproduction:**

- **Step 1:** Flash either "Developer" branch option in QGC or build and flash Main branch onto a Pixhawk 4 or Pixhawk 6X.
- **Step 2:** Attempt to use Level Horizon calibration tool under Sensors in QGC.
- **Step 3:** Dialog will pop up to start calibration, click OK.
- **Step 4:** After clicking OK, dialog box disappears, and there is no other message or change to indicate anything happened.
- **Step 5:** Verify that SENS_BOARD_X_OFF and SENS_BOARD_Y_OFF parameters have not changed.<font color='red'>现象一致，这两个值在调整前后不变，均为0</font>

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** N/A
- **Behavior after step 3:** Dialog to start calibration appears, user clicks OK.
- **Behavior after step 4:** Dialog box disappears with no further message or change.
- **Behavior after step 5:** SENS_BOARD_X_OFF and SENS_BOARD_Y_OFF parameters remain unchanged.

**Expected behavior:**

- **Expected behavior 1:** Indications in GUI of carrying out the calibration (either success or failure).
- **Expected behavior 2:** SENS_BOARD_X_OFF and SENS_BOARD_Y_OFF parameters get updated.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** The user has tested with different branches and commits, examined the level calibration code, identified an unintentional code modification related to level calibration.
- **URL of the flight log provided by the user:** [Developer branch log](https://review.px4.io/plot_app?log=a8e7148c-d405-41a8-9247-2cb3d288deb1)

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Suggested by tstastny that the issue might be linked to QGC not sending the command.
- **Result of the operation after the user adopted suggestion 1:** User continued investigating.
- **Suggestion 2 provided by developers or other personnel:** Suggested by benberry3d that a commit might have accidentally removed crucial code and proposed reverting the change.
- **Result of the operation after the user adopted suggestion 2:** benberry3d confirmed the issue was resolved after reverting the code, submitted PR #20117.
- **Suggestion 3 provided by developers or other personnel:** Suggested by junwoo091400 to reset parameters and reselect the airframe to resolve unrelated issues with Pixhawk 6C.
- **Result of the operation after the user adopted suggestion 3:** User decided to try resetting parameters, and planned to raise a separate issue if problems persisted.
