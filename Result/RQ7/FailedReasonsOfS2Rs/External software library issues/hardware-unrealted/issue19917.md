**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned (related to px4_sitl_rtps which likely indicates a simulated environment using Gazebo).
- **Software environment:** PX4 Autopilot with issues arising after merging master into main around July 8, 2022.
- **Report Time:** Jul 14, 2022
- **PX4 Autopilot commit version:** Not explicitly mentioned 
- **last commit before the reporting time:**c71cc5b

**Steps for bug reproduction:**

- **Step 1:** Clone the PX4-Autopilot repository and update submodules.
- **Step 2:** Build the PX4-Autopilot code and start the simulator with the `rtps` and `gazebo` targets.
- **Step 3:** Install Fast-DDS, ROS2, and set up the `px4_ros_com_ros2` workspace following the instructions from the provided URL, then try to run `micrortps_agent -t UDP`, which leads to the error.<font color='red'>执行micrortps_agent -t UDP命令返回错误micrortps命令无法找到，搜索后发现https://github.com/PX4/PX4-Autopilot/issues/20952中提到micrortps_agent已经不在px4中使用</font>
- **Step 4:** Revert PX4-Autopilot to an earlier commit `10a2b4c9f7d34234459b4d3604b99a33491a9d83` and restart the simulator.
- **Step 5:** Restart the `micrortps_agent -t UDP` and verify it continues running without crashing.
- **Step 6:** Use `ros2 topic echo` commands to check that messages are correctly published.

**Observed behavior by the user:**

- **Behavior after step 1:** Repository cloned and prepared for building.
- **Behavior after step 2:** PX4 simulator runs, but the `micrortps_agent` throws an exception and crashes.
- **Behavior after step 3:** Error indicating unexpected byte value when running `micrortps_agent -t UDP`.
- **Behavior after step 4:** Simulator operates without error after reverting to an earlier commit.
- **Behavior after step 5:** `micrortps_agent -t UDP` runs without crashing post revert.
- **Behavior after step 6:** Data is published successfully to ROS2 topics.

**Expected behavior:**

- **Expected behavior 1:** `micrortps_agent` should not throw exceptions or crash.
- **Expected behavior 2:** ROS2 should display incoming data correctly without manual intervention.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** The user attempted manual edits on files and verified message definitions in `px4_msgs` and `px4_ros_com`.
- **Reverted to an older commit:** The user temporarily resolved the issue by reverting the repository to a previous state before the problematic merge.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Many users suggested reverting to commit `10a2b4c9f7d34234459b4d3604b99a33491a9d83`.
- **Result of the operation after the user adopted suggestion 1:** Issue was temporarily resolved, allowing the `micrortps_agent` to run without error.
- **Suggestion 2 provided by developers or other personnel:** Update message definitions with `uorb_to_ros_msgs.py`.
- **Result of the operation after the user adopted suggestion 2:** Fixes were confirmed after correct naming conventions were taken care of, removing initial errors.

- **Additional Suggestions:** The users and developers engaged in discussing potential workarounds and alternatives such as using `micro-ROS-Agent`.
