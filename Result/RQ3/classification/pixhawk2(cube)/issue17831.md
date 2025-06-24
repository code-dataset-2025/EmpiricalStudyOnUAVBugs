**Environment where the bug occurred:**

- **Hardware environment:** Pixhawk Cube Orange, Iridium RockBLOCK 9603 module, SD card installed
- **Software environment:** PX4 v1.11.2 and PX4 v1.12.0-beta6
- **Report Time:** July 1, 2021
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**a51d47f

**Steps for bug reproduction:**

- **Step 1:** Make sure the cube is running PX4 v1.11.2, and that an SD card is installed.
- **Step 2:** Power on the Cube using USB.
- **Step 3:** Set "ISBD_CONFIG = GPS 2" without connecting the Iridium Module.
- **Step 4:** Reboot the Pixhawk.
- **Step 5:** It should refuse to connect to QGC and will play the “Error Tune”.
- **Step 6:** There should now be a .log file on the SD card displaying a message related to hard faults.

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** N/A
- **Behavior after step 3:** N/A
- **Behavior after step 4:** The Cube plays an “Error Tune”, indicating a system hard fault.
- **Behavior after step 5:** Unable to connect to QGC, showing a persistent error.
- **Behavior after step 6:** A .log file indicating a hard fault appears on the SD card.

**Expected behavior:**

- **Expected behavior 1:** The Pixhawk should boot and operate normally without requiring the Iridium module to be connected.
- **Expected behavior 2:** It should be able to connect to QGC without errors.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Attempted hardware tests indicating the issue is specific to the GPS2 port; worked around the issue by changing parameters before connecting/disconnecting the Iridium module.
- **URL of the flight log provided by the user:** Not provided.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** @RomanBapst needs to get a patch into master for resolution.
- **Result of the operation after the user adopted suggestion 1:** N/A

- **Suggestion 2 provided by developers or other personnel:** @bkueng provided a reference to issue #17837 for further investigation.
- **Result of the operation after the user adopted suggestion 2:** The user indicated plans to avoid the issue by keeping the Iridium connected.

- **Suggestion 3 provided by developers or other personnel:** Inquiry by @mrpollo about the current status of the issue.
- **Result of the operation after the user adopted suggestion 3:** The issue persisted with manual parameter adjustments to mitigate it.

- **Suggestion 4 provided by developers or other personnel:** @julianoes mentions a resolution in commits 6d7e0a1 and c7fb67e for similar issues.
- **Result of the operation after the user adopted suggestion 4:** The bootloop error appears resolved according to their tests.
