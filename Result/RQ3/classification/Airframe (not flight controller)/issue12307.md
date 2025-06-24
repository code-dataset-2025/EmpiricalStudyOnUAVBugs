**Environment where the bug occurred:**

- **Hardware environment:** Teal One
- **Software environment:** PX4 1.9.0
- **Report Time:** June 19, 2019
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**4831a4b

**Steps for bug reproduction:**

- **Step 1:** Fly drone in Position mode.
- **Step 2:** Lose communication with the drone. Exact steps to consistently reproduce are unknown.

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** Drone loses communication and descends to the ground.

**Expected behavior:**

- **Expected behavior 1:** Drone should continue doing what it was doing before losing communication because `NAV_RCL_ACT` was set to 0.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Tested the behavior in simulation in position and mission mode.
- **URL of the flight log provided by the user:** [Flight Log](https://review.px4.io/plot_app?log=d97a8a6f-94a6-42fa-abf0-0dff97ba8102)

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** 
  - Developer `dakejahl`: Check the failsafe function in `mc_pos_control_main`, possibly indicating a scenario where the XYZ setpoints stop due to RC loss.
  - `dakejahl`: Suggested checking the impact of `NAV_RCL_ACT` configurations.
  
- **Result of the operation after the user adopted suggestion 1:** 
  - User `RyanHurst` acknowledged and provided additional testing feedback, indicating unspecified behavior in position mode.
  
- **Suggestion 2 provided by developers or other personnel:** 
  - `julianoes`: Attempted to reproduce the issue with tweaks to parameters `NAV_RCL_ACT` and `NAV_DLL_ACT`, shared detailed findings, including potential problems with the current behavior in Position mode.
  
- **Result of the operation after the user adopted suggestion 2:** 
  - Provided feedback and attempted solutions; reopened the issue for further inspection.
  
- **Suggestion 3 provided by developers or other personnel:** 
  - `MaEtUgR`: Made a suggestion to fix the issue in `#13130` and asked for validation from the user.
  
- **Result of the operation after the user adopted suggestion 3:** 
  - Indicated potential failure in solving all aspects, leading to further investigation and discussions.
