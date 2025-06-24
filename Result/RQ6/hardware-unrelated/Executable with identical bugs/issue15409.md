**Environment where the bug occurred:**

- **Hardware environment:** Gazebo standard_vtol
- **Software environment:** PX4 Autopilot with commit version aa7735c
- **Report Time:** Jul 23, 2020
- **PX4 Autopilot commit version:** aa7735c

**Steps for bug reproduction:**

- **Step 1:** Checkout current master (aa7735c).
- **Step 2:** Execute `make px4_sitl gazebo_standard_vtol`.
- **Step 3:** Load a mission with a VTOL Takeoff & Transition waypoint, e.g., square vtol.zip.
- **Step 4:** Start the mission and observe.

**Observed behavior by the user:**
- **Behavior after step 1:** N/A
- **Behavior after step 2:** N/A
- **Behavior after step 3:** N/A
- **Behavior after step 4:** The VTOL is no longer yawing towards the VTOL Takeoff & Transition waypoint, causing the mission to fail and triggering RTL (Return to Launch).

**Expected behavior:**
- **Expected behavior 1:** The drone should yaw towards the waypoint.
- **Expected behavior 2:** The drone should then transition appropriately.

**Additional information provided by the user for bug investigation:**
- **Actions taken by the user:** Not explicitly mentioned, but included steps to reproduce the behavior and a link to a flight log indicating RTL behavior.
- **URL of the flight log provided by the user:** [Flight Log](https://logs.px4.io/plot_app?log=44529271-2e29-4827-a09a-64d78b725c6d)

**Communication between developers or other personnel and the user:**
- **Suggestion 1 provided by developers or other personnel:** Developer `dagar` asked if the user knew when the issue last worked as expected.
- **Result of the operation after the user adopted suggestion 1:** The user `ThomasRigi` responded, indicating it last worked on PR #15034 (June 04).
- **Suggestion 2 provided by developers or other personnel:** Developer `sfuhrer` indicated that issue may have started after PR #15358.
- **Result of the operation after the user adopted suggestion 2:** N/A (no further action recorded from the user).
