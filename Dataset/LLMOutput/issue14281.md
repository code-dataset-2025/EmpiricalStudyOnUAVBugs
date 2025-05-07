**Environment where the bug occurred:**

- **Hardware environment:** Cube with Pixhawk2.1, Pixhawk 4 board
- **Software environment:** 
  - PX4 Firmware versions: 1.10.1, 1.9.2, 1.11.1
  - QGroundControl (QGC) Version: v4.0.10
  - AirSim
- **Report Time:** Mar 2, 2020
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**862cb20

**Steps for bug reproduction:**

- **Step 1:** Fresh flash a Pixhawk2.1 Cube with 1.10.1.
- **Step 2:** Select HIL Quadcopter X.
- **Step 3:** Reboot the system.

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** N/A
- **Behavior after step 3:** The system shows missing parameters error for BAT_V_CHARGED, BAT_N_CELLS, and BAT_V_EMPTY as preflight requirements when attempting HITL (Hardware-in-the-loop).

**Expected behavior:**

- **Expected behavior 1:** The system should not require the battery parameters to be set as it is running HITL.
- **Expected behavior 2:** The user should be able to perform HITL without encountering parameter errors blocking usage.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:**
  - Used 2 USB connections to start both AirSim and QCG.
  - Attempted re-flashing the board.
  - Re-installed QGC.
  - Reset all parameters on the board.
  - Set the CBRK_SUPPLY_CHK to 894281 to bypass supply check.
  
- **URL of the flight log provided by the user:** Not provided.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `julianoes` suggested using the parameter `CBRK_SUPPLY_CHK` to work around the preflight errors.
- **Result of the operation after the user adopted suggestion 1:** User `depauwjimmy` was able to start both AirSim and QCG using 2 USB connections, allowing for manual control with an Xbox controller, but encountered other issues with automatic landing and navigation errors.
- **Suggestion 2 provided by developers or other personnel:** Developer `dagar` noted on Aug 31, 2020, that the issue had been fixed.
- **Result of the operation after the user adopted suggestion 2:** User `McKayCyborg` reported on Oct 12, 2020, that the issue seemed to persist in the current PX4 firmware build 1.11.1 when using AirSim on a Pixhawk 4 board.
