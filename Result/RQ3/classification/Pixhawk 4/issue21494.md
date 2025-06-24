**Environment where the bug occurred:**

- **Hardware environment:** Pixhawk 4 with a hexacopter
- **Software environment:** PX4 Autopilot v1.13.2
- **Report Time:** Apr 19, 2023
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**0934d3b

**Steps for bug reproduction:**

- **Step 1:** Assign one switch of your RC to Hold mode.<font color='red'>需要控制器</font>
- **Step 2:** Power on your drone with the switch of Flight Mode on Hold mode.
- **Step 3:** Wait for the drone to start, it will stay in Manual instead to go to Hold mode even when a good position is set.

**Observed behavior by the user:**
- **Behavior after step 1:** N/A
- **Behavior after step 2:** N/A
- **Behavior after step 3:** The drone remains in Manual mode and does not switch to Hold mode, resulting in a dangerous takeoff when started.

**Expected behavior:**
- **Expected behavior 1:** PX4 should automatically switch to Hold mode once a GPS position is set.

**Additional information provided by the user for bug investigation:**
- **Actions taken by the user:** Hot fixed by changing the manual mode to hold mode with a companion computer.
- **URL of the flight log provided by the user:** Not explicitly provided in the text.

**Communication between developers or other personnel and the user:**
- **Suggestion 1 provided by developers or other personnel:** Comment by `afwilkin` requesting the flight logs for further investigation.
- **Result of the operation after the user adopted suggestion 1:** The user provided details of the flight mode assignments and mentioned the switch was on hold mode, but manual was set by PX4.
- **Suggestion 2 provided by developers or other personnel:** N/A
- **Result of the operation after the user adopted suggestion 2:** N/A
