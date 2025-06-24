**Environment where the bug occurred:**

- **Hardware environment:** Yuneec H520
- **Software environment:** Not explicitly mentioned
- **Report Time:** Mar 14, 2019
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**f3533d3

**Steps for bug reproduction:**

- **Step 1:** Set the mission cruise speed and the manual position full stick flight speed to the same relatively high value e.g. 10m/s.
- **Step 2:** Fly away from you in very heavy wind.
- **Step 3:** Fly back to you in manual position mode full speed against the wind.
- **Step 4:** Switch to RTL which should continue flight with the cruise speed (you configured it to be the same).

**Observed behavior by the user:**

- **Behavior after step 1:** Setpoint is full speed but you don't reach full speed because of the wind.
- **Behavior after step 2:** N/A
- **Behavior after step 3:** N/A
- **Behavior after step 4:** Setpoint stays the same and now you reach it.

**Expected behavior:**

- **Expected behavior 1:** You can reach the same speed in both modes even against the wind if the vehicle has enough power.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Verified that the wind is not changing drastically between the two modes.
- **URL of the flight log provided by the user:** [https://logs.px4.io/plot_app?log=f8817dcc-abda-466a-b223-9e504e3486fd](https://logs.px4.io/plot_app?log=f8817dcc-abda-466a-b223-9e504e3486fd)

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Issue was marked as stale due to inactivity.
- **Result of the operation after the user adopted suggestion 1:** N/A (no direct user action indicated)
- **Suggestion 2 provided by developers or other personnel:** Issue automatically closed due to inactivity.
- **Result of the operation after the user adopted suggestion 2:** N/A (no direct user action indicated)
- **Suggestion 3 provided by developers or other personnel:** Re-examination of log data by user MaEtUgR indicated that a moving position setpoint during RTL might be causing the observed behavior.
- **Result of the operation after the user adopted suggestion 3:** The understanding that the issue resulted from the setpoints and vehicle tuning, specifically horizontal velocity integral. Issue is characterized as a possible side effect rather than a bug.
