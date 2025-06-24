**Environment where the bug occurred:**

- **Hardware environment:** Gazebo standard VTOL
- **Software environment:** PX4 Autopilot, version 1.11.0-beta2
- **Report Time:** May 20, 2020
- **PX4 Autopilot commit version:** 6c16a29d26b2c79d63f1459be361c8972399d9ce

**Steps for bug reproduction:**

- **Version 1:**
  - **Step 1:** Disable the elevator in the SDF file, e.g., by setting the area of the elevator to 0.
  - **Step 2:** Execute `make px4_sitl gazebo_standard_vtol`.
  - **Step 3:** Ensure that VT_FW_ALT_ERR is set accordingly (15m in the logs).
  - **Step 4:** Launch a mission or another task that causes the drone to transition to Fixed-Wing (FW) mode.
  - **Step 5:** In FW mode, the drone will tip over and lose altitude.
  - **Step 6:** Observe the late triggering of the quadchute.
   
- **Version 2:**
  - **Step 1:** Have the gazebo_standard_vtol model fly a normal mission in FW mode.
  - **Step 2:** Ensure VT_FW_ALT_ERR is set accordingly (15m in the logs).
  - **Step 3:** Disable the pusher motor via the motor failure plugin.
  - **Step 4:** Watch the drone lose altitude and eventually trigger the quadchute.

**Observed behavior by the user:**

- **Version 1:**
  - **Behavior after step 6:** Quadchute triggers too late after the drone loses altitude and it's not possible to recover, resulting in a crash.

- **Version 2:**
  - **Behavior after step 4:** Quadchute triggers late after losing altitude, but sooner than Version 1, still resulting in a crash.

**Expected behavior:**

- **Expected behavior 1:** Quadchute should activate as soon as the loss of VT_FW_ALT_ERR meters of altitude occurs relative to the altitude setpoint.
- **Expected behavior 2:** It should not wait for the drone to fall out of the sky with more than 20m/s vertical speed and more than 25m altitude lost.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Described the behavior in detail and provided steps for reproduction.
- **URL of the flight log provided by the user:** 
  - Version 1: [Flight Log](https://logs.px4.io/plot_app?log=5e45b915-3e91-4156-9d14-956cbffbc73e)
  - Version 2: [Flight Log](https://logs.px4.io/plot_app?log=b3cf09c8-9b47-4832-98bf-b453ebd7cfa2)

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers (sfuhrer):** Re-evaluate the TECS initialization for improved altitude tracking during transitions and potentially clean up VTOL transition logic parameters.
- **Result of the operation after the user adopted suggestion 1:** No follow-up action from the user is recorded.
- **Suggestion 2 provided by developers (sfuhrer post-comment from UASOP):** Put effort into fixing the issues, inquire if assistance from others such as UASOP is feasible.
- **Result of the operation after the user adopted suggestion 2:** Unclear as the communication suggests ongoing efforts or potential collaboration in the future.
- **Follow-up Query by another developer (LorenzMeier):** Inquiry about the current status as of June 2, 2021.
- **Response by original issue author (ThomasRigi):** On June 16, 2021, lack of recent testing results but assumed issues persist due to initialization/aerodynamics issues described earlier.
