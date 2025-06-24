**Environment where the bug occurred:**

- **Hardware environment:** Crazyflie 2.0
- **Software environment:** PX4 Autopilot
- **Report time:** Jan 15, 2020
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**d6cff80

**Steps for bug reproduction:**

- **Step 1:** Compile the default PX4 firmware for the Crazyflie 2.0.
- **Step 2:** Connect your computer to the vehicle via a USB port and flash the vehicle.
- **Step 3:** Try to connect to the nsh console using the command `./Tools/mavlink_shell.py /dev/ttyACM0`.

**Observed behavior by the user:**

- **Behavior after step 1:** Successful compilation.
- **Behavior after step 2:** Firmware is flashed to the vehicle.
- **Behavior after step 3:** The connection gets stuck after displaying "Connecting to MAVLINK..." with no error message displayed.

**Expected behavior:**

- **Expected behavior 1:** The connection succeeds.
- **Expected behavior 2:** The console displays `nsh>`.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Performed a bisection on the firmware commits to identify the merge causing the issue. Attempted to connect multiple times and provided reproduction steps.
- **URL of the flight log provided by the user:** Not provided.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `dagar` indicated plans to order hardware for debugging and add it to the test rack.
- **Result of the operation after the user adopted suggestion 1:** N/A (No direct action noted from the user based on this).
- **Suggestion 2 provided by developers or other personnel:** Developer `dagar` mentioned on Jul 27, 2020, that the issue should be fixed in #15421.
- **Result of the operation after the user adopted suggestion 2:** The issue was closed, implying it was resolved by this update.
