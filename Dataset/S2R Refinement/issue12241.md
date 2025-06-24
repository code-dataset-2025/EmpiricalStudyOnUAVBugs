**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned
- **Software environment:** PX4 Autopilot post version 1.9
- **Report Time:** Jun 11, 2019
- **PX4 Autopilot commit version:** 3faab90

**Steps for bug reproduction:**

- **Step 1:** Run the MAVSDK integration test against jMAVSim SITL using the command:<font color='red'>命令无法执行，显示未知参数-j8，去掉这个参数之后执行显示没有build/src/integration_tests/integration_tests_runner这个文件或目录</font>
  
  ```bash
  cmake -Bbuild -H. && cmake --build build -j8 && build/src/integration_tests/integration_tests_runner --gtest_filter="SitlTest.OffboardAttitudeRate"
  ```

**Observed behavior by the user:**

- **Behavior after step 1:** Offboard control mode is rejected with a temporary command rejection (176), and the test fails with a discrepancy between the expected and actual results.

**Expected behavior:**

- **Expected behavior 1:** The offboard control mode should successfully start, matching the expected result of `Offboard::Result::SUCCESS`.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Utilized git bisect to identify commit 3faab90 as the regression point.
- **URL of the flight log provided by the user:** Not provided.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `dagar` agreed to look into the issue and proposed running tests directly against PX4/Firmware.
- **Result of the operation after the user adopted suggestion 1:** Not explicitly mentioned.
- **Suggestion 2 provided by developers or other personnel:** Developer `dagar` inquired about the general requirements for offboard control mode.
- **Result of the operation after the user adopted suggestion 2:** The user, `julianoes`, confirmed the necessity of having an offboard setpoint set prior to switching modes.
