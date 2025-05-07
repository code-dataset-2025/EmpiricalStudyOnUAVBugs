> retrieving file (file-Nbz4xXispJH4k6VAkD51Bt) ok ✅

**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned
- **Software environment:** PX4 1.14.0 beta 2, MavSDK 1.4.5, ARK GPS RTK CAN version
- **Report Time:** May 17, 2023
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**599a66c

**Steps for bug reproduction:**

- **Step 1:** Enable configuration of UAVCAN_SUB_RTCM (from FC settings).
- **Step 2:** Enable configuration of CANNODE_SUB_RTCM (from CAN device settings).
- **Step 3:** Establish a MavSDK drone connection to enable communication between the companion computer and the flight controller.
- **Step 4:** Obtain the RTCM stream data from an NTRIP client of your choice.
- **Step 5:** Send the RTCM data stream to the MavSDK client using the `send_rtcm_data` method.
- **Step 6:** Check if the GPS status updates to RTK FIX.
- **Step 7:** Observe the `rtcm_msg_used` value from the ARK RTK GPS module.

**Observed behavior by the user:**

- The RTCM data appears to be injected towards the GPS but does not result in an RTK FIX.
- The GPS status remains at a maximum of 3D DGPS Lock.
- The `rtcm_crc_failed` flag is `false`, but the `rtcm_msg_used` value remains `0` instead of the expected `2`.

**Expected behavior:**

- The GPS status should reach RTK FIX.
- The `rtcm_msg_used` value should correctly reflect the processed RTCM messages (expected value: `2`).

**Additional information provided by the user for bug investigation:**

- The user attempted to bypass the MAVSDK and directly forward RTCM data to the GPS debug port in bypass mode. This approach resulted in immediate RTK FIX, suggesting the issue may lie within MAVSDK or PX4 data handling.
- The user provided a ZIP file (`TestPythons.zip`) for replicating the issue.
- The user suspects possible encoding issues or improper data handling in the `rtcm_inject` or `send_rtcm_data` method of the MAVSDK Python plugin.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 by `dagar` (May 30, 2023):** Requested confirmation if this setup had previously worked. The user speculated that the issue might be caused by encoding or timing in the MAVSDK's RTK plugin.
- **Suggestion 2 by `julianoes` (May 30, 2023):** Suspected type conversion issues in the MAVSDK Python plugin. Confirmed this scenario had not been tested.
- **Result of the operation after suggestions:** No specific results provided by the user.
- **Resolution:** `julianoes` (June 6, 2023) confirmed the issue was resolved in `mavsdk_server v1.4.16` and `MAVSDK-Python v1.4.8`.

If further clarification is needed, feel free to reach out!
