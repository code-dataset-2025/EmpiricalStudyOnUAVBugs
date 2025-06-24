**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned
- **Software environment:** PX4 Autopilot
- **Report Time:** Oct 25, 2022
- **PX4 Autopilot commit version:** c13726a (from comment)

**Steps for bug reproduction:**

- **Step 1:** Execute `make px4_sitl gazebo_standard_vtol`.
- **Step 2:** Upload a mission containing a transition, e.g., one from "Zurich FT loiter bug.zip".
- **Step 3:** Launch the mission. Trigger the Hold command at some point after the front transition.
- **Step 4:** Observe the error.
- **Step 5:** Resume the mission, trigger Hold again, and confirm correct loitering.
- **Step 6:** Resume mission, launch a back transition via QGC interface, and trigger Hold again to see it breaks.

**Observed behavior by the user:**

- **Behavior after step 3:** The drone loiters at the wrong position, often around Home or the next Waypoint instead of the current position, and ignores NAV_LOITER_RAD.
- **Behavior after step 6:** The loitering behavior breaks again following a back transition.

**Expected behavior:**

- **Expected behavior 1:** The drone should loiter around the current position when the Hold command is sent.
- **Expected behavior 2:** The loitering should respect the NAV_LOITER_RAD parameter.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Found that during the erroneous loitering, the `position_controller_status/type` stays at 0 instead of the usual 2.
- **URL of the flight log provided by the user:** Multiple logs provided, such as [v1.13 version](https://logs.px4.io/plot_app?log=f24d5c4e-b495-4d9b-93dc-b6e321beda15) and others on upstream.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Attempted to reproduce the issue with current main QGC and VTOL mission plan but couldn't initially.
- **Result of the operation after the user adopted suggestion 1:** User clarified the difference in switching to Hold mode, revealing the issue's dependence on mode-switch methods.
- **Suggestion 2 provided by developers or other personnel:** Proposed fix in the PR #20488.
- **Result of the operation after the user adopted suggestion 2:** User confirmed the fix resolved the issue without introducing new regressions.
