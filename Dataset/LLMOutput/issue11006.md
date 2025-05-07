**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned
- **Software environment:** PX4 Autopilot with no specific commit version mentioned
- **Report Time:** Dec 7, 2018
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**dc49e25

**Steps for bug reproduction:**

- **Step 1:** Create a directory with `mkdir -p ~/px4_catkin/src`
- **Step 2:** Navigate to the new directory with `cd ~/px4_catkin/src`
- **Step 3:** Clone the PX4 Firmware repository with `git clone git@github.com:PX4/Firmware px4`
- **Step 4:** Go back to the px4_catkin directory with `cd ~/px4_catkin`
- **Step 5:** Build the package using `catkin build`
- **Step 6:** Source the setup file with `. ./devel/setup.bash`
- **Step 7:** Attempt to run PX4 with `rosrun px4 px4`

**Observed behavior by the user:**

- **Behavior after step 7:** The command `rosrun px4 px4` fails with an error that the executable cannot be found, listing several paths where `px4` was expected but was either not a file or not executable.

**Expected behavior:**

- **Expected behavior 1:** The command `rosrun px4 px4` should successfully find and execute the PX4 executable.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** The user provided a detailed command walkthrough showing how the issue can be reproduced and discussed changes to the `CMakeLists.txt` file to resolve the issue for ROS.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `dagar` suggested looking at specific lines in the `CMakeLists.txt` file to fix the issue.
- **Result of the operation after the user adopted suggestion 1:** Not explicitly mentioned; however, the discussion continued regarding potential solutions.
  
- **Suggestion 2 provided by developers or other personnel:** Developer `TSC21` indicated understanding the complexities involved and pointed out challenges with the build process.
- **Result of the operation after the user adopted suggestion 2:** Collaboration continued with potential testing and investigation suggestions to ensure ROS compatibility.

- **Suggestion 3 provided by developers or other personnel:** Developer `dagar` hinted that `RUNTIME_OUTPUT_DIRECTORY` could be the problem.
- **Result of the operation after the user adopted suggestion 3:** User `jgoppert` confirmed the `CMAKE_RUNTIME_OUTPUT_DIRECTORY` was indeed causing issues and proposed modifications to the `CMakeLists.txt` file, suggesting further review by `dagar` for packaging implications.
