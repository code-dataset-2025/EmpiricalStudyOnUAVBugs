**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned
- **Software environment:** PX4 Autopilot
- **Report Time:** Oct 18, 2019
- **PX4 Autopilot commit version:** 95dc522b99688a08402ac6462ad28f5dfd338eda

**Steps for bug reproduction:**

- **Step 1:** Execute a failsafe descend test without GPS.
- **Step 2:** Observe the behavior of the land detector in Descend mode.

**Observed behavior by the user:**

- **Behavior after step 1:** The land detector falsely detects ground contact in Descend mode.
- **Behavior after step 2:** The z velocity down is much less than the z velocity setpoint; land speed jumps instead of gradually reaching it as it does in Land (with GPS) mode.<font color='red'>https://logs.px4.io/plot_app?log=374e6c54-f8b6-4920-b26c-0766b0e080da没有表现出这一点</font>

**Expected behavior:**

- **Expected behavior 1:** The system should not detect ground contact until actually landed.
- **Expected behavior 2:** The land speed should be gradually reached like in Land mode with GPS assistance.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Provided links to specific lines of code and flight logs for further investigation.
- **URL of the flight log provided by the user:** 
  - Failsafe descend test: [Link](https://review.px4.io/plot_app?log=3104d449-dd29-473f-9055-354984ff8afa)
  - Normal landing: [Link](https://review.px4.io/plot_app?log=2ea6423f-b232-45c9-8c40-32e775118359)

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Mention of related issues #13124 and #11683 by MaEtUgR.
- **Result of the operation after the user adopted suggestion 1:** No specific results mentioned.
- **Suggestion 2 provided by developers or other personnel:** LorenzMeier asked if a simple solution could be thought of for the issue.
- **Result of the operation after the user adopted suggestion 2:** No specific action taken, but ultimately, the issue was reworked and closed as per LorenzMeier on Jun 2, 2021.
