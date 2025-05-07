**Environment where the bug occurred:**

- **Hardware environment:** Holybro Pixhawk 6C
- **Software environment:** PX4 Autopilot with firmware version 1.13.2
- **Report Time:** Feb 23, 2023
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**a1efafc

**Steps for bug reproduction:**

- **Step 1:** Set `COM_RC_IN_MODE` to 1 without any RC input.
- **Step 2:** Try to arm the vehicle.

**Observed behavior by the user:**

- **Behavior after step 1:** QGroundControl stops complaining about the radio not being configured (icon turns from red to gray).
- **Behavior after step 2:** A "Critical: Arming Denied! manual control lost" message is received.

**Expected behavior:**

- **Expected behavior 1:** The RC signal lost check should be fully disabled after setting the parameter `COM_RC_IN_MODE` to 1.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Identified a potential trigger for the issue at line 76 in `preArmCheck.cpp`. Mentioned the application uses the Pixhawk primarily as a logger with no actuation capabilities, utilizing arm/disarm commands to start and stop SD logging.
- **URL of the flight log provided by the user:** Not provided.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** @MaEtUgR mentioned that the issue was fixed for version 1.14 with #20695 and reviewed the changes first introduced in 1.13 regarding stick input handling.
- **Result of the operation after the user adopted suggestion 1:** N/A (suggestion was a clarification of the changes rather than an actionable operation).
  
- **Suggestion 2 provided by developers or other personnel:** Multiple solutions were proposed: manually starting and stopping logging using MAVLink commands, disabling stick input with `COM_RC_IN_MODE` set to 4 and arming in a mode that satisfies other requirements, and forcibly arming using MAVLink commands with a force flag.
- **Result of the operation after the user adopted suggestion 2:** The issue was considered closed, indicating that the suggestions resolved the user's concerns or clarified the expected behavior.
