**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned
- **Software environment:** PX4 Autopilot
- **Report Time:** Apr 24, 2019
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**c95394f

**Steps for bug reproduction:**

- **Step 1:** Have `fastrtpsgen` in the PATH and `FASTRTPSGEN_DIR` not set.<font color='red'>安装fastrtpsgen的fast dds时遇到问题foonathan_memory.cmake缺失，按https://blog.csdn.net/tao_292/article/details/125317670修改命令后依然缺失</font>
- **Step 2:** Run `make px4_fmu-v3_rtps`.

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** The build fails with an error: `generate_microRTPS_bridge.py: error: argument -f/--fastrtpsgen-dir: expected one argument`.

**Expected behavior:**

- **Expected behavior 1:** The firmware should build successfully.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Identified that the issue is due to the `--fastrtpsgen-dir` option being set to `FASTRTPSGEN_DIR` in the `CMakeLists.txt`. Comments indicate that commenting the line causes `generate_microRTPS_bridge.py` to succeed.
- **URL of the flight log provided by the user:** Not provided.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `TSC21` suggested adding a condition to check if `FASTRTPSGEN_DIR` is set and, if not, to look in the default path. They mentioned this would be added as soon as possible.
- **Result of the operation after the user adopted suggestion 1:** N/A (the suggestion is a future action plan).
- **Suggestion 2 provided by developers or other personnel:** User `AlexisTM` proposed an alternative solution by allowing no data for `argparse`, using `nargs='?'`, which would result in a very small change.
- **Result of the operation after the user adopted suggestion 2:** N/A (it's a proactive suggestion from the user).
