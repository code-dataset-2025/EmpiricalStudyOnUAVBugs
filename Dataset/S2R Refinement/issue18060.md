**Environment where the bug occurred:**

- **Hardware environment:** Pixhawk4 mini, UAVCAN airspeed sensor (digital), and GPS from Holybro. One analog airspeed sensor from Holybro.
- **Software environment:** PX4 Autopilot v1.12.1 and v1.11.3
- **Report Time:** Aug 12, 2021
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**72bc864

**Steps for bug reproduction:**

1. Pixhawk4 mini firmware upgrade to v1.12.1 (tried px4_fmu-v5_fixedwing.px4 and px4_fmu-v5_default.px4).
2. Have an airspeed sensor connected via UAVCAN.
3. Press calibrate and observe the message "No airspeed sensor found."

**Observed behavior by the user:**

- **Behavior after step 1:** Firmware upgrade completed successfully.
- **Behavior after step 2:** Digital UAVCAN airspeed sensor connected but not calibrated.
- **Behavior after step 3:** Error message "No airspeed sensor found" appears.

**Expected behavior:**

1. Ability to calibrate UAVCAN airspeed sensor.
2. Error-free operation similar to version v1.11.3 where sensor calibration was successful.

**Additional information provided by the user for bug investigation:**

- The issue becomes apparent only after the firmware update to v1.12.1.
- The user attempted rolling back to stable release v1.11.3 to test the calibration, which functioned without issues.

**Communication between developers or other personnel and the user:**

1. **Suggestion 1 provided by developers or other personnel:** Developer `dagar` asked if the user was getting airspeed directly from UAVCAN or differential pressure, suggesting capturing outputs of `uavcan status`, `listener airspeed`, and `listener differential_pressure`.
   
   - **Result of the operation after the user adopted Suggestion 1:** User provided the status and listener information showing differential pressure was indeed being received, and confirmed the airspeed is calculated from this data.

2. **Suggestion 2 provided by developers or other personnel:** Developer `dagar` found that calibration is not being handled by UAVCAN differential pressure and suggested checking pull request \#18145.

   - **Result of the operation after the user adopted Suggestion 2:** No specific feedback from the user regarding testing \#18145, but it implied resolution or pathway for further troubleshooting with mentioned updates.
