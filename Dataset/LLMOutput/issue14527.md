需求:step3电池

**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned (But problem noted with Pixhawk 4)
- **Software environment:** PX4 Autopilot with version specified by the GitHub URL
- **Report Time:** Mar 30, 2020
- **PX4 Autopilot commit version:** 73f7243bc8350664864685d1a0adbeaaa2f2c5e5

**Steps for bug reproduction:**

- **Step 1:** Power the drone with a battery and power module such that it measures a battery voltage and state.
- **Step 2:** Plug the autopilot to a computer via USB.
- **Step 3:** Unplug the battery.
- **Step 4:** Observe the autopilot attempt to shutdown, noting that the board (Pixhawk 4) doesn't support shutdown.
- **Step 5:** Observe the autopilot entering a SHUTDOWN state where any attempt to calibrate or arm triggers a "Transition denied" message.
- **Step 6:** Arm and start flying a drone. Open the Radio tab in QGC and observe.
- **Step 7:** Use a power supply to bench test your drone, or configure the battery to deplete completely to observe shutdown attempt mid-air.

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** N/A
- **Behavior after step 3:** Autopilot attempts to shut down but cannot because the board does not support it.
- **Behavior after step 4:** The autopilot enters a SHUTDOWN state.
- **Behavior after step 5:** Any attempt to calibrate or arm triggers a transition guard message.
- **Behavior after step 6 and 7:** Transition "ARMED to INIT" denied mid-flight; potential "ARMED to SHUTDOWN" transitions occur.

**Expected behavior:**

- **Expected behavior 1:** Transition guards should remain in place to prevent safety-critical issues.
- **Expected behavior 2:** State machine calls should be revised to minimize user exposure to transition guard messages.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Provided detailed steps to reproduce the bug.
- **URL of the flight log provided by the user:** Not provided.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** User `tacdin` sought guidance for affected users.
- **Result of the operation after the user adopted suggestion 1:** N/A (suggestion was more of a request for direction).
- **Suggestion 2 provided by developers or other personnel:** Developer `dagar` noted that issue should be fixed by PR #14825.
- **Result of the operation after the user adopted suggestion 2:** `MaEtUgR` confirmed the fix in comment referenced with #14825.
