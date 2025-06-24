**Environment where the bug occurred:**

- **Hardware environment:** Pixhawk 2.1
- **Software environment:** Not explicitly mentioned
- **Report Time:** Nov 17, 2017
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**a2b24fa

**Steps for bug reproduction:**

- **Step 1:** Connect a digital signal to AUX4.
- **Step 2:** Set FMU to capture mode (`fmu mode_pwm3cap1`).
- **Step 3:** Run `fmu test`.

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** N/A
- **Behavior after step 3:** The board freezes and/or reboots.

**Expected behavior:**

- **Expected behavior 1:** The FMU test should verify the functionality without causing the board to crash.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** The user notes differences between releases v1.5.5 and v1.6.5 and mentions reaching out to developers for assistance.
  
- **URL of the flight log provided by the user:** Not provided.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `davids5` inquires about the hardware environment and signal characteristics.
- **Result of the operation after the user adopted suggestion 1:** User `mhkabir` replies specifying the hardware and signal details being used.
- **Suggestion 2 provided by developers or other personnel:** Developer `davids5` shares testing results on today's master build on Pixhawk 2.1 CUBE, providing detailed system diagnostics and suggesting checking code for long threads off the ISR.
- **Result of the operation after the user adopted suggestion 2:** No explicit results or actions taken by the user are documented.
