**Environment where the bug occurred:**

- **Hardware environment:** Pixhawk (fmu-v2) + quadcopter x6
- **Software environment:** PX4 stable in EKF2 mode
- **Report Time:** Apr 14, 2017
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**9038be2

**Steps for bug reproduction:**

- **Step 1:** Disconnect engines from the flight management unit (fmu).
- **Step 2:** Arm throttle in manual mode without GPS available.
- **Step 3:** Set max throttle.
- **Step 4:** Slowly roll the copter ~45 degrees left and observe actuator oscillations.

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** N/A
- **Behavior after step 3:** N/A
- **Behavior after step 4:** Actuators oscillate from min to max.

**Expected behavior:**

- **Expected behavior 1:** Actuators should not experience continuous oscillations.
- **Expected behavior 2:** Smooth operation of the copter without abrupt changes in actuator outputs.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Disconnected all engines to test for frame vibration influence and discovered that oscillations continued.
- **URL of the flight log provided by the user:** [Log 1](http://logs.uaventure.com/view/FbSe3zE7oB3WVCMqqbNF2e), [Log 2](http://review.px4.io/plot_app?log=1c12f28d-7e82-4747-8196-c66e77ff2db0), [Log 3](http://review.px4.io/plot_app?log=ba03e0b6-9146-4e42-aac7-50d2ba333b2a)

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers:** Check if it's a mixer limiting bug on full throttle (MaEtUgR).
- **Result of the operation after the user adopted suggestion 1:** User confirmed continuous oscillations with latest master too; issue persisted.
- **Suggestion 2 provided by developers:** Test with roll rate integral term set to zero to identify if it's a controller issue (diegoeck).
- **Result of the operation after the user adopted suggestion 2:** Not explicitly stated whether user attempted this suggestion.
- **Suggestion 3 provided by developers:** Reproduce the issue on current master branch (MaEtUgR).
- **Result of the operation after the user adopted suggestion 3:** User conducted tests with current master, confirming continuous oscillations and provided additional logs.
