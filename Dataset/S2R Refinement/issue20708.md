> retrieving file (file-CDDaunUTWVdmLjUdLfU91q) ok ✅

**Extracted Bug Report for PX4 Autopilot:**

---

### **Environment where the bug occurred:**
- **Hardware environment:** Holybro Kakute H7
- **Software environment:** PX4 v1.13.2
- **Report Time:** December 6, 2022
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**4f99ac2

---

### **Steps for bug reproduction:**
1. Flash PX4 firmware version v1.13.2 on the Holybro Kakute H7 board.
2. Connect a telemetry unit to TELEM1 and configure the baud rate.
3. Verify that telemetry works perfectly on TELEM1.
4. Assign the telemetry unit to TELEM2 and set the baud rate.
5. Modify `default.pxboard` to:
   - `CONFIG_BOARD_SERIAL_TEL2="/dev/ttyS1"`:
     - Observe that telemetry does not work, as "/dev/ttyS1" is not broken out.
   - `CONFIG_BOARD_SERIAL_TEL2="/dev/ttyS2"`:
     - Telemetry connects to QGC but only receives data from the drone (no data can be sent).

---

### **Observed behavior by the user:**
- **After step 2:** TELEM1 works perfectly with the configured telemetry.
- **After step 4:** 
  - `/dev/ttyS1`: Telemetry does not work, as the port is not broken out.
  - `/dev/ttyS2`: QGroundControl connects, but telemetry only receives data and cannot send commands.

---

### **Expected behavior:**
1. TELEM2 should behave similarly to TELEM1, supporting bidirectional telemetry.
2. The debug console (`/dev/ttyS2`) should be configurable or disabled if interfering with TELEM2 functionality.

---

### **Additional information provided by the user for bug investigation:**
- The user manually enabled TELEM2 in the configuration to test functionality.
- The user suspects a port conflict due to `/dev/ttyS2` being assigned as the debug console and sought ways to disable the debug console to use it as an additional UART for telemetry or external sensors.

---

### **Communication between developers or other personnel and the user:**
1. **Suggestion 1 (j-chen-opteran):** Confirmed that `/dev/ttyS2` is the debug console on Kakute H7 and cannot act as a telemetry port. Recommended not using it for telemetry.
   - **User's response:** User inquired about disabling the NuttX debug console on `/dev/ttyS2` to free the port for external sensors.
2. **Suggestion 2 (j-chen-opteran):** Indicated there is no current method to disable the debug console on Kakute H7, citing similar UART limitations.
   - **User's response:** Acknowledged the limitation and thanked the contributor.
3. **Final Comment (julianoes):** Confirmed closure of the issue.

---

If you need further details or edits, feel free to ask!
