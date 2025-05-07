**Environment where the bug occurred:**

- **Hardware environment:** MRobotics Control Zero H7
- **Software environment:** PX4 Autopilot with commit 2cb4ef0
- **Report Time:** Dec 19, 2022
- **PX4 Autopilot commit version:** 2cb4ef0

**Steps for bug reproduction:**

- **Step 1:** Flash commit 2cb4ef0 onto the control zero h7 with the command `make mro_ctrl-zero-h7 upload`.
- **Step 2:** Open QGroundControl (QGC) and try to do the setup.

**Observed behavior by the user:**

- **Behavior after step 1:** The system is flashed with the specified commit.
- **Behavior after step 2:** Unable to select an airframe in QGC, and in the nutt-shell, the `dmesg` command only returns "NuttShell (NSH) NuttX-11.0.0."

**Expected behavior:**

- **Expected behavior 1:** System should work normally.
- **Expected behavior 2:** Ability to select an airframe in QGC without errors.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Conducted a quick bench test with a patch to configure everything and spun the motors without receiving errors.
- **URL of the flight log provided by the user:** Not provided.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `PetervdPerk-NXP` provided a patch named `mro_fix_nx_10_4.patch` for testing.
- **Result of the operation after the user adopted suggestion 1:** The patch worked for both commit 2cb4ef0 and the current main branch (9c66f1b). The user reported successful configuration and motor testing, although no proper flight test was conducted.
- **Additional Information by the developer**: Developer `PetervdPerk-NXP` explained that the issue was due to the upgrade of the NuttX kernel, which missed some targets in the configuration update. Configuration comparisons with other targets (FMU-V6X) were used to fix the issue.
- **Additional Comment by another user:** User `gorghino` mentioned that this issue was a duplicate of #20743.
