**Environment where the bug occurred:**

- **Hardware environment:** Any drone with AM32 ESC (possibly also BLHeli, but not personally tested).
- **Software environment:** Not explicitly mentioned.
- **Report Time:** Jun 1, 2022.
- **PX4 Autopilot commit version:** Not mentioned.
- **last commit before the reporting time:**c19e747

**Steps for bug reproduction:**

- **Step 1:** Use commands `dshot reverse -m 1` and then `dshot save -m 1` as per PX4 motor direction reversal instructions.
- **Step 2:** Try testing motor direction - the motor will be reversed properly.
- **Step 3:** Reboot the drone (including its ESC).
- **Step 4:** Try testing motor direction again.

**Observed behavior by the user:**

- **Behavior after step 1:** Motor direction is reversed properly.
- **Behavior after step 2:** N/A
- **Behavior after step 3:** Upon rebooting, the motor reverts to its original direction rather than being reversed as expected.
- **Behavior after step 4:** The motor does not maintain the reversed direction.

**Expected behavior:**

- **Expected behavior 1:** The motor should remain with the set direction (reversed or non-reversed) persistent across reboots.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Provided references to AM32 implementation and forum discussion for additional context on proper DShot command usage.
- **URL of the flight log provided by the user:** Not provided.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `bkueng` acknowledged the issue, mentioned the lack of formal specifications, and suggested sending a PR to change the command.
- **Result of the operation after the user adopted suggestion 1:** N/A (there's no update on whether a PR was sent based on this document).
