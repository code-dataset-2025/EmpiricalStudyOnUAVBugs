**Environment where the bug occurred:**

- **Hardware environment:** SITL Gazebo Iris
- **Software environment:** Not explicitly mentioned
- **Report Time:** Mar 22, 2021
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**e2cd39b

**Steps for bug reproduction:**

- **Step 1:** Takeoff
- **Step 2:** Land
- **Step 3:** While landing, fail every compass instance

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** N/A
- **Behavior after step 3:** During the landing sequence, a compass failure leads to a position loss and the vehicle jerks violently.

**Expected behavior:**

- **Expected behavior 1:** The vehicle should proceed through the landing sequence without issue.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Tested on a recent commit.
- **URL of the flight log provided by the user:** [Flight Log](https://logs.px4.io/plot_app?log=b9da48e7-9b6a-4a87-a9b0-4d1ffb8d4e26)

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `bresch` pointed out several strange observations requiring further investigation, such as mag data stopping before takeoff and other anomalies related to GNSS fusion.
- **Result of the operation after user adopted suggestion 1:** No specific action taken noted in the document.

- **Suggestion 2 provided by developers or other personnel:** Developer `priseborough` mentioned that the issue in the log is not compass loss but an invalid GPS message causing the EKF to reset its position to 0 lat, lon.
- **Result of the operation after user adopted suggestion 2:** N/A (no further action noted).
