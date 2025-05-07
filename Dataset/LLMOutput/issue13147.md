**Environment where the bug occurred:**

- **Hardware environment:** Holybro s500 kit
- **Software environment:** PX4 Autopilot firmware version v1.9.2 and master
- **Report Time:** Oct 9, 2019
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**ea35923

**Steps for bug reproduction:**

- **Step 1:** Use a Holybro s500 kit and attempt to fly with the PX4 master firmware.
- **Step 2:** Compare behavior when using the older firmware version v1.9.2.
- **Step 3:** Observe the actuator outputs during boot with an oscilloscope.

**Observed behavior by the user:**

- **Behavior after step 1:** Cannot fly with the PX4 master firmware; ESC issues are observed.
- **Behavior after step 2:** The kit works fine without any issue on v1.9.2.
- **Behavior after step 3:** Different actuator output signals between versions during boot.

**Expected behavior:**

- **Expected behavior 1:** The user expects no ESC issues between different PX4 firmware versions.
- **Expected behavior 2:** Consistent actuator outputs during boot across firmware versions.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Observed the actuator outputs using a scope, checked ESC firmware model, and identified signal discrepancies.
- **URL of the flight log provided by the user:** 
  - v1.9.2: https://review.px4.io/plot_app?log=7f7aba71-125c-4861-9b67-6ced2962f7a1
  - master: https://review.px4.io/plot_app?log=dccabbd4-65cd-4efd-bd10-421a9504dfb4

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** 
  - @davids5: Requested hardware to help investigate.
  - @MaEtUgR: Suggested trying through different configurations (400 Hz PWM, OneShot, DShot).

- **Result of the operation after the user adopted suggestion 1:** Investigation revealed vibrations possibly caused by motor shuddering; misconfigured setup was corrected.

- **Suggestion 2 provided by developers or other personnel:** 
  - @jkflying: Suggested providing high-rate logs for both firmware versions for comparison.

- **Result of the operation after the user adopted suggestion 2:** High-rate logs highlighted an issue with vibrations affecting gyro/accel readings, and changing IMU_GYRO_CUTOFF from 80 to 30 resolved the instability.

- **Further Suggestion:** 
  - @julianoes: Suggested performing a git bisect to identify when the change was introduced.
  - Result: Git bisect was initiated, but physical damage to the drone paused the process.

- **Resolution Discussion:**
  - @LorenzMeier: Explained changes in the filtering pipeline might be causing the observed differences between firmware versions, emphasizing differences in frame vibration characteristics.

- **Pending Action:** 
  - Further bisecting to pinpoint the exact cause of changes and verification of @LorenzMeier's explanation by @bkueng and @bresch is ongoing.
