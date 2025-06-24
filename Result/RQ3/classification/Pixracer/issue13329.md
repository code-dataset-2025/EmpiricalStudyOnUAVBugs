**Environment where the bug occurred:**

- **Hardware environment:** Drotek Pixhawk 3 Pro or a Pixracer
- **Software environment:** PX4 Autopilot, version 1.10.0, git hash a6a88774637c745ee069c6482a79b7d4b3cc8b12
- **Report Time:** Oct 31, 2019
- **PX4 Autopilot commit version:** a6a8877

**Steps for bug reproduction:**

- **Step 1:** Connect CUAV GPS V5 magnetometer to a Pixracer.
- **Step 2:** Check for the device using the command `listener sensor_mag`.

**Observed behavior by the user:**

- **Behavior after step 1:** Magnetometer does not get detected.
- **Behavior after step 2:** `listener sensor_mag` shows no detection of the device.

**Expected behavior:**

- **Expected behavior 1:** Magnetometer should be detected when connected to the Pixracer.
- **Expected behavior 2:** The `listener sensor_mag` command should list the connected magnetometer.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Attempted to use `i2cdetect` to find the device with no success. Checked for the device on both v1.10.0 and v1.9.2.
- **URL of the flight log provided by the user:** Not provided.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Check GPS/Compass interface connection and see if there might be compatibility issues with Pixracer.
- **Result of the operation after the user adopted suggestion 1:** The user discovered that the pinouts order was incorrect.

- **Suggestion 2 provided by developers or other personnel:** Inspect the connection and wiring, referencing the CUAV V5+ documentation.
- **Result of the operation after the user adopted suggestion 2:** User corrected the wiring. GPS started working, but unfortunately, the magnetometer was potentially destroyed by incorrect voltage.

- **Suggestion 3 provided by developers or other personnel:** Recommended switching from M8N GPS to NEO GPS due to discontinuation.
- **Result of the operation after the user adopted suggestion 3:** The user acknowledged the recommendation and indicated understanding of future product compatibility improvements.
