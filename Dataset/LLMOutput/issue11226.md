**Environment where the bug occurred:**

- **Hardware environment:** Crazyflie 2.0 STEM Kit
- **Software environment:** Latest QGroundControl (QGC) on Linux
- **Report Time:** Jan 16, 2019
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**721f5e6

**Steps for bug reproduction:**

- **Step 1:** Get a Crazyflie 2.0 STEM Kit.
- **Step 2:** Flash the bootloader and upload PX4 as described in the [PX4 documentation for Crazyflie](https://docs.px4.io/en/flight_controller/crazyflie2.html).
- **Step 3:** Install the latest QGC on Linux and start it.
- **Step 4:** Attempt to connect through screen and gtkterm at various baud rates (115200, 57600, 921600).

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** The user is unable to get communication with QGroundControl.
- **Behavior after step 3:** N/A
- **Behavior after step 4:** User reports no MAVLink heartbeat or any communication over the serial terminal.

**Expected behavior:**

- **Expected behavior 1:** Successful communication between Crazyflie 2.0 and QGC.
- **Expected behavior 2:** Observation of MAVLink heartbeat on the serial terminal.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Tried reflashing the Crazyflie bootloader and checked different baud rates. Consulted previously reported issues for solutions.
- **URL of the flight log provided by the user:** Not provided.
- **Additional hardware noted:** Mention of lacking an SD-card expansion but later acquisition of another Crazyflie, SD-card, and debugging adapter.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `DanielePettenuzzo` suggested potentially not needing an SD-card expansion and planned to test when having access to the Crazyflie.
- **Result of the operation after the user adopted suggestion 1:** User realized the issue was due to installing the ranging board upside down, which affected the bootloader and MAVLink start.
- **Additional observations:** The user confirmed software version was not an issue and suspected potential hardware or procedural errors.
