**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned
- **Software environment:** PX4 Autopilot
- **Report Time:** Nov 5, 2020
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**91d1825

**Steps for bug reproduction:**

- **Step 1:** Make `px4_sitl jmavsim`
- **Step 2:** Take off and fly (e.g., using Joystick in QGC).
- **Step 3:** Enable failure injection: `param set SYS_FAILURE_EN 1`.
- **Step 4:** Set `param set COM_POS_FS_DELAY -1`.
- **Step 5:** Turn on orbit mode.
- **Step 6:** Trigger failure with `failure gps off`.
- **Result:** Fail to trigger the GPS failsafe; the drone keeps floating in the air.

Alternative case:
- **Step 1:** Make `px4_sitl jmavsim`
- **Step 2:** Take off and fly (e.g., using Joystick in QGC).
- **Step 3:** Enable failure injection: `param set SYS_FAILURE_EN 1`.
- **Step 4:** Set `param set COM_POS_FS_DELAY -1`.
- **Step 5:** Fly to a different location using "go to the location" in QGC.
- **Step 6:** Trigger failure with `failure gps off`.
- **Result:** The drone blind lands.

**Observed behavior by the user:**
- In the orbit or "go to the location" modes, PX4 does not trigger the GPS failsafe even when the parameter `COM_POS_FS_DELAY` has an invalid value.

**Expected behavior:**
- **Expected behavior 1:** Trigger GPS failsafe on GPS failure in all flight modes, regardless of parameter settings.

**Additional information provided by the user for bug investigation:**
- **Actions taken by the user:** Experimented and identified that the problem stems from the lack of valid range checking for `COM_POS_FS_DELAY`.
- **URLs of the flight logs provided by the user:**
  - [Flight Log 1](https://logs.px4.io/plot_app?log=a5823c45-07e5-43f5-9227-e8493ae89e54)
  - [Flight Log 2](https://logs.px4.io/plot_app?log=05fd86e9-3f3f-48c7-aa4f-117894ce26a3)

**Communication between developers or other personnel and the user:**
- **Suggestion 1 provided by developers or other personnel:** LorenzMeier highlighted that the parameter system is designed to prevent setting invalid parameters, and emphasized the importance of configuration management.
- **Result of the operation after the user adopted suggestion 1:** The user clarified that earlier PX4 versions enforced parameter value ranges to prevent such issues.

