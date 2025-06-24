Here is the extracted and formatted output for the provided bug report:

---

**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned
- **Software environment:** PX4 Autopilot version 1.8.1
- **Report Time:** Oct 28, 2018
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**a7d297e

**Steps for bug reproduction:**

- **Step 1:** Clone PX4 Autopilot version 1.8.1.
- **Step 2:** Change `EKF2_AID_MASK` to 24 in `ekf2/iris`.
- **Step 3:** Run SITL.
- **Step 4:** In the PX4 shell, run the command `pxh> listener vehicle_attitude`.
- **Step 5:** In the PX4 shell, run the command `pxh> listener vehicle_local_position`.

**Observed behavior by the user:**

- **Behavior after step 1:** PX4 SITL starts without any issues.
- **Behavior after step 4:** The command `listener vehicle_attitude` outputs `never published`.
- **Behavior after step 5:** The command `listener vehicle_local_position` outputs `never published`.

**Expected behavior:**

- **Expected behavior 1:** The EKF2 module should initialize the state even without vision position/yaw data.
- **Expected behavior 2:** The drone should correctly report being in STABILIZED mode instead of behaving like ACRO mode.
- **Expected behavior 3:** The drone should remain at a zero position until valid vision data or other inputs (e.g., barometer, rangefinder) become available.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** The user reproduced the issue in both real-world scenarios and SITL, provided reproduction steps, and suggested possible changes to the EKF2 behavior.
- **URL of the flight log provided by the user:** Not provided.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `dagar` suggested locking down the mode to require valid attitude data before arming or entering STABILIZED mode.
- **Result of the operation after the user adopted suggestion 1:** Not explicitly mentioned, as this was a discussion of potential solutions.
- **Suggestion 2 provided by developers or other personnel:** The user `okalachev` proposed having EKF2 estimate attitude without vision input, using either magnetometer yaw or a default yaw of 0, and adjusting the local position to (0, 0, 0).
- **Result of the operation after the user adopted suggestion 2:** Not applicable, as this was a proposal.
- **Suggestion 3 provided by developers or other personnel:** Developer `mhkabir` indicated that this functionality should already work as expected and promised to investigate the issue further.
- **Result of the operation after the user adopted suggestion 3:** Not provided, as the issue remained unresolved at that time.

---

Let me know if you need further adjustments or refinements!
