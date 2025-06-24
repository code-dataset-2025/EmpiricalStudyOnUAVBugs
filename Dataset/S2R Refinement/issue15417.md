**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned
- **Software environment:** HITL with FMU_V3
- **Report time:** Jul 25, 2020
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**62fe6d5

**Steps for bug reproduction:**

- **Step 1:** Arm the Drone in QGroundControl (QGC), Manual or Position mode engaged.
- **Step 2:** Apply full throttle up.
- **Step 3:** Wait for a few seconds.

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** N/A
- **Behavior after step 3:** The drone disarms and descends uncontrolled.

**Expected behavior:**

- **Expected behavior 1:** The drone is expected to remain armed.
- **Expected behavior 2:** The drone should disarm only on command or when landed.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Not explicitly mentioned.
- **URL of the flight log provided by the user:** Not provided.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Comment from `julianoes` on Apr 29, 2021, suggesting the issue might be fixed by #17481.
- **Result of the operation after the user adopted suggestion 1:** User `bravepaulo` confirmed on May 5, 2021, that the issue was indeed fixed by #17481 and agreed to close the issue.
