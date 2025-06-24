**Environment where the bug occurred:**

- **Hardware environment:** Tested with Gazebo standard_vtol
- **Software environment:** Not explicitly mentioned
- **Report Time:** Jul 23, 2020
- **PX4 Autopilot commit version:** Current master (aa7735c)

**Steps for bug reproduction:**

- **Step 1:** Checkout current master (aa7735c).
- **Step 2:** Execute `make px4_sitl gazebo_standard_vtol`.
- **Step 3:** Load a mission, e.g., `square vtol.zip`.
- **Step 4:** Start the mission and observe. Use the bug [VTOL] Not yawing towards VTOL Takeoff & Transition waypoint #15409 to trigger RTL with the provided .plan file.
- **Alternative Step 5:** Switch to RTL over QGC once the drone has taken off.

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** N/A
- **Behavior after step 3:** N/A
- **Behavior after step 4/5:** The drone starts to descend immediately and does not reach the Land waypoint of the mission.

**Expected behavior:**

- **Expected behavior 1:** The drone should stay at or above `RTL_RETURN_ALT` until it has reached the landing spot.
- **Expected behavior 2:** Follow the outlined procedure in the documentation: https://docs.px4.io/master/en/flight_modes/return.html.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Provided steps to reproduce the bug and a note about the related bug to trigger RTL.
- **URL of the flight log provided by the user:**
  - [Log 1](https://logs.px4.io/plot_app?log=44529271-2e29-4827-a09a-64d78b725c6d)
  - [Log 2](https://logs.px4.io/plot_app?log=32d68ad0-a322-451d-b3ca-4640bda64670)

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** None explicitly mentioned in the comments, but issue was initially marked as stale due to inactivity.
- **Result of the operation after the user adopted suggestion 1:** N/A
- **Suggestion 2 provided by developers or other personnel:** The issue was fixed by \#16377.
- **Result of the operation after the user adopted suggestion 2:** N/A
