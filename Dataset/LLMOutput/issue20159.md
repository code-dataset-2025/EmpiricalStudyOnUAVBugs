**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned
- **Software environment:** PX4 Autopilot v1.13
- **Report Time:** Sep 5, 2022
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**92fbd86

**Steps for bug reproduction:**

- **Step 1:** Start SITL.
- **Step 2:** Upload a mission with a speed change.
- **Step 3:** After the speed change, press in the map to do a Go-to.
- **Step 4:** Check the speed.

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** N/A
- **Behavior after step 3:** N/A
- **Behavior after step 4:** The last set cruise speed stays and is applied to Hold and “Go to/reposition” modes.

**Expected behavior:**

- **Expected behavior 1:** The speed should reset once out of mission mode.
- **Expected behavior 2:** The speed should be re-applied when going back into mission mode.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Not specifically mentioned.
- **URL of the flight log provided by the user:** Not provided.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Discussion around resetting speed on mode change and differentiation of DO_CHANGE_SPEED between mission and command.
- **Suggestion 2 provided by developers or other personnel:** The speed setting logic should not persist across different modes, but should be consistent within the same mode.
- **Suggestion 3 provided by developers or other personnel:** Consider adding a parameter to revert to default in missions.
- **Result of the operation after the user adopted suggestions:** The issue was fixed by commits #21414 and #21503, indicating the changes were implemented based on the discussion.

