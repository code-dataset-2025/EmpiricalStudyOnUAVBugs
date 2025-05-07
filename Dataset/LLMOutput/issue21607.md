**Environment where the bug occurred:**

- **Hardware environment:** VMware virtual machine
- **Software environment:** Ubuntu 22.04, PX4 Autopilot (commit version: not mentioned)
- **Report Time:** May 18, 2023
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**599a66c

**Steps for bug reproduction:**

- **Step 1:** Install a brand-new Ubuntu 22.04 on a VMware virtual machine.
- **Step 2:** Install the PX4 development environment using `bash ./PX4-Autopilot/Tools/setup/ubuntu.sh`.
- **Step 3:** Build and run the simulation with `make px4_sitl gz_x500`.
- **Step 4:** Observe the error in the terminal.

**Observed behavior by the user:**

- **Behavior after step 1:** Ubuntu 22.04 is successfully installed on VMware.
- **Behavior after step 2:** PX4 development environment installation completes without issues.
- **Behavior after step 3:** Simulation build process initiates, but an error occurs during runtime.
- **Behavior after step 4:** Gazebo simulation crashes with repeated errors about unsupported OpenGL 3.3.

**Expected behavior:**

- **Expected behavior 1:** Gazebo simulation GUI should launch successfully.
- **Expected behavior 2:** Simulation should run without any crashes or errors.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:**
  - Modified the start script `px4-rc.simulator` to explicitly specify the render engine.
  - Changed the script from:
    ```bash
    if [ -z "${HEADLESS}" ]; then
        # HEADLESS not set, starting gui
        ${gz_command} ${gz_sub_command} -g &
    fi
    ```
    to:
    ```bash
    if [ -z "${HEADLESS}" ]; then
        # HEADLESS not set, starting gui
        ${gz_command} ${gz_sub_command} -g --render-engine ogre &
    fi
    ```
  - After this change, the simulation worked correctly, and the Gazebo GUI launched as expected.

- **URL of the flight log provided by the user:** Not provided.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** 
  - Developer `dagar` suggested that there was no preference between `ogre` and `ogre2` as long as the simulation worked. He invited the user to submit a pull request implementing the change.

- **Result of the operation after the user adopted suggestion 1:** 
  - User `TianmingLi` confirmed submitting the pull request to fix the issue.

- **Suggestion 2 provided by developers or other personnel:** 
  - Developer `dagar` asked `MaEtUgR` to test the issue using WSL2 (Windows Subsystem for Linux 2).

- **Result of the operation after the user adopted suggestion 2:** 
  - Developer `MaEtUgR` tested on WSL2 but encountered a different error related to EGL permissions and unimplemented exceptions. He provided additional debugging logs and mentioned testing the fix from pull request #21617 next.

- **Suggestion 3 provided by developers or other personnel:** 
  - None explicitly mentioned, but the resolution of the issue was linked to pull request #21617.

- **Result of the operation after the user adopted suggestion 3:** 
  - Issue was resolved and closed after the fix in #21617.
