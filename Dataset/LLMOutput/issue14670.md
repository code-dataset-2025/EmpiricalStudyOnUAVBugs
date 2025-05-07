**Environment where the bug occurred:**

- **Hardware environment:** modalai_fc-v1
- **Software environment:** PX4 Autopilot (commit version not mentioned)
- **Report Time:** Apr 14, 2020
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**d5e0a52

**Steps for bug reproduction:**

- **Step 1:** Build a target without the `battery_status` module.
- **Step 2:** Connect to QGroundControl (QGC) and open the Power settings.
- **Step 3:** Observe the "Missing Params:.. BAT_V_DIV .... BAT_A_PER_V" warning.

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** N/A
- **Behavior after step 3:** The message "Missing Params:.. BAT_V_DIV .... BAT_A_PER_V" is displayed in QGC.

**Expected behavior:**

- **Expected behavior 1:** No warning in QGC from these legacy params being missing.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Considered adding the missing params to the `voxlpm` driver but felt it was a hacky solution. Mentioned a related PR for context (`c201906`).
- **URL of the flight log provided by the user:** Not provided.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `julianoes` suggested adding the params to the `voxlpm` driver for backwards compatibility and provided a link to where deprecated params are synced with new ones for reference.
- **Result of the operation after the user adopted suggestion 1:** The user (`modaltb`) acknowledged the suggestion and indicated they could proceed with the approach provided.
