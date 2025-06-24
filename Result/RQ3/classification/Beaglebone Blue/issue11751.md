**Environment where the bug occurred:**

- **Hardware environment:** Beaglebone Blue
- **Software environment:** PX4 Autopilot
- **Report Time:** Mar 31, 2019
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**39d1751

**Steps for bug reproduction:**

- **Step 1:** Execute `make beaglebone_blue_cross`.
- **Step 2:** Use GCC toolchain `gcc-linaro-7.4.1-2019.02-x86_64_arm-linux-gnueabihf`.
- **Step 3:** Use library `librobotcontrol_1.0.4`.

**Observed behavior by the user:**

- **Behavior after step 1:** Compilation error due to `-Werror=cast-align`.
- **Behavior after step 2:** N/A
- **Behavior after step 3:** Specific error message: "librobotcontrol -> include/rc/mavlink/common/../protocol.h:280:49: error: cast from ‘const char*’ to ‘const uint16_t* {aka const short unsigned int*}’ increases required alignment of target type [-Werror=cast-align]".

**Expected behavior:**

- **Expected behavior 1:** Successful compilation without alignment errors.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Suggested a fix by using the `-Wno-cast-align` flag in `Firmware/cmake/px4_add_common_flags.cmake`.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `dagar` suggested ignoring the warning `-Wno-cast-align` on a per module/driver basis with an example provided in the `CMakeLists.txt` file.
- **Result of the operation after the user adopted suggestion 1:** N/A
- **Suggestion 2 provided by developers or other personnel:** Comment by `dagar` about the need to include Beaglebone in the CI system; later confirmed it was done.
- **Result of the operation after the user adopted suggestion 2:** Once Beaglebone was included in CI, it potentially helped prevent such issues in the future.

