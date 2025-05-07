**Environment where the bug occurred:**

- **Hardware environment:** INTEL AERO RTF
- **Software environment:** PX4 Autopilot version v1.11.0-beta1-144-g5dfc8f1
- **Report Time:** Jan 5, 2020
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**ce1e976

**Steps for bug reproduction:**

- **Step 1:** Execute the command `make intel_aerofc-v1_default`.

**Observed behavior by the user:**
- **Behavior after step 1:** Generates binary files for `modalai_fc-v1_default` inside the `build/intel_aerofc-v1_default` folder instead of `intel_aerofc-v1_default` binaries.

**Expected behavior:**
- **Expected behavior 1:** Correct binary generation for `intel_aerofc-v1_default` configuration.

**Additional information provided by the user for bug investigation:**
- **Actions taken by the user:** 
  - Removed and re-downloaded the entire Firmware repository.
  - Synchronized subprojects with `git submodule update --init --recursive`.
  - Identified a potential issue in `cmake/px4_config.cmake` where `intel_aerofc-v1_default` and `modalai_fc-v1_default` shared the same `fc-v1` model label, fixed by altering the CMake logic.

**Communication between developers or other personnel and the user:**
- **Suggestion 1 provided by developers or other personnel:** Developer `dagar` asked about reproducing the issue without external factors and suggested trying other build targets (e.g., `px4_fmu-v5_default`).
- **Result of the operation after the user adopted suggestion 1:** User confirmed that other targets built properly and identified the issue was reproducible even after a clean setup.
- **Suggestion 2 provided by developers or other personnel:** Asked if the issue persisted after cleaning the build and re-building.
- **Result of the operation after the user adopted suggestion 2:** User confirmed the issue persisted even after cleaning and updating submodules.
- **Suggestion n provided by developers or other personnel:** Developer `dagar` acknowledged the issue was fixed in #14123 without further troubleshooting from the user.

The solution identified by the user involved a configuration mismatch in the CMake setup that was later fixed in a subsequent Pull Request (#14123).
