**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned
- **Software environment:** PX4 Autopilot (version not mentioned)
- **Report Time:** Dec 5, 2019
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**5cbcf60

**Steps for bug reproduction:**

- **Step 1:** Plan a mission in SITL (Software In The Loop) with a landing at the end and a long distance between the landing and the prior waypoint.
- **Step 2:** Trigger Return-To-Launch (RTL) when the 2nd to last waypoint is already reached.

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** The VTOL immediately transitions to multicopter mode instead of proceeding in fixed-wing mode until close to landing.

**Expected behavior:**

- **Expected behavior 1:** VTOL should continue flying in fixed-wing mode until it is close to home/land.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** The issue report describes the specific scenario in which the unexpected behavior occurs and distinguishes it from missions planned using recommended procedures with a `DO_LAND_START` marker, but no specific actions to troubleshoot were mentioned.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `julianoes` noted that the issue only occurs with `RTL_TYPE = 1`, suggesting other RTL types may not reproduce the issue.
- **Result of the operation after the user adopted suggestion 1:** User `sfuhrer` confirmed `RTL_TYPE = 1` is indeed the default RTL procedure for VTOLs, and therefore the suggestion did not resolve the issue. 
- **Additional comments:** The issue was automatically marked as stale and closed later due to inactivity, as seen in comments by `stale`.
