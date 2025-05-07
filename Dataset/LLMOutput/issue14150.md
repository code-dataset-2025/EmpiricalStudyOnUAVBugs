**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned
- **Software environment:** Not explicitly mentioned
- **Report Time:** Feb 13, 2020
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**abd2bb4

**Steps for bug reproduction:**

- **Step 1:** Replace the maintainer line of an airframe configuration, e.g., https://github.com/PX4/Firmware/blob/master/ROMFS/px4fmu_common/init.d/airframes/4001_quad_x#L20, with "# Some comment".
- **Step 2:** Execute `make clean`.
- **Step 3:** Build using `make px4_fmu-v5`.
- **Step 4:** See error.

**Observed behavior by the user:**
- **Behavior after step 1:** N/A
- **Behavior after step 2:** N/A
- **Behavior after step 3:** N/A
- **Behavior after step 4:** The parser fails unexpectedly with an error.

**Expected behavior:**
- **Expected behavior 1:** The parser should still work without a maintainer tag.
- **Expected behavior 2:** Alternatively, the parser should ask for a maintainer but not fail unexpectedly.

**Additional information provided by the user for bug investigation:**
- **Actions taken by the user:** The user described the steps for reproducing the issue and provided a detailed error log.
- **URL of the flight log provided by the user:** Not provided.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** `JacobCrabill` suggested adding a "@desc" tag to allow comments ignored by the parser.
- **Result of the operation after the user adopted suggestion 1:** Not provided (suggestion was a proposal for a potential solution).
  
- **Suggestion 2 (PR) provided by developers or other personnel:** `JacobCrabill` mentioned the possibility of submitting a pull request for this solution, albeit being a small change.
- **Result of the operation after the user adopted suggestion 2:** Not provided (no indication of adoption or implementation in the provided content).
