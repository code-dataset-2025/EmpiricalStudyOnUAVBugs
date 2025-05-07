**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned
- **Software environment:** PX4 Autopilot with unspecified commit version (fixed by PX4/PX4-SITL_gazebo-classic#386 and #415)
- **Report time:** June 11, 2019
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**cef2ba5

**Steps for bug reproduction:**

- **Step 1:** Execute `make px4_sitl gazebo_tiltrotor`.
- **Step 2:** Observe the motors shaking when disarmed.
- **Step 3:** Execute `commander arm`.
- **Step 4:** Observe the shaking stops when armed.
- **Step 5:** Execute `commander disarm`.
- **Step 6:** Observe the shaking resumes after disarming.

**Observed behavior by the user:**

- **Behavior after step 1:** Motors shake when the tiltrotor is disarmed.
- **Behavior after step 3:** Shaking stops when the tiltrotor is armed.
- **Behavior after step 5:** Shaking resumes after disarming the tiltrotor.

**Expected behavior:**

- **Expected behavior 1:** Motors should not shake when the tiltrotor is disarmed.
- **Expected behavior 2:** System should maintain stability whether armed or disarmed.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Reported the issue and discussed potential workarounds and expectations with other developers.
- **URL of the flight log provided by the user:** Not provided.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** @dlwalter suggested disabling lockstep and increasing the real-time update rate as a workaround to fix the issue temporarily.
- **Result of the operation after the user adopted suggestion 1:** Disabling lockstep and setting a higher real-time update rate reduced motor shaking, but some transitions remained unstable.
  
- **Suggestion 2 provided by developers or other personnel:** Julien (julianoes) recommended testing with an increased rate from a work-in-progress branch and sought feedback to confirm if it fixed the issue.
- **Result of the operation after the user adopted suggestion 2:** Testing with the new branch that increased the rate to 500 Hz resolved both motor shaking and transition issues, leading to closure of the issue.
