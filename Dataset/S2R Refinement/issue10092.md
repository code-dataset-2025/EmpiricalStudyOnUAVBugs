**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned
- **Software environment:** Not explicitly mentioned
- **Report Time:** Jul 30, 2018
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**99fd1f7

**Steps for bug reproduction:**

- **Step 1:** Disconnect iridium device from Pixhawk.<font color='red'>需要iridium device（铱星设备）指的是利用Iridium（铱星）卫星通信系统进行通信的硬件设备。以及未提及版本的pixhawk</font>
- **Step 2:** Set parameter `SYS_COMPANION` to "19,200 kbps Iridium".
- **Step 3:** Reboot the device.

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** N/A
- **Behavior after step 3:** The system fails during reboot when `SYS_COMPANION` is set to "19,200 kbps Iridium".

**Expected behavior:**

- **Expected behavior 1:** System should handle the absence of the iridium device and boot without crashing.
- **Expected behavior 2:** The parameter setting should enable relevant communication without requiring manual configuration steps that involve `extras.txt`.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Provided initial reproduction steps.
- **URL of the flight log provided by the user:** The logs were mentioned as being provided later by another user (researcher3) in the discussion, but no specific URL was given.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** LorenzMeier suggested a workaround in ticket #10095 to get out of the issue.
- **Result of the operation after the user adopted suggestion 1:** Not explicitly mentioned following the initial suggestion.

- **Suggestion 2 provided by developers or other personnel:** acfloria explained manual steps to start the iridium driver before the Mavlink instance, suggesting modifications in `extras.txt`. Emphasized the need for a wait time between driver startup and Mavlink instance initialization.
- **Result of the operation after the user adopted suggestion 2:** Improved understanding of configuration, shared by researcher3. Adjustments were made to allow successful connection and reboot.

- **Suggestion 3 provided by developers or other personnel:** acfloria advised using the master branch for latest fixes, including timing adjustments for driver startup relative to Mavlink instance.
- **Result of the operation after the user adopted suggestion 3:** researcher3 reported success in recognizing Pixhawk 4 by QGC and performing a firmware update.

- **Suggestion 4 provided by developers or other personnel:** acfloria confirmed that baud rate for Iridium communication should be 115200, not 19200, which wasn’t supported.
- **Result of the operation after the user adopted suggestion 4:** researcher3 queried about the effort required to support 19200, highlighting that it wasn't directly supported in the dropdown setting.
