**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned
- **Software environment:** PX4 Autopilot on v1.12 and master
- **Report Time:** Sep 21, 2021
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**cf5da66

**Steps for bug reproduction:**

- **Step 1:** Reproducible on SITL using PX4 v1.12 and master versions.
- **Step 2:** Use the command `make px4_sitl gazebo_standard_vtol`.
- **Step 3:** Load the mission provided in `bad RTL.zip`.
- **Step 4:** Trigger RTL when the drone is closer to home or a rally point than to the mission landing.

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** N/A
- **Behavior after step 3:** No specific issues observed, prepares for RTL.
- **Behavior after step 4:** The drone flies to the correct RTL position but then goes to the mission landing instead of descending at the RTL_DESCEND_ALT.

**Expected behavior:**

- **Expected behavior 1:** The drone should return to the closest safe point (home or rally point) instead of a distant mission landing point.
- **Expected behavior 2:** The drone should descend as per the parameter RTL_DESCEND_ALT instead of flying to a potentially unsafe or distant location.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Described the issue with detailed steps for reproduction and provided flight logs for both the problematic and expected behavior.
- **URL of the flight log provided by the user:** Log files for different versions and RTL types are provided in the report content.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** The user has questions about specific lines of code that may be affecting the issue.
- **Result of the operation after the user adopted suggestion 1:** N/A, as the user himself is investigating and providing potential solutions.
- **Suggestion 2 provided by developers or other personnel:** The user identifies a problematic line and suggests two options to fix the bug.
- **Result of the operation after the user adopted suggestion 2:** N/A, as the suggestion comes from the user’s own insights, with no confirmation or action from other developers mentioned.
