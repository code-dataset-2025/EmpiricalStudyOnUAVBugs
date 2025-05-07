**Environment where the bug occurred:**

- **Hardware environment:** VTOL drone using Cube Orange.
- **Software environment:** Not explicitly mentioned.
- **Report Time:** Aug 16, 2021.
- **PX4 Autopilot commit version:** Not mentioned.
- **last commit before the reporting time:**474b018

**Steps for bug reproduction:**

- **Step 1:** Trigger a mission upload from QGroundControl (QGC).
- **Step 2:** Use a telemetry link that is slow or "full."
- **Step 3:** Observe mission request behavior from PX4.

**Observed behavior by the user:**

- **Behavior after step 1:** PX4 receives mission count.
- **Behavior after step 2:** PX4 begins element requests; element requests are repeatedly triggered due to timeouts and receiving unexpected elements.
- **Behavior after step 3:** Excessive mission requests result in a flooded telemetry link, further worsening the delay.

**Expected behavior:**

- **Expected behavior 1:** PX4 should not send requests for unexpected elements.
- **Expected behavior 2:** PX4 should avoid re-requesting elements that have already been successfully received.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Described the scenario and provided a detailed bug report but could not generate a relevant logfile. Screenshot described was of a flight plan upload with 100 waypoints.
- **URL of the flight log provided by the user:** Not provided.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `dagar` acknowledged the detailed bug report.
- **Result of the operation after the user adopted suggestion 1:** N/A (The developer only acknowledged the report).
