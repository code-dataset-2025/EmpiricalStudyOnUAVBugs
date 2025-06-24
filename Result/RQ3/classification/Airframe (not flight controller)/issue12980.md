**Environment where the bug occurred:**

- **Hardware environment:** Hover 1 Frame, Pixhawk Radiolink with v3 bootloader
- **Software environment:** PX4 Autopilot, v1.9.2 stable
- **Report Time:** Sep 17, 2019
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**4f19d45

**Steps for bug reproduction:**

- **Step 1:** Switch on the drone.
- **Step 2:** Publish a command on `mavros/setpoint_raw/attitude` with a yawrate and correct mask.
- **Step 3:** Observe the vehicle's response to the yawrate command.

**Observed behavior by the user:**

- **Behavior after step 1:** Drone is powered on and ready.
- **Behavior after step 2:** The vehicle does not respond to yawrate commands.
- **Behavior after step 3:** The vehicle remains unresponsive to the yawrate command despite correct input.

**Expected behavior:**

- **Expected behavior 1:** The vehicle should rotate according to the bodyrate Z command.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Tested the issue in SITL with different configurations; attempted multiple tests and reported the results.
- **URL of the flight log provided by the user:** [Google Drive Folder](https://drive.google.com/open?id=1jufiucPZ2O7UPZHpCZfKG8gnDEj1XmIC)

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** `MaEtUgR` suggested performing a `make clean` if there is a compass calibration issue in SITL.
  - **Result of the operation after the user adopted suggestion 1:** `Pedro-Roque` acknowledged and mentioned they would follow up on it.
- **Suggestion 2 provided by developers or other personnel:** Follow `@dagar`'s suggestion to add a test for the issue before the next release.
  - **Result of the operation after the user adopted suggestion 2:** `Pedro-Roque` agreed to follow up and add tests in the future.

