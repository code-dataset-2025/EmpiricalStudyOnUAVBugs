**Environment where the bug occurred:**

- **Hardware environment:** MRO X2.1-777 flight controller, Ublox M8 GPS module.
- **Software environment:** PX4 Autopilot, commit version: Not mentioned.
- **Report Time:** Aug 21, 2020.
- **PX4 Autopilot commit version:** Not mentioned.
- **last commit before the reporting time:**f62662e

**Steps for bug reproduction:**

- **Step 1:** Boot the flight controller (FC).
- **Step 2:** Observe that Spektrum 3.3V is initially present during the boot process but disappears later.
- **Step 3:** Verify that the receiver is not detected, even when 3.3V is supplied externally.
- **Step 4:** Connect the GPS module via UART (TX initialization observed) and verify the FC does not detect the GPS module on UART RX at any baud rate.

**Observed behavior by the user:**

- **Behavior after step 1:** No 3.3V supply to Spektrum Satellite.
- **Behavior after step 2:** RC receiver is not detected.
- **Behavior after step 3:** GPS module initialization commands are sent by the FC, but the module is not detected on the UART RX side.
- **Behavior after step 4:** GPS external I2C magnetometer is detected and functions correctly, but no communication occurs via UART RX.

**Expected behavior:**

- **Expected behavior 1:** RC receiver should function and display channels.
- **Expected behavior 2:** GPS should work and be detected on one of the FC's UARTs.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:**
  1. Attempted flashing firmware to the IO unit using various methods (safety button, commands).
  2. Measured GPS UART TX initialization signals using an oscilloscope.
  3. Tested GPS modules on other hardware (e.g., PixRacer), confirming correct functionality.
  4. Disabled RX DMA for UART4 in the configuration, which allowed GPS to function.
  5. Performed further tests with different UART ports, firmware versions, and bootloader flashing methods.
  6. Used external SWD flashing to successfully update IO firmware, resolving most issues except GPS functionality on UART RX.
  7. Verified telemetry and MAVLink functioning on the same UART ports where GPS failed.
- **URL of the flight log provided by the user:** Not provided.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Review configuration files for UART setup in the firmware (links to specific lines in the PX4 source code provided).
  - **Result:** The user further investigated and identified RX DMA as a key factor affecting GPS detection.
- **Suggestion 2 provided by developers or other personnel:** Inquire about measuring transmission errors.
  - **Result:** The user provided details on telemetry packet loss observed during operations but acknowledged the lack of objective measurement methods.
- **Suggestion 3 provided by developers or other personnel:** Re-test the issue with the latest PX4 master branch after safety checks were improved.
  - **Result:** The user confirmed that issues with GPS detection persisted, and IO bootloader compatibility remained problematic.
- **Suggestion 4 provided by developers or other personnel:** Investigate using SWD flashing to resolve firmware issues.
  - **Result:** The user successfully flashed the IO firmware via SWD but identified additional configuration problems related to RX DMA and UART performance.

**Additional user findings and remarks:**

- GPS detection only works with RX DMA disabled.
- UARTs function perfectly for telemetry but fail for GPS RX communication.
- IO firmware updates via the FMU are unreliable; manual SWD flashing is necessary.
- Persistent issues with UART DMA, clock frequency, and baud rate negotiation for GPS communication.
- The board hardware appears functional, as all issues are software-related.

**Current status:**

- Most board functions are stable and operational, except for:
  - UART performance issues with GPS when RX DMA is active.
  - IO firmware updates from the FMU.
  - Errors related to RX DMA and UART initialization.  

