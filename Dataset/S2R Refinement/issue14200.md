**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned
- **Software environment:** PX4 Autopilot with commit regression likely related to `fc9d31c`
- **Report Time:** Feb 21, 2020
- **PX4 Autopilot commit version:** Not explicitly mentioned
- **last commit before the reporting time:**71d4d22

**Steps for bug reproduction:**

- **Step 1:** Run PX4 docker environment using the command: <font color='red'>缺少docker镜像</font>
  ```bash
  PX4_DOCKER_REPO=px4io/px4-dev-ros-melodic:2020-02-11 Tools/docker_run.sh bash
  ```
- **Step 2:** Begin the SITL (Software In The Loop) simulation with:
  ```bash
  DONT_RUN=1 make px4_sitl gazebo
  ```
- **Step 3:** Execute the ROS test for a tiltrotor using:
  ```bash
  test/rostest_px4_run.sh mavros_posix_test_mission.test mission:=VTOL_mission_1 vehicle:=tiltrotor
  ```

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** N/A
- **Behavior after step 3:** The tiltrotor appears to not take off as expected, switching to in-air for about 1 second and then auto-disarming itself.

**Expected behavior:**

- **Expected behavior 1:** The tiltrotor should take off properly and continue the mission without auto-disarming prematurely.
- **Expected behavior 2:** The mission should progress without detecting a premature landing.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Identified and reported issues in the regression likely caused by a past commit (`fc9d31c`). Observed similar issues in manual testing with tailsitters.
- **URL of the flight log provided by the user:** [PX4 Flight Log](https://logs.px4.io/plot_app?log=feba07e1-cd9d-4ee6-8f77-f570f2ebc8fb)

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Initially suspected a specific commit (`fc9d31c`) as causing the regression.
- **Result of the operation after the user adopted suggestion 1:** Further investigation revealed that the multicopter land detector might be falsely detecting a landed state quickly after arming. 

No further suggestions or results from adopting other suggestions are explicitly mentioned.
