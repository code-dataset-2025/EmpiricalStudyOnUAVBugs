**Environment where the bug occurred:**

- **Hardware environment:** Pixhawk 1 (original 3DR)
- **Software environment:** Firmware: px4_fmuv2_default 1.11.0, also tested (same error) on 1.9.0
- **Report Time:** Sep 2, 2020
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**24125b3

**Steps for bug reproduction:**

- **Step 1:** Power the Pixhawk with the USB.
- **Step 2:** Wait for the LED to be blue breathing.
- **Step 3:** Wait an additional 10 seconds.
- **Step 4:** Try to connect Mavros, QGc, or `cat /dev/ttyACM0`.
- **Step 5:** When connecting, a few messages are received.
- **Step 6:** The connection hangs: No message can be sent or received.

**Observed behavior by the user:**

- **Behavior after step 4:** Few messages are received.
- **Behavior after step 5:** The connection hangs; no message can be sent or received.

**Expected behavior:**

- **Expected behavior 1:** You can wait any time before connecting.
- **Expected behavior 2:** The connection is successful and can be used for any time.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Replicated the behavior using libusb1.0 instead of the kernel usb-cdc-acm driver.
- **URL of the flight log provided by the user:** [Example log](https://review.px4.io/plot_app?log=85f3ab21-074b-4a19-9baa-820d606824c2)

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Instrument the mavlink module and debug through the serial console (provided by `dagar`).
- **Result of the operation after the user adopted suggestion 1:** Unable to adopt due to lack of a serial cable.
- **Suggestion 2 provided by developers or other personnel:** Possible solution - \#16180 (suggested by `dagar`).
- **Result of the operation after the user adopted suggestion 2:** User indicated they would test the solution, and later expressed intent to close the report temporarily.
