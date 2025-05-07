**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned
- **Software environment:** Not explicitly mentioned
- **Report Time:** Feb 25, 2017
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**507f48a

**Steps for bug reproduction:**

- **Step 1:** Takeoff.
- **Step 2:** Fly to another location.
- **Step 3:** Start RTL (Return-to-Launch).
- **Step 4:** Pause the drone.
- **Step 5:** Fly to another location.
- **Step 6:** Start RTL again.

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** N/A
- **Behavior after step 3:** The drone follows the sequence of RTL steps: climbing (RTL_STATE_CLIMB), returning home (RTL_STATE_RETURN), and descending (RTL_STATE_DESCEND).
- **Behavior after step 4:** The drone pauses.
- **Behavior after step 5:** N/A
- **Behavior after step 6:** Instead of starting RTL from the beginning (step 4), the drone continues from its last state (in this case, descending).

**Expected behavior:**

- **Expected behavior 1:** When RTL is activated, it should start from the beginning of the RTL sequence regardless of previous state.
- **Expected behavior 2:** Consistency in the RTL state upon reactivation, especially critical if the mode proceeds to RTL_STATE_LAND.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Suggested that a call to `set_can_loiter_at_sp(true)` might be necessary at certain points in the code.
- **URL of the flight log provided by the user:** Not provided.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `dagar` acknowledged the report and mentioned they would look into it.
- **Result of the operation after the user adopted suggestion 1:** N/A (no specific operation suggested beyond acknowledgment).
- **Suggestion 2 provided by developers or other personnel:** Developer `LorenzMeier` mentioned they have a fix coming.
- **Result of the operation after the user adopted suggestion 2:** Fix referenced in issue #6670.
