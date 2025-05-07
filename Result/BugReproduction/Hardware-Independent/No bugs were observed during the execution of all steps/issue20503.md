**Environment where the bug occurred:**

- **Hardware environment:** SITL Gazebo plane model
- **Software environment:** Not explicitly mentioned
- **Report Time:** Oct 28, 2022
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**498937c

**Steps for bug reproduction:**

- **Step 1:** Fly in offboard mode, for a while in SITL.
- **Step 2:** Check px4 shell.

**Observed behavior by the user:**

- **Behavior after step 1:** Preflight errors keep appearing during flight, specifically "TM: Time jump detected. Resetting time synchroniser."
- **Behavior after step 2:** "Preflight Fail: Yaw estimate error" and "Preflight Fail: Velocity estimate error" warnings appear.

**Expected behavior:**

- **Expected behavior 1:** Preflight errors should not prompt after takeoff.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Provided a flight log but noted "Could not upload to flight review due to size."
- **URL of the flight log provided by the user:** [Flight log](https://drive.google.com/file/d/11N-AGdYJllGIyIddgSK6Ry6q_e2JtuPd/view?usp=sharing)

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** [jstrebel on Feb 21, 2023] Observed the same issue with 1.14 main(beta).
- **Result of the operation after the user adopted suggestion 1:** Not explicitly mentioned.
- **Suggestion 2 provided by developers or other personnel:** [junwoo091400 on Jun 29, 2023] Mentioned the issue might be the same as #21387, which was fixed in the main branch as of May 4th, and questioned if the issue persisted in the main branch.
- **Result of the operation after the user adopted suggestion 2:** Not explicitly mentioned or confirmed by the original reporter.
- **Suggestion 3 provided by developers or other personnel:** [julianoes on Oct 20, 2023] Closed the issue as outdated.
- **Result of the operation after the user adopted suggestion 3:** The issue was closed, implies no further action was necessary or the issue was deemed resolved/obsolete.
