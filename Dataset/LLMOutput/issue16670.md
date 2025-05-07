**Environment where the bug occurred:**

- **Hardware environment:** Pixhawk 1 hardware
- **Software environment:** PX4 Autopilot with firmware version 1.10.2
- **Report Time:** Jan 27, 2021
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**39ad84e

**Steps for bug reproduction:**

- **Step 1:** Flash the 1.10.2 firmware on Pixhawk 1.
- **Step 2:** Follow the steps mentioned in the documentation to set up QGC for HITL.
- **Step 3:** Follow the steps to start the jMAVSim simulator in HITL mode.
- **Step 4:** Create a simple mission, upload it, and start. Follow the instructions provided.
- **Step 5:** Observe the jumpy behavior.

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** N/A
- **Behavior after step 3:** N/A
- **Behavior after step 4:** Jumpy controller performance.
- **Behavior after step 5:** Continued jumpy behavior.

**Expected behavior:**

- **Expected behavior 1:** Smooth controller performance.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Performed HITL Simulation; provided reproduction steps, a flight log URL, and a video.
- **URL of the flight log provided by the user:** Provided in the original report (exact URL not specified in the document).

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `julianoes` suggested that the issue might be related to #17006.
- **Result of the operation after the user adopted suggestion 1:** N/A
- **Suggestion 2 provided by developers or other personnel:** Developer `julianoes` closed the issue as a duplicate.
- **Result of the operation after the user adopted suggestion 2:** N/A (issue was closed).

