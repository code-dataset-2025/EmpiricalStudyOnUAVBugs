**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned
- **Software environment:** Ubuntu 22.04
- **Report Time:** Dec 28, 2022
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**964e9dd

**Steps for bug reproduction:**

- **Step 1:** Run the `./Tools/setup/ubuntu.sh --sim_jammy` command.
- **Step 2:** Restart the computer.
- **Step 3:** Execute the command `make px4_sitl gazebo`.

**Observed behavior by the user:**

- **Behavior after step 1:** The `ubuntu.sh` script does not install Gazebo.<font color='red'>由于实现使用其他版本px4中的ubuntu.sh安装了gazebo，在这里卸载gazebo，然后按照此步骤执行，结果一致</font>
- **Behavior after step 3:** The simulation environment using legacy Gazebo (SITL) does not work.

**Expected behavior:**

- **Expected behavior 1:** The `ubuntu.sh` script should install Gazebo as part of its dependencies.
- **Expected behavior 2:** SITL should be enabled and functional with the installed Gazebo.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** The user installed Gazebo and `libgazebo-dev` packages via `apt-get`.
- **URL of the flight log provided by the user:** Not provided.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `bperseghetti` discussed the need to choose between classic Gazebo and the new Gazebo (gz) for future compatibility and recommended not using classic Gazebo on Ubuntu 22.04.
- **Result of the operation after the user adopted suggestion 1:** The user realized the potential issues with classic Gazebo and understood the need for changes in the documentation and setup scripts.
- **Suggestion 2 provided by developers or other personnel:** Update documentation and consider renaming to clarify between classic Gazebo and new Gazebo, including making changes to avoid confusion in the future.
- **Result of the operation after the user adopted suggestion 2:** User agreed that updates should be made to the documentation to prevent confusion and considered system dependencies implications for future releases.
