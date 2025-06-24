**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned 
- **Software environment:** PX4 Autopilot with commit version not explicitly mentioned 
- **Report Time:** Aug 14, 2016 
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**8a3b9e3

**Steps for bug reproduction:**

- **Step 1:** Run the PX4 Autopilot system after commit 9f4a91a.
- **Step 2:** Attempt to connect to QGroundControl (QGC) via USB or radio telemetry.

**Observed behavior by the user:**

- **Behavior after step 1:** System starts, but fails to connect.
- **Behavior after step 2:** No connection established with QGC.

**Expected behavior:**

- **Expected behavior 1:** The system should connect to QGC over USB.
- **Expected behavior 2:** The system should connect to QGC over radio telemetry.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** 
  - Reported that reverting changes did not resolve the issue.
  - Identified a hard fault triggered in the MAVLink application.
  - Debugging through `gdb` to trace lines of errors.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `LorenzMeier` suggested running an address sanitizer SITL run and identified potential regression.
- **Result of the operation after the user adopted suggestion 1:** Developer `bkueng` reported not being able to reproduce the issue using address sanitizers, but valgrind indicated possible uninitialized data usage.
- **Suggestion 2 provided by developers or other personnel:** Developer `LorenzMeier` acknowledged the overflow problem and mentioned running EKF2 with enhanced compiler flags.
- **Result of the operation after the user adopted suggestion 2:** Additional monitoring of RAM usage implemented to handle memory issues.
- **Suggestion 3 provided by developers or other personnel:** Developer `bkueng` questioned the source of random pointers and had a discussion about heap corruption indications.
- **Result of the operation after the user adopted suggestion 3:** It was identified that there was an issue with the system running out of RAM.
  

Note: The information extracted above is based on comments and interpretations of the developers during the troubleshooting process.
