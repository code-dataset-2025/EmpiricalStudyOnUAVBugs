需求：step2的现象需要6个电机连IO和6个伺服器连FMU

**Environment where the bug occurred:**

- **Hardware environment:** Pixhawk 4, hexacopter with 6 x motors connected to PX4 IO out, and 6 x servos connected to FMU out
- **Software environment:** PX4 Autopilot v1.12.0 beta1 (commit 935c5df)
- **Report Time:** Mar 24, 2021
- **PX4 Autopilot commit version:** commit 935c5df

**Steps for bug reproduction:**

- **Step 1:** Switch on the drone.
- **Step 2:** Arm the drone via RC or QGroundControl (QGC).

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** Motors spin up to ~1500 pwm when the vehicle is armed with no response to throttle or stick inputs.

**Expected behavior:**

- **Expected behavior 1:** Motors should spin at idle speed (~1075 pwm default) when armed.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** 
  - Observed that `actuator_controls_4` and `actuator_controls_5` are functioning normally.
  - Found that `actuator_outputs` is problematic and does not change due to throttle or stick inputs.
  - Mentioned that the issue does not occur with the normal hexacopter airframe (6001_hexa_x).
- **URL of the flight log provided by the user:** [Flight Log](https://review.px4.io/plot_app?log=f2aa0437-ef1d-416c-aa16-5c64591922fa)

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** @jlecoeur mentioned that control allocation is supported on FMU only and advised connecting the motors to FMU outputs and loading the appropriate mixer on FMU.
- **Result of the operation after the user adopted suggestion 1:** @akarshgopal acknowledged the information and inquired about helping with IO support. Found a workaround using `actuator_controls_2`.
- **Suggestion 2 provided by developers or other personnel:** @jlecoeur suggested a temporary solution by modifying the control allocation code.
- **Result of the operation after the user adopted suggestion 2:** @akarshgopal thanked for the suggestion and mentioned willingness to try it out. Later reported success using a summing mixer and `actuator_controls_2`.

- **Additional comment by another user (ErcBunny):** Noted that as of stable release v1.12.3, the issue persists with `actuator_outputs` not responding to changes of `actuator_controls_4`.
