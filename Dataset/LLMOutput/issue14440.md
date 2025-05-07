**Environment where the bug occurred:**

- **Hardware environment:** Inside Docker (specific hardware not mentioned)
- **Software environment:** PX4 Autopilot on Ubuntu 16.04
- **Report Time:** March 20, 2020
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**341dd6b

**Steps for bug reproduction:**

- **Step 1:** Try to build PX4 SITL on Ubuntu 16.04.
- **Step 2:** The build process fails at compiling `ekf_helper.cpp`.

**Observed behavior by the user:**

- **Behavior after step 1:** Build process is initiated.
- **Behavior after step 2:** Compilation fails due to an error related to `isfinite` not being declared.

**Expected behavior:**

- **Expected behavior 1:** Compilation should succeed without errors.
- **Expected behavior 2:** PX4 SITL should build successfully on Ubuntu 16.04.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Reproduced the issue inside Docker and provided detailed compilation error messages.
- **URL of the flight log provided by the user:** Not provided.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Comment by `TSC21` suggested using `PX4_ISFINITE()`.
- **Result of the operation after the user adopted suggestion 1:** `dusan19` commented that the issue compiles with the suggested change, indicating it resolved the problem.
