**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned.
- **Software environment:** PX4 Autopilot (commit version not mentioned).
- **Report Time:** Feb 26, 2020.
- **PX4 Autopilot commit version:** Not mentioned.
- **last commit before the reporting time:**b53bd2b

**Steps for bug reproduction:**

- **Step 1:** In SITL, fly a VTOL in fixed-wing mode or a plane.
- **Step 2:** Disable GPS fusing in air by setting `EKF2_AID_MASK` to 0.
- **Step 3:** Switch to Stabilized mode and then back to Altitude mode.<font color='red'>执行完第二步后GPS信息丢失，飞机无法控制并降落执行不了第三步，在飞机落地后可以执行，在log中观察altitude setpoint在设置参数前后消失，但似乎与设置参数的时刻对不上https://logs.px4.io/plot_app?log=e11a43ee-6946-45c2-a861-4efb12867f5f</font>

**Observed behavior by the user:**

- **Behavior after step 1:** N/A.
- **Behavior after step 2:** GPS fusing is disabled successfully.
- **Behavior after step 3:** The attitude setpoints (`att_sp`) and control signals freeze, and altitude mode stops functioning properly.

**Expected behavior:**

- **Expected behavior 1:** Altitude flight mode should work without issues even after a GPS loss, assuming valid barometer data is available.
- **Expected behavior 2:** If this functionality cannot be achieved, the system should disable switching to altitude flight mode without a valid global position.
- **Expected behavior 3:** For VTOL, the system should disable the transition to fixed-wing mode in altitude flight mode when GPS is unavailable.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Conducted SITL testing with specific steps to disable GPS fusing and observed the system behavior.
- **URL of the flight log provided by the user:** [Flight log](https://review.px4.io/plot_app?log=3cfedd2d-14e0-4f6f-8afd-781823577aa6).
- **Additional suggestions:** The user suggested splitting TECS and L1 modules to disentangle the functionality.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by the user:** The user proposed disabling the ability to switch to altitude flight mode if GPS data is unavailable and possibly splitting the TECS and L1 modules for better separation of functionality.
- **Result of the operation after the user adopted suggestion 1:** N/A.

