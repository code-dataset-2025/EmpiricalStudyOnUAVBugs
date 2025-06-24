**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned
- **Software environment:** PX4 Autopilot at commit version `aa7735c`
- **Report Time:** Jul 23, 2020
- **PX4 Autopilot commit version:** `aa7735c`

**Steps for bug reproduction:**

- **Step 1:** Checkout current master (commit `aa7735c`).
- **Step 2:** Launch SITL using the command `make px4_sitl gazebo_standard_vtol`.
- **Step 3:** Set `MPC_TKO_RAMP_T` parameter to `5`.
- **Step 4:** Load a mission, e.g., use `square vtol.zip`.
- **Step 5:** Start the mission.

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** N/A
- **Behavior after step 3:** Parameter set, no immediate change.
- **Behavior after step 4:** N/A
- **Behavior after step 5:** The drone does not take off with `MPC_TKO_RAMP_T` set to `5`. It takes off with a `4s` delay on `MPC_TKO_RAMP_T = 3` and a `1s` ramp.

**Expected behavior:**

- **Expected behavior 1:** The drone should take off smoothly, respecting the `MPC_TKO_RAMP_T` value for a gradual increase in speed during takeoff.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Experimented with different `MPC_TKO_RAMP_T` values (`5s`, `3s`, and `1s`) to observe the differences and provided logs for analysis.
- **URL of the flight log provided by the user:** 
  - [Log 1](https://logs.px4.io/plot_app?log=0aa9b360-1230-4944-9159-4fb03aabd9d3)
  - [Log 2](https://logs.px4.io/plot_app?log=44529271-2e29-4827-a09a-64d78b725c6d)
  - [Log 3](https://logs.px4.io/plot_app?log=f698d92c-6636-496b-921a-5bc2c3d8a02f)

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `MaEtUgR` suggested investigating a specific code block related to the issue ([FlightTaskAutoLineSmoothVel.cpp](https://github.com/PX4/Firmware/blob/7354e3989335dfb38cc41216182f48fe84d165c7/src/lib/flight_tasks/tasks/AutoLineSmoothVel/FlightTaskAutoLineSmoothVel.cpp#L335-L342)) and attempting the test with those lines commented out.
  
- **Result of the operation after the user adopted suggestion 1:** User `ThomasRigi` confirmed that commenting out the lines resulted in a smooth takeoff ramp, but it ignored `MPC_TKO_SPEED`, which was acceptable for their use case but might not suit others relying on `MPC_TKO_SPEED`. A test log [here](https://logs.px4.io/plot_app?log=c376d64e-d23d-4052-8149-66a6bf6b8ac8) was provided.
