**Environment where the bug occurred:**

- **Hardware environment:** MindRacer FCU, potentially other FCUs
- **Software environment:** PX4 Autopilot version >= v1.10
- **Report Time:** Apr 1, 2020
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**15332a7

**Steps for bug reproduction:**

- **Step 1:** For MindRacer users, use version 1.10 or higher of the firmware.
- **Step 2:** Connect MindRacer (standalone) to QGroundControl (QGC) through a USB cable and wait for connection.
- **Step 3:** QGC will alert "dangerously low battery, system SHUTDOWN".
- **Step 4:** You cannot perform most calibration/parameter update actions. QGC alerts "Transition denied, SHUTDOWN to INIT" or similar.

Alternative scenario for other FCUs:

- **Step 1:** Power FCU with a 3S battery and use version 1.10 or higher of the firmware.
- **Step 2:** Connect to QGC through a USB cable and wait for connection.
- **Step 3:** In QGC, change the power parameter from a 3S battery to a 4S battery.
- **Step 4:** QGC will alert "dangerously low battery, system SHUTDOWN".
- **Step 5:** You cannot perform most calibration/parameter update actions. QGC alerts "Transition denied, SHUTDOWN to INIT". You need to unplug the battery and reboot to resolve.

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2 (MindRacer scenario):** QGC alerts "dangerously low battery, system SHUTDOWN".
- **Behavior after step 3 (MindRacer scenario):** Unable to perform calibration/parameter updates, receive "Transition denied" alerts.
- **Behavior after step 2 (Other FCUs scenario):** N/A
- **Behavior after step 3 (Other FCUs scenario):** QGC alerts "dangerously low battery, system SHUTDOWN".
- **Behavior after step 4 (Other FCUs scenario):** Unable to perform calibration/parameter updates, receive "Transition denied" alerts until battery disconnect and reset.

**Expected behavior:**

- **Expected behavior 1:** Avoid entering "dangerously low battery, system SHUTDOWN" status when USB is connected.
- **Expected behavior 2:** Be able to perform calibration and parameter update actions without encountering shutdown alerts.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Suggested fixes include adding `system_power.usb_connected` detection in the `battery_status_check()` function and revising the implementation of `shutdown_if_allowed()`.
- **URL of the flight log provided by the user:** Not provided.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Suggestion to try fix with PR #14825.
- **Result of the operation after the user adopted suggestion 1:** Fixed as confirmed by developer `dagar` in comment mentioning fix in PR #14825.
