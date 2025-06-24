**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned
- **Software environment:** PX4 Autopilot
- **Report Time:** Apr 20, 2019
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**c78aaeb

**Steps for bug reproduction:**

- **Step 1:** Switch on the UAV.
- **Step 2:** Put the UAV on a leveled surface.
- **Step 3:** Press the safety switch on.
- **Step 4:** Activate stabilized mode.
- **Step 5:** Move the elevator to the maximum up or maximum down position using manual controls.
- **Step 6:** Wait a few seconds for the elevator servo to twitch; it will be repeated randomly.

**Observed behavior by the user:**

- **Behavior after step 1 to 5:** N/A
- **Behavior after step 6:** The elevator servo experiences random twitching.

**Expected behavior:**

- **Expected behavior 1:** Stable output of servo command without any random glitch or twitching.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** User observed and reported that the elevator twitching correlates perfectly with the indicated airspeed and deduced it is related to airspeed elevator deflection scaling.
- **URL of the flight log provided by the user:** Not provided, but mentioned graph showing elevator twitches.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developers discussed removing airspeed scaling issues and finding a suitable transfer function to avoid actuator jitter at low airspeeds.
- **Result of the operation after the user adopted suggestion 1:** User mentioned further tests provided insights that the twitching disappears when airspeed is forcefully set to non-zero or exactly zero.
- **Suggestion 2 provided by developers or other personnel:** Developer `dagar` highlighted the issue with airspeed validity checks which cause scaling shifts, suggesting sharing a full log for more insights.
- **Result of the operation after the user adopted suggestion 2:** User attempted to locate log data relevant to differential pressure.
- ...
- **Suggestion n provided by developers or other personnel:** The discussion covered architectural changes necessary to handle airspeed scaling more robustly.
- **Result of the operation after the user adopted suggestion n:** The bug was addressed and fixed in the master branch.
