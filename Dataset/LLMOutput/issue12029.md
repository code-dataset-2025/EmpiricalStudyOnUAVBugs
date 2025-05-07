**Environment where the bug occurred:**

- **Hardware environment:** Simulated typhoon h480
- **Software environment:** PX4 Autopilot with simulated environment in Gazebo using the mavros_posix_sitl.launch
- **Report Time:** May 16, 2019
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**9d8015d

**Steps for bug reproduction:**

- **Step 1:** Execute `roslaunch px4 mavros_posix_sitl.launch vehicle:=typhoon_h480`.<font color='red'>执行遇到错误，找不到mavlink_sitl_gazebo，按https://blog.csdn.net/wmj_studying/article/details/130719807、https://discuss.px4.io/t/mavros-posix-sitl-launch-is-neither-a-launch-file-in-package-px4-nor-is-px4-a-launch-file-name/30522 解决未果</font>
- **Step 2:** Arm the vehicle and take off.
- **Step 3:** Publish `/mavros/actuator_control` ROS message at 10Hz with (group_mix=2).

**Observed behavior by the user:**

- **Behavior after step 1:** The simulation environment, Gazebo, with typhoon h480 is launched.
- **Behavior after step 2:** The vehicle is armed and takes off correctly.
- **Behavior after step 3:** The UAV becomes unstable, particularly if non-zero setpoints are sent to the controls field of the ActuatorControls topic. If this process is repeated with a lower publish rate (1 Hz works), the vehicle remains stable.

**Expected behavior:**

- **Expected behavior 1:** The vehicle should remain stable when the actuator control messages are published at 10 Hz.
- **Expected behavior 2:** The gimbal should be controlled without causing instability to the vehicle.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Suggested making changes in the behavior of control group settings and considered using a different MAVLink message for controlling the gimbal.
- **URL of the flight log provided by the user:** Multiple logs shared indicating behavior at different publishing rates:
  - Log at 10Hz: [Log](https://review.px4.io/plot_app?log=6310f80b-8714-4626-810e-6a83a1e680e7)
  - Log at 100Hz: [Log](https://review.px4.io/plot_app?log=7482249f-a0c0-44b7-a692-aad373741b8b)

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** It's suggested that one potential fix could involve suppressing certain outputs to stabilize the control.
- **Result of the operation after the user adopted suggestion 1:** The user found that stopping `vmount` solved the problem of resetting values to 0.
- **Suggestion 2 provided by developers or other personnel:** The MountControl plugin in mavros was suggested as an alternative method for controlling the gimbal.
- **Result of the operation after the user adopted suggestion 2:** The user was informed about the merged plugin and considered integrating it, marking the issue as resolved.
