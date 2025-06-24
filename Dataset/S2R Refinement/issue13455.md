**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned
- **Software environment:** PX4 Autopilot
- **Report Time:** Nov 13, 2019
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**99a7491

**Steps for bug reproduction:**

- **Step 1:** Launch SITL.
- **Step 2:** Clean mission from vehicle.
- **Step 3:** Set `COM_ARM_MIS_REQ` to 1.
- **Step 4:** Try to arm.

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** N/A
- **Behavior after step 3:** N/A
- **Behavior after step 4:** Arming is possible even without a mission, despite `COM_ARM_MIS_REQ` being set to 1.

**Expected behavior:**

- **Expected behavior 1:** Arming should be denied as no mission is available on the vehicle.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Investigated `vehicle_status_flags.condition_auto_mission_available` and found it was always true; provided link to the relevant code section.
- **URL of the flight log provided by the user:** Not provided.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** @julianoes mentioned in response to the pre-arm check issues.
- **Result of the operation after the user adopted suggestion 1:** N/A
- **Suggestion 2 provided by developers or other personnel:** MaEtUgR could not reproduce the issue anymore, suggested a check within commander and passing the result back.
- **Result of the operation after the user adopted suggestion 2:** The issue seems fixed with the caveat of commander check not properly showing the result, indicating potentially an unrelated issue with result reporting.
