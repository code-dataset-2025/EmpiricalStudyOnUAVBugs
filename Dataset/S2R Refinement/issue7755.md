**Environment where the bug occurred:**

- **Hardware environment:** PixRacer
- **Software environment:** PX4 Autopilot (version not mentioned)
- **Report Time:** Aug 9, 2017
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**aa9023b

**Steps for bug reproduction:**

- **Step 1:** Flash current master.
- **Step 2:** Reset all parameters.
- **Step 3:** On the console, execute the following commands:
  ```bash
  param set MNT_MODE_IN 3
  param set MNT_MODE_OUT 1
  vmount start
  ```

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** N/A
- **Behavior after step 3:** The system freezes; console via debug port is no longer responsive, QGroundControl (QGC) loses connection, and the PixRacer stops flashing.

**Expected behavior:**

- **Expected behavior 1:** The PixRacer should not freeze when 'vmount' is used with the specified settings.
- **Expected behavior 2:** The mavlink inputs and outputs should operate without creating a loop that causes a freeze.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** The user suspected a loop between the 'vmount' input and output via 'vehicle_command' and attempted modifying InputMavlinkCmdMount to skip processing own messages by checking system and component IDs.
- **URL of the flight log provided by the user:** Not provided.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `bkueng` acknowledged the issue and mentioned it was easily reproducible thanks to the user's steps.
- **Result of the operation after the user adopted suggestion 1:** N/A (the suggestion was acknowledgment and intention to investigate).
- **Suggestion 2 provided by developers or other personnel:** Developer `LorenzMeier` stated that the issue was fixed.
- **Result of the operation after the user adopted suggestion 2:** N/A (the result of adopting a fixed solution is not detailed in comments).
