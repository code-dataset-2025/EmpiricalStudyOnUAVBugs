**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned
- **Software environment:** Ubuntu 16.04 with PX4 Autopilot using arm-none-eabi-gcc (GNU Tools for Arm Embedded Processors 7-2018-q3-update) 7.3.1 and ccache 3.2.4<font color='red'>ubuntu版本及 ccache版本</font>
- **Report Time:** Aug 27, 2019
- **PX4 Autopilot commit version:** master@2f10c315b56f0bd9cb200956b112ad1f0930b90a

**Steps for bug reproduction:**

- **Step 1:** Checkout master@2f10c315b56f0bd9cb200956b112ad1f0930b90a.
- **Step 2:** Execute `make px4_fmu-v4_default`.

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** The build fails with an error message indicating an implicit fallthrough in the code, leading to compilation termination due to -Wfatal-errors.

**Expected behavior:**

- **Expected behavior 1:** The build should complete successfully without fallthrough errors.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Verified the arm-none-eabi-gcc version and ccache links. Attempted to clear ccache cache and identified that removing ccache resolved the issue.
- **URL of the flight log provided by the user:** Not provided.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Verified the gcc version and its installation path. Considered the impact of ccache on the build process.
- **Result of the operation after the user adopted suggestion 1:** Identified that the issue was related to ccache and removing it resolved the compile error.

- **Suggestion 2 provided by developers or other personnel:** Recommended using `export CCACHE_CPP2=yes` as a workaround.
- **Result of the operation after the user adopted suggestion 2:** The workaround seemed to work, allowing the build to proceed past the error.

- **Suggestion 3 provided by developers or other personnel:** Indicated updating ccache or disabling compile warnings as temporary fixes. Suggested adopting C++17 for better handling of fallthrough.
- **Result of the operation after the user adopted suggestion 3:** Not explicitly documented, but the issue seemed to be acknowledged with potential long-term solutions in the pipeline.
