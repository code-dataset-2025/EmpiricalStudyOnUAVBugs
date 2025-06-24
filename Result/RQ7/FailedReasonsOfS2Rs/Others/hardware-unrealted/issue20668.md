**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned
- **Software environment:** Ubuntu 22.04 LTS, PX4 Autopilot with no specific commit version mentioned
- **Report Time:** Nov 24, 2022
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**85e9c17

**Steps for bug reproduction:**

- **Step 1:** On an Ubuntu 22.04 LTS system, download the PX4 GitHub project with its submodules.
- **Step 2:** Install the dependencies using the `ubuntu.sh` script with the argument `--sim_jammy`.
- **Step 3:** Open the PX4 project folder using Visual Studio Code (VSCode).
- **Step 4:** Navigate to the Launch and Debug Panel (4th one from the top).
- **Step 5:** Select the SITL (GZ) launch configuration and launch it by clicking the small green play button beside the dropdown.<font color='red'>这样打开在run and debug栏中找不到能debug和run的文件</font>
- **Step 6:** Observe the terminal tab at the bottom for output.

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** N/A
- **Behavior after step 3:** N/A
- **Behavior after step 4:** N/A
- **Behavior after step 5:** Errors occur indicating the `ign` command is not found.
- **Behavior after step 6:** Various errors in terminal log including the failure to start `ign gazebo`.

**Expected behavior:**

- **Expected behavior 1:** PX4 and Gazebo should launch without issue.
- **Expected behavior 2:** The x500 model should run in Gazebo without errors.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Mentioned an issue with Ubuntu 20.04 with similar configuration but preferred to focus on resolving the issue on the latest Ubuntu LTS version.
- **URL of the flight log provided by the user:** Not provided.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** `ivanpadavan` suggested modifying `GZBridge.cpp` to change certain values from 1000 to 10000.
- **Result of the operation after the user adopted suggestion 1:** No improvement reported by `master0v` and `vacabun`.
- **Suggestion 2 provided by developers or other personnel:** `lvanasse` indicated the issue was fixed in the installation script by addressing missing dependencies.
- **Result of the operation after the user adopted suggestion 2:** `vacabun` reported resolving the issue by turning off the firewall.
- **Suggestion 3 provided by developers or other personnel:** `bastianhjaeger` suggested killing a background instance of the Gazebo ignition server.
- **Result of the operation after the user adopted suggestion 3:** `RodrigofrBastos` asked how to kill the server, and `bastianhjaeger` later advised using `htop`.

