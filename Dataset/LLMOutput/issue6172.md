**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned
- **Software environment:** Ubuntu 16.04 with GCC version 6.x, PX4 Autopilot (commit version not mentioned)
- **Report Time:** Dec 26, 2016
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**3a17c07

**Steps for bug reproduction:**

- **Step 1:** Run the command `make px4fmu-v4_default` on Ubuntu 16.04.
- **Step 2:** Observe the build process and note any errors that occur.

**Observed behavior by the user:**

- **Behavior after step 1:** The build process initiates with the scanning of dependencies and generation of necessary files.
- **Behavior after step 2:** The process fails with the error `/usr/bin/arm-none-eabi-ld: romfs.bin: not in ELF format` during the build of `romfs.o`.

**Expected behavior:**

- **Expected behavior 1:** The build process should complete successfully without errors.
- **Expected behavior 2:** The generated binary files should be in the correct format expected by the tools.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Attempted to build using the latest master branch; noted the Ubuntu 16.04 auto update to GCC version 6.x and provided version details of `arm-none-eabi-gcc`.
- **URL of the flight log provided by the user:** Not provided.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** LorenzMeier requested @dagar's help to look into the frequent build issues.
- **Result of the operation after the user adopted suggestion 1:** N/A (no specific actions derived from this communication).
- **Suggestion 2 provided by developers or other personnel:** jgoppert confirmed they could reproduce the issue and asked @davids5 for ideas.
- **Result of the operation after the user adopted suggestion 2:** N/A (no resolution from this communication).
- **Suggestion 3 provided by developers or other personnel:** LorenzMeier indicated that the problem was fixed on Dec 28, 2016.
- **Result of the operation after the user adopted suggestion 3:** iZhangHui tried building the latest master but reported that it still failed, indicating ongoing issues with GCC version.
