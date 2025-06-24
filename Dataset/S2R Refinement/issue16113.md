需求：step1需要CAN型GPS（issue中用的是Here2 GPS）

**Environment where the bug occurred:**

- **Hardware environment:** Pixhawk 4 with Here 2 GPS unit (also tested with Here 3 on Cube Orange)
- **Software environment:** PX4 Autopilot v1.11.1
- **Report Time:** Nov 3, 2020
- **PX4 Autopilot commit version:** Not explicitly mentioned for the initial report, but commit b399698 identified as the issue's cause.
- **last commit before the reporting time:**99833eb

**Steps for bug reproduction:**

- **Step 1:** Switch the Here 2 unit to CAN mode and connect it to the Pixhawk 4 over either CAN1 or CAN2 port.
- **Step 2:** Power the Pixhawk 4. Enable UAVCAN by setting UAVCAN_ENABLE to either automatic or manual config (1 or 2).
- **Step 3:** Reboot the Pixhawk.
- **Step 4:** Observe the missing GPS. For example, in QGC's Mavlink Inspector there's no GPS_RAW_INT message, and typing "uavcan status" in the mavlink console shows all empty in the gnss and mag fields.
- **Step 5:** Unplug and replug the GPS.
- **Step 6:** Wait a few seconds.

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** N/A
- **Behavior after step 3:** The GPS unit is not detected.
- **Behavior after step 4:** No GPS_RAW_INT message, and empty gnss and mag fields in "uavcan status".
- **Behavior after step 5:** N/A
- **Behavior after step 6:** GPS is detected, and GPS_RAW_INT messages appear.

**Expected behavior:**

- **Expected behavior 1:** The GPS unit should be discovered directly upon first boot without needing to physically replug it.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** 
  - Tested different GPS units and Pixhawk boards, tracking the issue to commit b399698.
  - Attempted changes in startup sequence (moved `uavcan start` before board sensors initialization in rcS).
  - Noted the issue resolution on the master branch, indicating it might be due to NuttX changes.
  - Reported damage to USB ports during testing.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Check for traffic on the CAN bus with a Zubax Babel tool, and try disabling serial GPS.
- **Result of the operation after the user adopted suggestion 1:** User reported same issue on multiple setups, unrelated to node ID or UAVCAN_ENABLE settings.
  
- **Suggestion 2 provided by developers or other personnel:** Investigate the changes potentially affecting NuttX.
- **Result of the operation after the user adopted suggestion 2:** User tracked the issue to commit b399698 and attempted adjustments without success.
  
- **Suggestion 3 provided by developers or other personnel:** Consider having someone with the hardware setup look into it.
- **Result of the operation after the user adopted suggestion 3:** User managed a temporary workaround but identified the problem might be more complex, leading to abandoning the fix.
  
- **Additional input provided by `LorenzMeier`:** Advised to review the entire setup and check for common external factors.
