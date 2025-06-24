**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned
- **Software environment:** Not explicitly mentioned
- **Report time:** Dec 15, 2019
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**2a707cf

**Steps for bug reproduction:**

- **Step 1:** SITL jMAVsim on master.
- **Step 2:** Make sure it starts and stays in Manual mode.
- **Step 3:** Wait for GPS lock.
- **Step 4:** Send takeoff command from QGC.
- **Step 5:** See problem in ~1 out of 5 cases.

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** N/A
- **Behavior after step 3:** N/A
- **Behavior after step 4:** Sometimes, rather than taking off, the drone detects takeoff, landing, and disarms.

**Expected behavior:**

- **Expected behavior 1:** The vehicle should take off even if the takeoff command, mode transition, and arming occur almost instantaneously as in a SITL setup.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Described the reproduction steps and linked a flight log for investigation.
- **URL of the flight log provided by the user:** [Flight log](https://logs.px4.io/plot_app?log=03e85548-bd0e-449a-a0cf-9a3b3426b46c)

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Automated response indicating the issue was marked as stale due to a lack of recent activity.
- **Result of the operation after the user adopted suggestion 1:** N/A (the acknowledgment was automated).
  
- **Suggestion 2 provided by developers or other personnel:** The issue author, MaEtUgR, stated that the issue has long been resolved and closed it.
- **Result of the operation after the user adopted suggestion 2:** The issue was closed, indicating resolution.
