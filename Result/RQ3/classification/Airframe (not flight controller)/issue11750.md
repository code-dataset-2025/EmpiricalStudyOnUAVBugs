**Environment where the bug occurred:**

- **Hardware environment:** Crazyflie 2.0
- **Software environment:** Latest master or 1.9.0beta Firmware
- **Report Time:** Mar 31, 2019
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**39d1751

**Steps for bug reproduction:**

- **Step 1:** Install the latest master or 1.9.0beta Firmware on Crazyflie 2.0 hardware.
- **Step 2:** Connect to QGC using USB or the PA radio (with cfbridge).
- **Step 3:** Observe the connection status on QGC.

**Observed behavior by the user:**

- **Behavior after step 1:** The firmware is installed on Crazyflie 2.0.
- **Behavior after step 2:** The connection attempt is made.
- **Behavior after step 3:** "Waiting for connection" is displayed on QGC indefinitely and no vehicle status or parameters are shown.

**Expected behavior:**

- **Expected behavior 1:** QGC should display vehicle status.
- **Expected behavior 2:** QGC should show parameters.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** User mentioned using cflib 1.6.0 and cfbridge, and provided detailed logs from cfbridge for different firmware versions. The report author also performed a bisection to pinpoint the start of connection issues to a specific commit.
- **URL of the flight log provided by the user:** Not provided.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** @dagar considered the usage of PX4 on Crazyflie 2.
- **Result of the operation after the user adopted suggestion 1:** No immediate results, as it was a discussion on continued support.
- **Suggestion 2 provided by developers or other personnel:** @julianoes asked if anyone could help with maintaining and supporting PX4 on Crazyflie 2.
- **Result of the operation after the user adopted suggestion 2:** @xiangyu-wu provided further debugging insights and possible commit issues, but did not resolve the problem.
- **Final resolution suggestion by @dagar on Jul 27, 2020:** Fixed in commit #15421.
- **Result of the operation after final resolution:** The issue was confirmed fixed by @bresch on Apr 30, 2021.
