**Environment where the bug occurred:**

- **Hardware environment:** Standard VTOL quadplane, Real drone is a standard VTOL running v1.9 on a Cube.
- **Software environment:** PX4 Autopilot version v1.9 (current master in some instances), SITL for simulation.
- **Report Time:** Aug 20, 2019
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**b439e08

**Steps for bug reproduction:**

- **Step 1:** Start SITL with the command `make px4_sitl gazebo_standard_vtol`.
- **Step 2:** Set the `NAV_GPSF_*` parameters to some non-zero value.
- **Step 3:** Launch a mission or just loiter in FW mode.
- **Step 4:** Trigger the failsafe by disabling the GPS signal with command `gpssim stop`.
- **Step 5:** Observe the drone will not perform the fixed bank loiter properly.
- **Step 6:** Enable the GPS driver again with command `gpssim start`.
- **Step 7:** Observe that the drone will not (directly) recover its global position.
- **Step 8:** Wait.
- **Step 9:** Observe that the drone will not initiate landing and will eventually switch back to the previous mission or loiter.

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** N/A
- **Behavior after step 3:** N/A
- **Behavior after step 4:** The drone does not perform a fixed bank loiter correctly.
- **Behavior after step 5:** The fixed bank loiter is not performed properly.
- **Behavior after step 6:** The drone does not immediately recover its global position.
- **Behavior after step 7:** The drone fails to initiate landing and falls back to its previous mode after some time.

**Expected behavior:**

- **Expected behavior 1:** The drone should perform a fixed bank loiter in FW mode.
- **Expected behavior 2:** Upon recovery of its global position, the drone should continue its mission or previous mode.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** User proposed changes in `GpsFailure::on_active()` to address the fixed bank loiter issue, attempted multiple SITL tests, and created a PR (#12778).
- **URL of the flight logs provided by the user:** 
  - SITL, v1.9: [log link](https://logs.px4.io/plot_app?log=5befa577-0ade-4c90-b82c-045830915138)
  - SITL, current master: [log link](https://logs.px4.io/plot_app?log=ac15492a-04b5-4e27-851e-cdb00cb27d62)
  - Real flight, v1.9: [log link](https://logs.px4.io/plot_app?log=7c1a4be9-8e6b-41e2-b7fa-dd29cd270795)

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** ThomasRigi suggested publishing the GPSF loiter setpoints in `_fw_virtual_att_sp` for VTOLs.
- **Result of the operation after the user adopted suggestion 1:** ThomasRigi confirmed the fixed bank loiter worked with the proposed changes but the recovery was not consistent.
- **Suggestion 2 provided by developers or other personnel:** sfuhrer acknowledged the PR by ThomasRigi and indicated continuation to address recovery and termination behavior.
- **Result of the operation after the user adopted suggestion 2:** Not specifically mentioned; was a continuation of work.
- **Suggestion by another developer (Comment 5 & 6):** julianoes highlighted the issue as a release blocker.
- **Result after final fixes:** Fixed in PR #12778.
