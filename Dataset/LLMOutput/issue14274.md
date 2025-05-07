Here’s the extracted and formatted bug report based on the provided document:

---

# Basic Information:
### Title: Stm32H7 hard fault when SPI2 and I2C4 work together #14274
### Issue status: Closed
### Author: ShiauweiZhao
### Issue open time: Mar 2, 2020
### Fixed by: Not explicitly mentioned

# Report
### Report author: ShiauweiZhao
### Report Time: Mar 2, 2020
### Report Content:
**Describe the bug:**
The reporter encountered a hard fault on STM32H7 hardware when running drivers for the barometer (via the SPI2 interface) and magnetometer IST8308 (via I2C3 and I2C4 interfaces) in the work queue. The fault occurs during SPI reads when called in the work queue transfer.

**To Reproduce:**
Steps were not explicitly detailed but involve configuring STM32H7 hardware with the stated interfaces and running both drivers simultaneously.

**Expected behavior:**
- Both drivers (barometer on SPI2 and magnetometer on I2C3/I2C4) should function correctly without triggering a hard fault.

**Log Files and Screenshots:**
- Debug log and fault details:
  ```bash
  (gdb) info line *0x080d84b9
  Line 134 of "../../src/lib/drivers/device/nuttx/SPI.cpp"
     starts at address 0x80d84b4 <device::SPI::transfer(unsigned char*, unsigned char*, unsigned int)+18>
     and ends at 0x80d84bc <device::SPI::transfer(unsigned char*, unsigned char*, unsigned int)+26>.
  (gdb) info line *0x080d84fe
  Line 147 of "../../src/lib/drivers/device/nuttx/SPI.cpp"
     starts at address 0x80d84fa <device::SPI::transfer(unsigned char*, unsigned char*, unsigned int)+88>
     and ends at 0x80d8502 <device::SPI::transfer(unsigned char*, unsigned char*, unsigned int)+96>.
  ```
- Fault log, ELF file, and debug UART console are referenced but not provided in full.

---

# Environment where the bug occurred:
- **Hardware environment:** STM32H7 with barometer (SPI2), internal magnetometer IST8308 (I2C4), and external magnetometer IST8308 (I2C3)
- **Software environment:** PX4 Autopilot (commit version not mentioned)
- **Report Time:** Mar 2, 2020
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**862cb20

---

# Steps for bug reproduction:
1. Set up STM32H7 hardware with the following configuration:
   - Barometer connected via SPI2
   - External magnetometer IST8308 via I2C3
   - Internal magnetometer IST8308 via I2C4
2. Run both barometer and magnetometer drivers in the work queue.
3. Observe the system behavior.

---

# Observed behavior by the user:
- **Behavior after step 1:** N/A
- **Behavior after step 2:** N/A
- **Behavior after step 3:** A hard fault occurs during SPI reads in the work queue transfer.

---

# Expected behavior:
1. The barometer driver (SPI2) and magnetometer drivers (I2C3 and I2C4) should function correctly in the work queue without conflicts.
2. The system should not generate a hard fault during SPI reads or other operations.

---

# Additional information provided by the user for bug investigation:
- **Actions taken by the user:**
  - Investigated the hard fault using the debugger and identified the fault occurring in the SPI transfer function.
  - Suggested sharing their code if necessary.
- **URL of the flight log provided by the user:** Not provided.

---

# Communication between developers or other personnel and the user:
1. **Suggestion 1 provided by developers or other personnel:**
   - `julianoes`: Asked how to reproduce the issue to facilitate fixing it.
   - **Result of the operation after the user adopted suggestion 1:** No specific user action was noted in response to this comment.

2. **Suggestion 2 provided by developers or other personnel:**
   - `dagar`: Recommended creating pull requests for the IST8308 magnetometer and tcbp001ta barometer to enable further review and upstream maintenance.
   - Highlighted that there should be no overlap or conflicts since each work queue operates in a separate thread.
   - **Result of the operation after the user adopted suggestion 2:** The user created PR #14286 and noted that the issue was resolved in the master branch by Apr 24, 2020.

---

This summarizes the bug report and related interactions. Let me know if further details are required!
