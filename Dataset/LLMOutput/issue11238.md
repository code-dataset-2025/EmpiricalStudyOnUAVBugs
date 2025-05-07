**Environment where the bug occurred:**

- **Hardware environment:** Custom adapter board with a Pixhawk 2.1 cube, a WiFi module, and a long-range radio.
- **Software environment:** PX4 code fork based on version 1.7.3 with a custom CAN driver for ESCs.
- **Report Time:** Jan 18, 2019
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**95eff33

**Steps for bug reproduction:**

- **Step 1:** Unplug the RC receiver and remove props.
- **Step 2:** Power on the aircraft.
- **Step 3:** Wait for the issue to occur.

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** N/A
- **Behavior after step 3:** Sometimes, the aircraft arms and takes off due to input_rc messages with SOURCE=RC_INPUT_SOURCE_MAVLINK.

**Expected behavior:**

- **Expected behavior 1:** The aircraft should remain unarmed while on the ground.
- **Expected behavior 2:** There should be no unexpected arming or motor spin-up without RC input.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Ensured RC_IN lines are not electrically floating; disabled all external MAVLink traffic; tested with various setups.
- **URL of the flight log provided by the user:** 
  - https://logs.px4.io/plot_app?log=4abb3756-1202-4d7f-93df-7278dcec0897
  - https://logs.px4.io/plot_app?log=d12666c6-faed-4645-bc04-0d5a94d05116
  - https://logs.px4.io/plot_app?log=508c3766-012d-4a24-a538-80235388be71
  - https://logs.px4.io/plot_app?log=2f046532-ae41-4327-b683-57cdfe3e1d70
  - https://logs.px4.io/plot_app?log=7cd79b51-c6b8-4ee0-9b33-311ef4f6c0ae

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Dagar asked if QGroundControl was being used and asked to verify if thumbsticks were enabled.
- **Result of the operation after the user adopted suggestion 1:** Jzazbert confirmed using QGroundControl but mentioned the issue occurred with all external data links disconnected.
  
- **Suggestion 2 provided by developers or other personnel:** Discussion regarding potential legacy use; recommended disabling the sending of RC_CHANNELS_OVERRIDE.
- **Result of the operation after the user adopted suggestion 2:** Jzazbert disabled the RC_CHANNELS_OVERRIDE message for safety, which partially addressed the vulnerability but wasn't the ideal solution.

- **Further discussion:** Developers speculated the issue might be related to same MAV_SYS_ID settings on multiple aircraft, CPU load, and the potential legacy functionality of RC_CHANNELS_OVERRIDE. Suggestions involved examining CPU plots and considering a fix in future updates.
