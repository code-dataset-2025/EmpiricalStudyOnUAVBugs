**Environment where the bug occurred:**

- **Hardware environment:** MRO Control Zero H7 OEM
- **Software environment:** PX4 Autopilot version 1.13.2 stable (master as well)
- **Report Time:** Mar 3, 2023
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**7edce94

**Steps for bug reproduction:**

- **Step 1:** Turn on Flight Controller (FC).
- **Step 2:** Set up GPS1 serial port as a mavlink port.
- **Step 3:** Set `GPS_1_CONFIG` to disabled.
- **Step 4:** Set `MAV_1_CONFIG` to GPS1.
- **Step 5:** Set `MAV_1_MODE` to Onboard (as default).
- **Step 6:** Set `SER_GPS1_BAUD` to 57600 8N1.
- **Step 7:** Reboot whenever needed to get these parameters set.
- **Step 8:** Verify mavlink instance and streams are started via the mavlink console: `mavlink status` and `mavlink status streams`.

**Observed behavior by the user:**

- **Behavior after step 1-7:** No data comes out on the mavlink TX pin; the TX pin shows zero activity.
- **Behavior after step 8:** Active mavlink instance and streams are listed, but still nothing coming out of the TX port.

**Expected behavior:**

- **Expected behavior 1:** The TX pin should transmit data as expected when configured.
- **Expected behavior 2:** Mavlink should operate normally with data output observable on the TX pin.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Used an oscilloscope and microcontroller to verify no data on the TX pin, ran `mavlink stop -d /dev/ttyS2` and `mavlink start -d /dev/ttyS2` to get the port working, and noted the TX pin issue might be due to misconfiguration of the PA0 pin.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `lgarciaos` suggested using another port and verified the behavior on reference boards, mentioning it could be due to some startup misconfiguration.
- **Result of the operation after the user adopted suggestion 1:** User `carlosmurphyDragoon` mentioned the workarounds work fine and highlighted the usage of UART4 due to custom board design.
