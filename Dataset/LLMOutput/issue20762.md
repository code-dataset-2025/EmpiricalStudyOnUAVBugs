**Environment where the bug occurred:**

- **Hardware environment:** Pixhawk 6X
- **Software environment:** PX4 Autopilot v1.13.2 (tested on v1.13.0, v1.13.1, and v1.13.2; bug persists in all these versions but not in v1.12.3 or ArduPilot)
- **Report Time:** Dec 13, 2022
- **PX4 Autopilot commit version:** Not explicitly mentioned
- **last commit before the reporting time:**696eeb9

**Steps for bug reproduction:**

1. Hold an oscilloscope probe to the TX pin of the TELEM1 port.
2. Observe that no data is coming through.
3. Hold the probe to the TX pin of the TELEM3 port.
4. Observe that data is coming through.
5. Flash PX4 v1.13.2 onto the Pixhawk 6X using QGC and set the parameters to default (via `param reset_all`).
6. Connect a telemetry radio to the TELEM1 port and check for MAVLink data transmission using QGC or an oscilloscope.

**Observed behavior by the user:**

- **Behavior after step 1:** No data is transmitted through the TX pin of the TELEM1 port.
- **Behavior after step 3:** Data is successfully transmitted through the TX pin of the TELEM3 port.
- **Behavior after step 6:** No data is transmitted through the TELEM1 port even after parameter reset, though the TELEM3 port works fine. When ArduPilot is flashed, TELEM1 works as expected.

**Expected behavior:**

1. Data should be transmitted through the TX pin of the TELEM1 port under all configurations.
2. TELEM1 should work identically to TELEM3 when both are configured for MAVLink.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:**
  - Tested the Pixhawk 6X on PX4 v1.12.3, where TELEM1 worked fine.
  - Tested PX4 v1.13.2 on Pixhawk 5X, where TELEM1 also worked fine.
  - Compared startup procedures and UART port configurations in firmware between Pixhawk 4 and Pixhawk 6X.
  - Verified UART numbering changes in Pixhawk 6X.

- **URL of the flight log provided by the user:** Not provided.
- **Additional testing insights:**
  - Disabling DMA for UART7 solved the issue temporarily.
  - Setting the parameter `MAV_0_FLOW_CTRL` to 0 (disabling flow control) also fixed the issue.

**Communication between developers or other personnel and the user:**

1. **Suggestion 1 provided by developers or other personnel:** Test with stock PX4 v1.13.2 and reset parameters (`param reset_all`).
   - **Result of the operation after the user adopted suggestion 1:** Bug persisted; TELEM1 did not work.
   
2. **Suggestion 2 provided by developers or other personnel:** Check if the telemetry radio uses flow control pins and verify the output of `mavlink status`.
   - **Result of the operation after the user adopted suggestion 2:** Flow control detection was confirmed to be malfunctioning on TELEM1 but working on TELEM3. Developers could replicate the issue using an FTDI cable without flow control.

3. **Suggestion 3 provided by developers or other personnel:** Disable DMA for UART7 (TELEM1).
   - **Result of the operation after the user adopted suggestion 3:** TELEM1 worked correctly without DMA.

4. **Suggestion 4 provided by developers or other personnel:** Add a pull-down resistor configuration to the CTS GPIO pin in the board's initialization file.
   - **Result of the operation after the user adopted suggestion 4:** Bug was resolved with DMA re-enabled and flow control functioning correctly.

5. **Suggestion 5 provided by developers or other personnel:** Submit a pull request (PR) with the fix.
   - **Result of the operation after the user adopted suggestion 5:** User submitted their first PR, and the issue was marked resolved.

**Conclusion:** The root cause of the bug was traced to improper handling of the CTS pin configuration for TELEM1 with DMA and flow control. A pull-down resistor was added to resolve the issue.
