**Environment where the bug occurred:**

- **Hardware environment:** PixRacer and Pixhawk 2.4.5
- **Software environment:** PX4 Autopilot version 1.5.5 stable
- **Report Time:** Mar 11, 2017
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**32cf540

**Steps for bug reproduction:**

- **Step 1:** Set up the PixRacer without props and the PX4 1.5.5 stable version via QGroundControl.
- **Step 2:** Modify the `extras.txt` file with the following lines:
  - `vmount start`
  - `set MNT_MODE_IN 2`
  - `set MNT_MODE_OUT 0`
  - `set MNT_MAN_CONTROL 1`
  - `set MNT_MAN_PITCH 2`
- **Step 3:** Connect the telemetry link to a Linux machine using the Uart example code (https://github.com/mavlink/c_uart_interface_example).
- **Step 4:** After Take-off in manual mode, launch the UART example program.
- **Step 5:** Switch the flight mode to OFFBOARD using the program.

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** N/A
- **Behavior after step 3:** N/A
- **Behavior after step 4:** N/A
- **Behavior after step 5:** The system stops responding, QGroundControl loses connection, logging stops, and all fail-safes are ignored.

**Expected behavior:**

- **Expected behavior 1:** The system should continue to respond to RC inputs during OFFBOARD mode.
- **Expected behavior 2:** QGroundControl should maintain connection and continue logging while the drone operates in OFFBOARD mode.
- **Expected behavior 3:** Fail-safes should activate if necessary, ensuring drone safety.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** User reported testing on both PixRacer and Pixhawk 2.4.5.
- **URL of the flight log provided by the user:** Not provided.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer @LorenzMeier suggested increasing a parameter value to 1700 and re-testing the issue.
- **Result of the operation after the user adopted suggestion 1:** User reported no visible change in behavior.
