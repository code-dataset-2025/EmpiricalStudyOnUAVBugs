**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned
- **Software environment:** PX4 Autopilot with commit not mentioned
- **Report Time:** Jun 5, 2019
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**79eb74b

**Steps for bug reproduction:**

- **Step 1:** Execute `make px4_sitl jmavsim`.

**Observed behavior by the user:**

- **Behavior after step 1:** ERROR "[land_detector] Timed out while waiting for thread to start".

**Expected behavior:**

- **Expected behavior 1:** No timeout error when starting the land detector.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** User mentioned encountering an error and asked for suggestions. Also, they tagged developer `@dagar` for insights.
- **URL of the flight log provided by the user:** Not provided.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `dagar` asked if the issue occurred recently as in today or earlier.
- **Result of the operation after the user adopted suggestion 1:** No direct results mentioned.
- **Suggestion 2 provided by developers or other personnel:** Developer `dagar` suggested trying PR #12196.
- **Result of the operation after the user adopted suggestion 2:** Not directly mentioned in provided document.
- **Suggestion 3 provided by developers or other personnel:** Developer `mcsauder` suggested a potential fix in PR #12209 related to a schedule call.
- **Result of the operation after the user adopted suggestion 3:** No direct results mentioned.
- **Further suggestions:** Developer `mcsauder` offered changes to the ScheduleOnInterval() to ScheduleNow() and confirmed flight testing the fix in PR #12209.
- **Result of the operation after the user adopted further suggestions:** No direct results mentioned, though testing was confirmed.
