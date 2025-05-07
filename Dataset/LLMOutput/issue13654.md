**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned
- **Software environment:** Not explicitly mentioned
- **Report Time:** Dec 2, 2019
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**9b66cbd

**Steps for bug reproduction:**

- **Step 1:** Attempt to build the PX4 Autopilot for Raspberry Pi using the command `make px4_raspberrypi_cross`.

**Observed behavior by the user:**

- **Behavior after step 1:** The build process for `src/modules/camera_feedback` fails.

**Expected behavior:**

- **Expected behavior 1:** The build process should complete successfully without errors.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** The user described the bug and provided basic steps to reproduce it but did not include detailed investigation efforts.
- **URL of the flight log provided by the user:** Not provided.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `julianoes` suggested that they might not have a Raspberry Pi build in the Continuous Integration (CI) system.
- **Result of the operation after the user adopted suggestion 1:** Developer `dagar` confirmed the absence of a Raspberry Pi build in the CI system and mentioned plans to address this issue.
