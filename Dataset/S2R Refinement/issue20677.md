# Basic Information:
### Title: Geofence_breach_check doesn't rely on GF_SOURCE anymore. Always uses global_pos.* #20677
### Issue status: Closed
### Author: MikeCharikov
### Issue open time: Nov 29, 2022
### Fixed by: #22394

# Report
### Report author: MikeCharikov
### Report Time: Nov 29, 2022
### Report Content:
#### Describe the bug:
Since PX4 version 1.12, the `geofence_breach_check` function no longer takes into account the value of the `GF_SOURCE` parameter. It always uses the `global_pos` topic as the source for the drone's location. This can cause the drone to breach the geofence significantly in a `no_global_pos` state.

Here is a snippet of the new `geofence_breach_check` function introduced in 1.12:
```cpp
_gf_breach_avoidance.setHorizontalTestPointDistance(test_point_distance);
_gf_breach_avoidance.setVerticalTestPointDistance(vertical_test_point_distance);
_gf_breach_avoidance.setTestPointBearing(test_point_bearing);
_gf_breach_avoidance.setCurrentPosition(_global_pos.lat, _global_pos.lon, _global_pos.alt);
_gf_breach_avoidance.setMaxHorDistHome(_geofence.getMaxHorDistanceHome());
_gf_breach_avoidance.setMaxVerDistHome(_geofence.getMaxVerDistanceHome());

if (home_position_valid()) {
    _gf_breach_avoidance.setHomePosition(_home_pos.lat, _home_pos.lon, _home_pos.alt);
}
fence_violation_test_point = _gf_breach_avoidance.getFenceViolationTestPoint();
gf_violation_type.flags.dist_to_home_exceeded = !_geofence.isCloserThanMaxDistToHome(fence_violation_test_point(0),
        fence_violation_test_point(1),
        _global_pos.alt);
gf_violation_type.flags.max_altitude_exceeded = !_geofence.isBelowMaxAltitude(_global_pos.alt +
        vertical_test_point_distance);
gf_violation_type.flags.fence_violation = !_geofence.isInsidePolygonOrCircle(fence_violation_test_point(0),
        fence_violation_test_point(1),
        _global_pos.alt);
```
The old logic in `geofence.Check()` is now only used for handling the `DO_REPOSITION` and `ORBIT` commands.

#### To reproduce:
1. Set the drone to the `no_global_pos` state.
2. Observe the drone's behavior when a geofence breach is expected.

#### Expected behavior:
If `GF_SOURCE == 1`, the `geofence_breach_check` function should rely on the `gps_pos` topic instead of the `global_pos` topic.

#### Drone:
- **Type:** Multicopter

#### Additional context:
- Version: PX4-1.12+
- No additional logs or related data were provided.

---

# Comment
## Comment1
### Comment author: MikeCharikov
### Comment Time: Dec 2, 2022
### Comment Content:
Here is the pull request (PR) to fix this bug: [#20697](https://github.com/PX4/PX4-Autopilot/pull/20697)

---

# Detailed Bug Report
**Environment where the bug occurred:**
- **Hardware environment:** Not mentioned
- **Software environment:** PX4 Autopilot version 1.12+
- **Report Time:** Nov 29, 2022
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**0c923bd

**Steps for bug reproduction:**
- **Step 1:** Configure the drone to use the `GF_SOURCE` parameter with a value of 1.
- **Step 2:** Transition the drone into a `no_global_pos` state.
- **Step 3:** Observe how the geofence breach check behaves during this state.

**Observed behavior by the user:**
- **Behavior after step 1:** Configuration of `GF_SOURCE` has no effect on the `geofence_breach_check`.
- **Behavior after step 2:** The `geofence_breach_check` continues to rely on the `global_pos` topic, leading to potential geofence breaches during `no_global_pos`.<font color='red'>设置参数SYS_HAS_GPS为DISABLED后，listener监听vehicle_gps_position显示never published，模拟禁用gps成功，但此时listener监听 geofence_result也是同样的结果never published，而非出现错误</font>

**Expected behavior:**

- **Expected behavior 1:** The `geofence_breach_check` should rely on the `gps_pos` topic when `GF_SOURCE == 1`.
- **Expected behavior 2:** The drone should respect geofence boundaries even in a `no_global_pos` state.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** The user identified the issue in the code and provided a code snippet for review.
- **Pull request submitted:** PR #20697 to fix the bug.

**Communication between developers or other personnel and the user:**
- **Suggestion 1 provided by the user:** Submitted PR #20697 as a potential fix for the issue.
- **Result of the operation after the user adopted suggestion 1:** Acknowledged and eventually fixed in PR #22394.
