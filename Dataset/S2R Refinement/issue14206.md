**Environment where the bug occurred:**

- **Hardware environment:** Pixhawk4 Mini
- **Software environment:** PX4 Autopilot v1.10.1 Stable and current master
- **Report Time:** Feb 22, 2020
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**af6213e

**Steps for bug reproduction:**

- **Step 1:** Set `UAVCAN_ENABLE` to 1, 2, or 3.
- **Step 2:** Reboot the device.
- **Step 3:** Connect UAVCAN devices.

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** UAVCAN does not start automatically.
- **Behavior after step 3:** UAVCAN devices do not receive a node ID and `uavcan status` produces a hard fault.

**Expected behavior:**

- **Expected behavior 1:** Turn on UAVCAN through `UAVCAN_ENABLE`, reboot, connect a UAVCAN device, and it will get a node ID.
- **Expected behavior 2:** If no device is connected, data should be transmitted over CAN High and Low.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Verified pinout and schematic connections, ran various `uavcan` commands manually.
- **URL of the flight log provided by the user:** Not provided.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** `jinger26` suggested consulting with specific team members.
- **Result of the operation after the user adopted suggestion 1:** N/A
- **Suggestion 2 provided by developers or other personnel:** `davids5` recommended starting `uavcan` with `fw` flag and checking the silent pin state.
- **Result of the operation after the user adopted suggestion 2:** User confirmed the silent pin was low but experienced the same issue.
- **Suggestion 3 provided by developers or other personnel:** `davids5` and `LorenzMeier` suggested hardware configurations and testing the CAN transceiver connections.
- **Result of the operation after the user adopted suggestion 3:** User confirmed the pinout correctness and tested different configurations.
- **Suggestion 4 provided by developers or other personnel:** `davids5` suggested changing `UAVCAN_INTERFACES` from 2 to 1.
- **Result of the operation after the user adopted suggestion 4:** This change resolved the issue; no hard fault, and `uavcan` functioned correctly.
