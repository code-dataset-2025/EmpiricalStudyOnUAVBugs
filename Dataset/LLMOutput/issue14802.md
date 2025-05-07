**Environment where the bug occurred:**

- **Hardware environment:** Holybro Kakute F7 (including Kakute F7 AIO)
- **Software environment:** Not explicitly mentioned
- **Report Time:** April 30, 2020
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**3ea52fe

**Steps for bug reproduction:**

- **Step 1:** Set `TEL_FRSKY_CONFIG` on the transmitter.
- **Step 2:** Attempt to discover new sensors on the transmitter.

**Observed behavior by the user:**

- **Behavior after Step 1:** N/A
- **Behavior after Step 2:** No sensors are discovered on the transmitter, except for `rxbat` and `rssi`.

**Expected behavior:**

- **Expected behavior 1:** A list of sensors should be displayed on the transmitter.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:**
  1. Used the non-inverted smart-port pad on their `r-xsr`.
  2. Verified packets are being sent using "frsky_telemetry status."
  3. Changed the mode using "frsky_telemetry -m" to both sport and sport_single.
  4. Tried rewiring to UARTs 1, 2, 3, 6 and changing `TEL_FRSKY_CONFIG`.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** `bkueng` mentioned it requires NuttX changes for F7 and was awaiting `davids5` for testing.
- **Result of the operation after the user adopted suggestion 1:** N/A as it required further action from developers.
- **Suggestion 2 provided by developers or other personnel:** `davids5` mentioned that the issue was fixed in PR \#15492 that was merged and instructed to re-open if unresolved.
- **Result of the operation after the user adopted suggestion 2:** Not explicitly mentioned, but the issue was closed implying resolution.
