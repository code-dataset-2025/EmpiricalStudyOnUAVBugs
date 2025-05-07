**Environment where the bug occurred:**

- **Hardware environment:** MindPX or MindRacer
- **Software environment:** QGroundControl (QGC) on macOS Mojave (10.14.x)
- **Report Time:** Apr 24, 2019
- **PX4 Autopilot commit version:** not mentioned
- **last commit before the reporting time:**c95394f

**Steps for bug reproduction:**

- **Step 1:** Use a Mac computer (10.14.x/Mojave), launch QGC.
- **Step 2:** Connect MindPX (or MindRacer) via USB.
- **Step 3:** Observe the connection status in QGC.

**Observed behavior by the user:**
- **Behavior after step 1:** QGC launches without issues.
- **Behavior after step 2:** A cu/tty device is created under /dev, and the correct port is identified and opened.
- **Behavior after step 3:** No mavlink message bytes are received on the QGC side, resulting in a failure to connect automatically.

**Expected behavior:**
- **Expected behavior 1:** The system should auto-connect to QGC on a Mac computer, similar to its behavior on Windows.
- **Expected behavior 2:** Connection should be stable as in previous versions like v1.8.2 on macOS/QGC.

**Additional information provided by the user for bug investigation:**
- **Actions taken by the user:** Tested the connection on version 1.9.2 and noted the same issue. Provided console logs to developers for inspection.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `julianoes` inquired if the issue was the same as another issue #12201.
- **Result of the operation after the user adopted suggestion 1:** User `airmind` confirmed the issue was different.
  
- **Suggestion 2 provided by developers or other personnel:** Developer `davids5` requested dmesg output from Mac when the FMU is connected to ascertain connection details.
- **Result of the operation after the user adopted suggestion 2:** User `airmind` provided dmesg log outputs for analysis.

- **Suggestion 3 provided by developers or other personnel:** `davids5` suggested checking USB device information using the System Report on macOS.
- **Result of the operation after the user adopted suggestion 3:** User `airmind` provided additional information, noted inconsistent behavior with Pixhawk hardware.

- **Suggestion 4 provided by developers or other personnel:** `airmind` offered to provide hardware to developer `davids5` for further testing.
- **Result of the operation after the user adopted suggestion 4:** The offer was considered but not acted upon due to existing resources on the developer side.
