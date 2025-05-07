**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned
- **Software environment:** PX4 Autopilot v1.11
- **Report Time:** Nov 29, 2020
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**5f0ecc8

**Steps for bug reproduction:**

- **Step 1:** Select VTOL standard HI airframe.
- **Step 2:** Upload a specific mission.
- **Step 3:** During the mission, change the mode to return.

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** N/A
- **Behavior after step 3:** The drone flies directly to the land location and dismisses the planned land pattern.

**Expected behavior:**

- **Expected behavior 1:** The drone should directly fly to the waypoint after the "land start" command following the planned landing pattern.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** The user identified the problem and suggested adding a waypoint between the survey and land start, or editing the code to fix the issue.
- **URL of the flight log provided by the user:** [Flight log](https://logs.px4.io/plot_app?log=5b7ac051-0e0b-4be4-adc9-d8bb75717c56)

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** No explicit suggestions provided in the comments.
- **Result of the operation after the user adopted suggestion 1:** The user mentioned a fix with the PR `12875f7`.
- **Suggestion 2 provided by developers or other personnel:** Not mentioned.
- ...
- **Result of the operation after the user adopted suggestion n:** N/A
