**Environment where the bug occurred:**

- **Hardware environment:** CUAV V6x flight controller
- **Software environment:** PX4 version v1.13, QGroundControl (QGC) version V4.2.6
- **Report Time:** May 29, 2023
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**70178b6

**Steps for bug reproduction:**

- **Step 1:** Follow the official ESC calibration document with UAVCAN power module.

**Observed behavior by the user:**

- **Behavior after step 1:** ESC calibration results in failure.

**Expected behavior:**

- **Expected behavior 1:** ESC calibration completes successfully.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Used the actuator testing panel to perform manual ESC calibration by following a set of steps involving disconnecting and connecting the battery and adjusting motor sliders.
- **URL of the flight log provided by the user:** Not provided.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Sidzeppelin95 suggested performing manual calibration using UAVCAN GUI Tool or Mavlink console, ensuring proper connections and firmware updates, and referring to specific ESC calibration methods from the manufacturer's guidance.

- **Result of the operation after the user adopted suggestion 1:** TianmingLi manually calibrated the ESCs using the actuator testing panel and shared steps involved in the process.

- **Suggestion 2 provided by developers or other personnel:** Julianoes questioned the need for ESC calibration for UAVCAN ESCs, suggesting that only min/max parameters and bench tests may be necessary.

- **Result of the operation after the user adopted suggestion 2:** N/A, as this suggestion was more of a clarification.

- **Suggestion 3 provided by other personnel (ghavan0517):** Asked for confirmation on calibration success and what to do if motor information varies.

- **Result of the operation after the user adopted suggestion 3:** TianmingLi provided a method to check calibration success using the Mavlink console to verify PWM outputs.

