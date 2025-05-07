**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned
- **Software environment:** PX4 Autopilot version v1.11.0-rc3-914-g7861377e20
- **Report Time:** Dec 24, 2020
- **PX4 Autopilot commit version:** not mentioned<font color='red'>实际在软件环境中写了</font>
- **last commit before the reporting time:**92afe45

**Steps for bug reproduction:**

- **Step 1:** Execute `make clean`.
- **Step 2:** Set the build type with `PX4_CMAKE_BUILD_TYPE=Debug`.
- **Step 3:** Execute `make px4_sitl gazebo_tailsitter_gdb`.

**Observed behavior by the user:**

- **Behavior after step 1:** Not mentioned
- **Behavior after step 2:** Not mentioned
- **Behavior after step 3:** Error appears: `etc/init.d-posix/rcS: 6: .: px4-alias.sh: not found` and `ERROR [px4] Startup script returned with return value: 512`.

**Expected behavior:**

- **Expected behavior 1:** PX4 should run without errors.
- **Expected behavior 2:** Debugging should be possible with `-O0` optimization for effective stepping.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Described the steps to reproduce the issue.
- **URL of the flight log provided by the user:** Not provided.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Fixed by commit `#16446`.
- **Result of the operation after the user adopted suggestion 1:** Not directly mentioned, but the issue status was closed, indicating resolution.
