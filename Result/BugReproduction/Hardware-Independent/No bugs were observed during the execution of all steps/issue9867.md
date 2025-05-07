**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned
- **Software environment:** Not explicitly mentioned
- **Report Time:** Jul 9, 2018
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**33f7318

**Steps for bug reproduction:**

- **Step 1:** Monitor message GLOBAL_POSITION_INT.
- **Step 2:** Rotate vehicle 360 degrees.
- **Step 3:** See GLOBAL_POSITION_INT.hdg overflowing.

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** N/A
- **Behavior after step 3:** GLOBAL_POSITION_INT.hdg overflows instead of wrapping correctly.

**Expected behavior:**

- **Expected behavior 1:** To see values in the GLOBAL_POSITION_INT.hdg field in the range of 0..35999.
- **Expected behavior 2:** UINT16_MAX for unknown heading values.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** User suggested that the line of code should wrap yaw between zero and 360 degrees as it did in previous versions.
- **URL of the flight log provided by the user:** Not provided.

**Communication between developers or other personnel and the user:**

No specific suggestions or communication entries provided in the document.
