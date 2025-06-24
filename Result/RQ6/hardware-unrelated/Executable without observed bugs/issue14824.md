**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned
- **Software environment:** Ubuntu 18.04 with openjdk version "1.8.0_252"
- **Report Time:** May 4, 2020
- **PX4 Autopilot commit version:** v1.11.0-beta1-151-g8e2c52a31a

**Steps for bug reproduction:**

- **Step 1:** Fresh download of the PX4 Firmware and execute `ubuntu.sh`.
- **Step 2:** Install and select Java OpenJDK 8 using `sudo update-alternatives --config java`.
- **Step 3:** Execute `make px4_sitl_default jmavsim` in the Firmware folder.

**Observed behavior by the user:**

- **Behavior after step 3:** The process throws a `java.lang.UnsupportedClassVersionError` indicating that `jmavsim` has been compiled by a more recent version of the Java Runtime than is available.

**Expected behavior:**

- **Expected behavior 1:** The PX4 simulation should connect to jmavsim.
- **Expected behavior 2:** jMAVSim should start up without errors.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:**
  - Attempted to ensure JDK version 8 is used.
  - Removed `Tools/jMAVSim/out` directory multiple times and retried the build process.
  - Verified that `/out` directory does not exist before executing build commands.
  
**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `julianoes` asked if the error persists after removing `Tools/jMAVSim/out` and retrying.
- **Result of the operation after the user adopted suggestion 1:** The user confirmed the issue persists even after trying the suggested solution.
- **Suggestion 2 provided by developers or other personnel:** Developer `julianoes` inquired about the user's OS version and tested on both Ubuntu 18.04 and Ubuntu 20.04 with OpenJDK 8, without encountering the problem.
- **Result of the operation after the user adopted suggestion 2:** The user reinstalled Ubuntu 18.04 freshly and found the issue resolved.
