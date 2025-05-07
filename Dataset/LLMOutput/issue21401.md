**Environment where the bug occurred:**

- **Hardware environment:** OmnibusF4SD and BLHeli_32 4 in 1 ESC
- **Software environment:** Latest main branch of PX4 Autopilot
- **Report Time:** Mar 30, 2023
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**93ba7de

**Steps for bug reproduction:**

- **Step 1:** Compile the firmware using `make omnibus_f4sd_default`.
- **Step 2:** Flash the firmware onto the board with QGroundControl (QGC).
- **Step 3:** Open the NSH console and start the dshot module with `dshot start`.
- **Step 4:** Check the status with `dshot status`.

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** The firmware is flashed onto the board.
- **Behavior after step 3:** The dshot module does not start and remains "Not Running".
- **Behavior after step 4:** The motors do not spin; the file `/dev/pwm_output0` is not present.

**Expected behavior:**

- **Expected behavior 1:** The dshot module should start correctly.
- **Expected behavior 2:** The motors should spin when the drone is armed.
  

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** The user modified the build configuration by adding EKF2 and removing the GPS driver. The user also checked the NSH console and noted the missing `/dev/pwm_output0` file.
- **URL of the flight log provided by the user:** Not provided.

**Communication between developers or other personnel and the user:**

- Suggestion and results are not mentioned in the provided document.
