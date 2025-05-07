**Environment where the bug occurred:**

- **Hardware environment:** Windows 11 Pro build 22622.586
- **Software environment:** WSL2 with Ubuntu 22.04.1 LTS, Latest PX4-Autopilot commit
- **Report Time:** Aug 29, 2022
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**e780a58

**Steps for bug reproduction:**

- **Step 1:** Open Ubuntu 22.04 Terminal (WSL2)
- **Step 2:** Run `bash Tools/setup/ubuntu.sh` command
- **Step 3:** Export `PX4_SIM_HOST_ADDR=xx.xx.xx.xx` (IP of the WSL machine)
- **Step 4:** Execute `make px4_sitl_default none_iris`

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** N/A
- **Behavior after step 3:** N/A
- **Behavior after step 4:** Error occurs as `none_iris` target is not found

**Expected behavior:**

- **Expected behavior 1:** Successful build should occur
- **Expected behavior 2:** PX4 should be running on ports

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Ran `make clean`, deleted the local folder, and downloaded the repository again.
- **URL of the flight log provided by the user:** Not provided.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** `tkhamvilai` suggested using `none` instead of `none_iris`.
- **Result of the operation after the user adopted suggestion 1:** Suggestion not explicitly adopted in the conversation.
  
- **Suggestion 2 provided by developers or other personnel:** `dagar` suggested running the PX4 binary directly and provided command instructions.
- **Result of the operation after the user adopted suggestion 2:** User `Javit96` successfully ran the binaries and proceeded with configuration for QGroundControl.
