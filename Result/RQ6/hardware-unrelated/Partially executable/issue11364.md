**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned
- **Software environment:** PX4 Autopilot
- **Report Time:** Feb 1, 2019
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**1d86b75

**Steps for bug reproduction:**

- **Step 1:** Send a COMMAND_LONG with LAT and LON as integers multiplied by 10^7 with negative latitude or longitude.<font color='red'>MAVLINK MAV_CMD_NAV_WAYPOINT命令无反应</font>
- **Step 2:** Aircraft will attempt to fly off to an impossible location setpoint (example 50.0001, -2400000).

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** Aircraft attempts to fly to an impossible location.

**Expected behavior:**

- **Expected behavior 1:** Aircraft should not attempt to fly to an impossible location.
- **Expected behavior 2:** Values should be correctly scaled down if negative, or the sanity check should be eliminated allowing simulation failures, or the reposition command should be rejected if lat/lon are not in valid ranges.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Proposed a fix using absolute values (`abs`) to correctly handle negative lat/lon values.
- **URL of the flight log provided by the user:** Not provided.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Julianoes suggested option a would be the first quick fix and recommended documenting on the MAVLink level.
- **Result of the operation after the user adopted suggestion 1:** Fix likely implemented as suggested, confirmed with reference to a later fix (\\\#13690).
- **Suggestion 2 provided by developers or other personnel:** Hamishwillee suggested rejecting COMMAND_LONG straightaway or handling the LONG vs INT problem holistically.
- **Result of the operation after the user adopted suggestion 2:** Not explicitly mentioned.

- **Suggestion 3 provided by developers or other personnel:** GarfieldG raised a concern regarding the loss of functionality with reposition command without LAT/LON when using COMMAND_INT.
- **Result of the operation after the user adopted suggestion 3:** No explicit resolution mentioned in the document.
