**Environment where the bug occurred:**

- **Hardware environment:** Simulator, `gazebo_standard_vtol`
- **Software environment:** PX4 Autopilot with commit `0ae296bfe21add6276f5c28a97884059fb317999`
- **Report Time:** Mar 17, 2023
- **PX4 Autopilot commit version:** `0ae296bfe21add6276f5c28a97884059fb317999`

**Steps for bug reproduction:**

- **Step 1:** Start simulator using `make px4_sitl gazebo_standard_vtol`.
- **Step 2:** Upload mission `bumpy.zip`.
- **Step 3:** Start mission.
- **Step 4:** Observe the error after waypoint 4 as described.

**Observed behavior by the user:**

- **Behavior after step 1:** The simulator initializes with the standard VTOL setup.
- **Behavior after step 2:** The mission `bumpy.zip` is uploaded successfully.
- **Behavior after step 3:** The mission begins as expected.
- **Behavior after step 4:** After completing loiter to altitude at WP 4, the drone unexpectedly selects WP 6 (bypassing WP 5, though unsure if WP 5 was briefly selected) and flies straight east while adjusting altitude to that specified in WP 5.

**Expected behavior:**

- **Expected behavior 1:** The drone should proceed to WP 5 after completing loiter to altitude at WP 4.
- **Expected behavior 2:** The drone should loiter to the correct altitude after reaching WP 5.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:**
  - Attempted to reproduce the issue using a new plan (`bumpy2.zip`) with waypoints placed close together. Noted that the issue does not occur every time.
  - Used `git bisect` to find the commit/PR causing the behavior, identifying it as `#21168`.
  - Investigated the code in `FixedwingPositionControl::navigateWaypoints` function and provided analysis of potential issues in the logic.

- **URL of the flight log provided by the user:**
  - Initial flight log: [Log1](https://logs.px4.io/plot_app?log=d5fb6ec1-4393-406c-904d-77450f2c6b4f)
  - Additional flight log: [Log2](https://logs.px4.io/plot_app?log=1fc36355-0265-4f81-a060-bdb2341135fd)

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** @Jaeyoung-Lim suggested that the issue may be related to a problem fixed in `#18996`.
  - **Result of the operation after the user adopted suggestion 1:** User investigated further and found the issue relevant but concluded it was caused by a different commit/PR.

- **Suggestion 2 provided by developers or other personnel:** @kibidev noted the problematic commit as `#21168` and suspected older code might be the root cause, suggesting that the commit stopped masking the problem.
  - **Result of the operation after the user adopted suggestion 2:** The user analyzed the `FixedwingPositionControl` code and identified potential issues in the logic but did not provide a final fix.

- **Suggestion 3 provided by developers or other personnel:** @sfuhrer reproduced the issue based on the hints provided by the user and began looking for a solution. Encouraged the user to ping maintainers for faster responses in the future.
  - **Result of the operation after the user adopted suggestion 3:** The user did not take further action but confirmed the maintainer's acknowledgment and reproduction of the issue.

- **Other communications:**
  - @DronecodeBot mentioned the issue on the PX4 discussion forum, but no additional details from the forum were included in the report.
