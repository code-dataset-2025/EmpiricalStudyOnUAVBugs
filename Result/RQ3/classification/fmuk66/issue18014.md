**Environment where the bug occurred:**

- **Hardware environment:** NXP_FMUK66_V3
- **Software environment:** PX4 Autopilot built for target nxp_fmuk66-v3_socketcan
- **Report Time:** Aug 2, 2021
- **PX4 Autopilot commit version:** 607be59fd5b47160326052dea8eea7edc7619d66

**Steps for bug reproduction:**

- **Step 1:** Compile the current master for target nxp_fmuk66-v3_socketcan.
- **Step 2:** Update FMUK66_v3 with the fmuk66-v3_socketcan build.
- **Step 3:** Power cycle the FMU.
- **Step 4:** Observe the error.

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** N/A
- **Behavior after step 3:** N/A
- **Behavior after step 4:** Encountering a hardfault.

**Expected behavior:**

- **Expected behavior 1:** Normal operation without encountering a hardfault.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** User mentioned periodically getting a hardfault, provided a full hardfault log, and described the hardware and software environment used. Additionally, a fresh build was attempted after related fixes were merged.
- **URL of the flight log provided by the user:** Not provided.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `davids5` asked to test #18017, which partially fixes an issue.
- **Result of the operation after the user adopted suggestion 1:** The user tested the fix and reported that the hardfault now occurred upon arming the rover.
- **Suggestion 2 provided by developers or other personnel:** Developer `davids5` requested more detailed reproduction steps and parameters.
- **Result of the operation after the user adopted suggestion 2:** User gave detailed hardware configuration and confirmed using the latest master without custom code changes.
- **Suggestion 3 provided by developers or other personnel:** Developer `davids5` inquired about the issue's persistence.
- **Result of the operation after the user adopted suggestion 3:** User confirmed that unexpected reboots still occur.
