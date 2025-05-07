**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned
- **Software environment:** 
  - Ubuntu 20.04
  - ROS2 Foxy
  - Ignition Fortress
- **Report Time:** May 14, 2023
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**616a71a

**Steps for bug reproduction:**

- **Step 1:** Directly run `make px4_sitl ignition`.
- **Step 2:** Follow the guide [px4-simulation-ignition](https://github.com/Auterion/px4-simulation-ignition) for the creation and installation of the Debian package on Linux.
- **Step 3:** Attempt to compile with `cmake`.

**Observed behavior by the user:**

- **Behavior after step 1:** An error occurs: `ninja: error: unknown target 'ignition'`.
- **Behavior after step 2 and 3:** During the compilation with `cmake`, an error shows the MAVLINK package is not found, despite being installed via `sudo apt-get install ros-foxy-mavros ros-foxy-mavros-extras`.<font color='red'>cmake这步通过但下一步make出错</font>

**Expected behavior:**

- **Expected behavior 1:** Successful build of SITL with Ignition using the command `make px4_sitl ignition`.
- **Expected behavior 2:** Successful compilation of the Debian package following the aforementioned guide without encountering the MAVLINK not found error.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Attempted the build following another guide from the repository but encountered a persistent error.
- **URL of the flight log provided by the user:** Not provided.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Jaeyoung-Lim suggested using updated instructions as Ignition has been renamed to "gz".
- **Result of the operation after the user adopted suggestion 1:** Not explicitly mentioned in the comment. The report itself was closed, possibly indicating resolution.
