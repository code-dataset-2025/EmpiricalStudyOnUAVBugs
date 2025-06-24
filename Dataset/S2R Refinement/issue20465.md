**Environment where the bug occurred:**

- **Hardware environment:** Fixedwing, CUAV's V5 Autopilot
- **Software environment:** PX4 Autopilot v1.13.0 stable
- **Report Time:** Oct 21, 2022
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**ed558e1

**Steps for bug reproduction:**

- **Step 1:** The plane is flying in any mode.
- **Step 2:** Switch the mode to RTL (Return to Launch).
- **Step 3:** The plane flies back home first.
- **Step 4:** Occasionally, the plane just flies away from the home point in RTL mode even if no further actions are taken.

**Observed behavior by the user:**

- **Behavior after step 1:** Plane continues to fly in its current mode.
- **Behavior after step 2:** Plane switches to RTL mode.
- **Behavior after step 3:** Plane begins to fly back towards the home point.
- **Behavior after step 4:** Plane occasionally flies away from home in RTL mode, without additional user input.

**Expected behavior:**

- **Expected behavior 1:** The plane should accurately return home without deviation in RTL mode.
- **Expected behavior 2:** The plane's RTL altitude setpoint should not change spontaneously.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Reported the issue and described the problem with an occurrence time of around 6:50 in RTL mode. No specific flight log URL is provided in the report.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Comment #20464 was referenced by user `tstastny`. No specific actions or solutions were detailed in the comment.
- **Result of the operation after the user adopted suggestion 1:** No further action is mentioned by the user in response to Comment #20464.
- **Suggestion 2 provided by developers or other personnel:** Comment from user `sfuhrer` on Feb 15, 2023, suggesting the issue should be resolved with changes from #20464 and to reopen if not resolved.
- **Result of the operation after the user adopted suggestion 2:** No re-opening of the issue mentioned, indicating potential resolution or lack of further issues reported by the user.
