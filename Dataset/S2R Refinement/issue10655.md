**Environment where the bug occurred:**

- **Hardware environment:** 
  - Tarot Peeper with T10x gimbal
  - Pixhawk 2.1 (Cube)
  - HERE GPS
- **Software environment:** Not explicitly mentioned
- **Report Time:** Oct 5, 2018
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**62d71bf

**Steps for bug reproduction:**

- **Step 1 (External Mag):** Enable only the external mag (set CAL_MAG0_EN = Enabled, and disable MAG1, MAG2, MAG3).
- **Step 2 (External Mag):** Set the CAL_MAG_PRIME parameter to the CAL_MAG0_ID.
- **Step 3 (External Mag):** Point the copter towards a physical direction (or north).
- **Step 4 (External Mag):** Check the computed north location.
- **Step 5 (External Mag):** Observe an offset between 120 and 180° for MAG0.

- **Step 1 (Internal MAG):** Enable only the MAG1, MAG2, MAG3.
- **Step 2 (Internal MAG):** Set the CAL_MAG_PRIME parameter to the CAL_MAGX_ID.
- **Step 3 (Internal MAG):** Point the copter towards a physical direction (or north).
- **Step 4 (Internal MAG):** Check the computed north location.
- **Step 5 (Internal MAG):** Observe an offset around 90° for all internal MAGs.

**Observed behavior by the user:**

- **Behavior after External Mag Step 1-5:** An offset between 120 and 180° for MAG0 is observed.
- **Behavior after Internal MAG Step 1-5:** An offset around 90° for all internal MAGs is observed.

**Expected behavior:**

- **Expected behavior 1:** The magnetometer readings should align with the physical direction the copter is pointed towards.
- **Expected behavior 2:** No significant offset should be observed in either external or internal magnetometer readings.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:**
  - Ensured HERE GPS is mounted with the arrow aligned with the Pixhawk 2.1 Cube arrow.
  - Verified external mag by disconnecting the HERE GPS and checked for MAG0 timeout.
- **URL of the flight log provided by the user:** Not provided

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `dagar` requested verification of the sensor type in the HERE GPS and suggested running listeners across all mags.
- **Result of the operation after the user adopted suggestion 1:** User confirmed HERE GPS is MAG0 and provided additional context with no changes in the observed issue.

- **Suggestion 2 provided by developers or other personnel:** Further investigation into the GPS mounting revealed potential documentation to examine a line of code that could be problematic.
- **Result of the operation after the user adopted suggestion 2:** User attempted additional debugging and discussed a possible wrong driver due to multiple versions available.

- **Suggestion 3 provided by developers or other personnel:** Discussed related rotational parameters (ROTATION_PITCH_180_YAW_90) for newer HERE GPS units.
- **Result of the operation after the user adopted suggestion 3:** Considerations were made around reorienting the compass, indicating that newer units might still encounter difficulties if improperly set.

- **Additional interactions:** Comments indicate ATV and component discrepancies. Additional test logs and compass behavior analysis were discussed in context.
