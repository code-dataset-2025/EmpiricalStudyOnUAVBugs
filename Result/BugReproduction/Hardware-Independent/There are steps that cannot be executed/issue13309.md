**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned
- **Software environment:** PX4 firmware (v1.9.2), mavlink (release/kinetic/mavlink/2019.10.10-1), mavros (0.33.0)
- **Report Time:** Oct 29, 2019
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**fad0c31

**Steps for bug reproduction:**

- **Step 1:** Run `px4_sitl_default gazebo`
- **Step 2:** Send mavlink messages via pymavlink using `c.mav.set_actuator_control_target_send(0, 0, 0, 0, controls)`<font color='red'>pymavlink这句</font>
- **Step 3:** Switch to offboard mode using `commander mode offboard`

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** N/A
- **Behavior after step 3:** The PX4 stack freezes, no uorb topics are published, and no mavlink messages are received; system console remains responsive but ineffectual.

**Expected behavior:**

- **Expected behavior 1:** PX4 should switch vehicle_control_mode into offboard mode.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** 
  - Attempted PX4_INFO() print outputs to debug
  - Used gdb to inspect variables but found no insights
  - Provided URL of the flight log: [Flight Log](https://review.px4.io/plot_app?log=86db944d-af82-456a-bb6c-79e8e5b223dd)

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Julianoes suggested disabling lockstep, rebuilding and trying again.
- **Result of the operation after the user adopted suggestion 1:** Problem was resolved by disabling lockstep.
- **Suggestion 2 provided by developers or other personnel:** Julianoes mentioned that timeouts might occur in SITL when lockstep is disabled, but it shouldn't make a significant difference.
- **Result of the operation after the user adopted suggestion 2:** User received error messages but was assured they are not critical.
