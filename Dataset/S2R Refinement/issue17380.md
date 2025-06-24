**Environment where the bug occurred:**

- **Hardware environment:** Modal AI Flight Deck board and pixracer
- **Software environment:** PX4 Autopilot v1.12.0-beta2
- **Report Time:** Apr 12, 2021
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**b9e0a16

**Steps for bug reproduction:**

- **Step 1:** Flash pixracer with v1.12.0-beta2 with default params.
- **Step 2:** Set the airframe to Generic Quadrotor X.
- **Step 3:** Set the SYS_MC_EST_GROUP parameter to LPE.
- **Step 4:** Reboot flight controller.
- **Step 5:** Attempt to create mavlink connection to board using qgroundcontrol.

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** N/A
- **Behavior after step 3:** N/A
- **Behavior after step 4:** N/A
- **Behavior after step 5:** Error where re-connection does not occur

**Expected behavior:**

- **Expected behavior 1:** The flight controller should boot like normal after setting the parameter and rebooting.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Tested the issue on different hardware (Modal AI Flight Deck board and pixracer) and in the gazebo simulation where the drone behaved normally.
- **URL of the flight log provided by the user:** Not provided.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `dagar` suggested resolving the issue before the release of v1.12, and recommended switching to EKF2 as LPE isn't really supported anymore.
- **Result of the operation after the user adopted suggestion 1:** Not provided.
