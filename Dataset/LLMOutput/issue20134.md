**Environment where the bug occurred:**

- **Hardware environment:** DroneCAN F9P RTK
- **Software environment:** PX4 Autopilot (specific commit version not mentioned)
- **Report Time:** Aug 31, 2022
- **PX4 Autopilot commit version:** not mentioned
- **last commit before the reporting time:**75f6f22

**Steps for bug reproduction:**

- **Step 1:** Use a DroneCAN F9P RTK to attempt to get RTK GPS Lock.
- **Step 2:** Use an i2c F9P RTK to witness a proper RTK GPS Lock.

**Observed behavior by the user:**

- **Behavior after step 1:** Unable to get RTK GPS Lock with DroneCAN F9P RTK.
- **Behavior after step 2:** No issue obtaining RTK GPS Lock with i2c F9P RTK.

**Expected behavior:**

- **Expected behavior 1:** PX4 should send RTCMStream DroneCAN messages upon receiving GPS_RTCM_DATA MAVLink messages.
- **Expected behavior 2:** Achieve RTK GPS Lock when using a DroneCAN F9P RTK, similar to the functionality with an i2c F9P RTK.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Conducting tests with different RTK configurations and using the DroneCAN GUI tool.
- **URL of the flight log provided by the user:** Not provided.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Enable UAVCAN_PUB_RTCM parameter as mentioned by AlexKlimaj.
- **Result of the operation after the user adopted suggestion 1:** Not specified in the communication; however, subsequent comments suggest continued issues.
- **Suggestion 2 provided by developers or other personnel:** AlexKlimaj mentions that UAVCAN_PUB_RTCM is broken in the main branch and suggests looking at fix \#20056.
- **Result of the operation after the user adopted suggestion 2:** Issue was fixed with \#20056 according to AlexKlimaj.
