**Environment where the bug occurred:**

- **Hardware environment:** Hexacopter with Pixhawk 4 and CUAV F9P RTK
- **Software environment:** PX4 v1.13.2
- **Report Time:** Apr 13, 2023
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**82fd298

**Steps for bug reproduction:**

- **Step 1:** Fly the drone with RTK enabled.<font color='red'>需要支持RTK（实时动态载波相位差分技术，用于高精度定位）的硬件，需要飞控支持，且需要一个RTK的GNSS模块</font>
- **Step 2:** Disable the RTK stream coming from a fixed tower or a provider through the internet.

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** The drone loses its position before regaining control.

**Expected behavior:**

- **Expected behavior 1:** The drone should not lose its positioning after losing RTK connection.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Not explicitly mentioned. The user reported the issue and provided log files.
- **URL of the flight log provided by the user:** [Log File](https://logs.px4.io/plot_app?log=7cd9c968-ce40-4c7c-809d-b00fd9f315e3)

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Not explicitly mentioned; however, the user observed this might be a known issue on the ublox side.
- **Result of the operation after the user adopted suggestion 1:** The user decided to close the issue on the PX4 side and continue discussions with ublox.
