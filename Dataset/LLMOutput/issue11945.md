**Environment where the bug occurred:**

- **Hardware environment:** Snapdragon Flight
- **Software environment:** PX4 Autopilot v1.9 release candidate
- **Report Time:** May 1, 2019
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**a27a43e

**Steps for bug reproduction:**

- **Step 1:** Use PX4 Autopilot on Snapdragon Flight with v1.9 release candidate.
- **Step 2:** Build the project using the eagle_default target.
- **Step 3:** Run the command `uorb start`.

**Observed behavior by the user:**

- **Behavior after step 1:** The build completes successfully on both POSIX and QURT sides.
- **Behavior after step 2:** Unspecified in detail, but the build is successful.
- **Behavior after step 3:** Errors occur on the DSP side during uORB startup with undefined PLT symbols related to atomic operations.

**Expected behavior:**

- **Expected behavior 1:** The PX4 Autopilot should run without linker errors on the DSP side of Snapdragon Flight.
- **Expected behavior 2:** The uORB should start successfully without encountering undefined symbols.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** The user provided the specific linker error messages and noted that previous commits in version 1.9 or in 1.8.2 worked successfully.
- **URL of the flight log provided by the user:** Not provided.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `julianoes` acknowledged the issue and attempted to reproduce it.
- **Result of the operation after the user adopted suggestion 1:** Developer `julianoes` confirmed the reproduction of the issue.
- **Suggestion 2 provided by developers or other personnel:** Developer `julianoes` suggested ifdefing the usage of atomic operations and created a pull request.
- **Result of the operation after the user adopted suggestion 2:** N/A (no outcome described as resulting from the suggestion because it's more about fixing by the developer).
