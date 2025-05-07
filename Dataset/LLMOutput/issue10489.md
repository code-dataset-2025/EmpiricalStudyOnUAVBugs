**Environment where the bug occurred:**

- **Hardware environment:** Pixhawk 2.4.8 (Chinese clone board)
- **Software environment:** PX4 Autopilot 1.8
- **Report Time:** Sep 16, 2018
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**8158cdf

**Steps for bug reproduction:**

- **Step 1:** Try to switch on the CAN bus in PX4 1.8 on the Pixhawk 2.4.8.
- **Step 2:** Observe that no UAVCAN configuration is shown.

**Observed behavior by the user:**

- **Behavior after step 1:** The CAN bus does not get enabled; no UAVCAN configuration is shown.

**Expected behavior:**

- **Expected behavior 1:** The CAN bus should enable properly.
- **Expected behavior 2:** The UAVCAN configuration should be visible.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** User confirmed the Pixhawk board type and checked "ver all" for hardware version.
- **URL of the flight log provided by the user:** Not provided.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** `dagar` asked for the board type and suggested checking the build type with `ver all`.
- **Result of the operation after the user adopted suggestion 1:** The user found out they had the px4fmu-v2 board and could not enable UAVCAN with the default build.
  
- **Suggestion 2 provided by developers or other personnel:** `dagar` suggested building a custom binary with certain drivers/modules commented out to include UAVCAN.
- **Result of the operation after the user adopted suggestion 2:** User built a custom binary as suggested, but also inquired about determining the board version before purchase.

- **Suggestion 3 provided by developers or other personnel:** `dagar` suggested upgrading the bootloader for better flash detection, which could allow using px4fmu-v3 build.
- **Result of the operation after the user adopted suggestion 3:** User successfully upgraded, allowing functionality with updated bootloader.
