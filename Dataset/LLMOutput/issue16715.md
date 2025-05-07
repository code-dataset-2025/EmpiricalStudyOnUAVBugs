**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned
- **Software environment:** Not explicitly mentioned
- **Report Time:** Feb 1, 2021
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**13e8756

**Steps for bug reproduction:**

- **Step 1:** Add `distance_sensor/lightware_laser_i2c` to `default.cmake`.
- **Step 2:** Build the project.

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** Undefined reference to `PX4Rangefinder` during compilation.

**Expected behavior:**

- **Expected behavior 1:** Successful compilation without undefined reference errors.
- **Expected behavior 2:** Proper integration of `lightware_laser_i2c` with necessary dependencies.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** None explicitly mentioned regarding further investigation; however, included steps for reproducing the issue and mentioned referencing another issue, `#13616`.
- **URL of the flight log provided by the user:** Not provided.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `dagar` mentioned making the dependency explicit for reduced builds.
- **Result of the operation after the user adopted suggestion 1:** N/A (no direct follow-up indicated by the user, as the suggestion was about a planned code adjustment by the developer).
- **Suggestion 2 provided by developers or other personnel:** Developer `dagar` inquired if the user can try `#16721`.
- **Result of the operation after the user adopted suggestion 2:** N/A (no response or outcome mentioned in the provided data).
