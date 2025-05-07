**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned
- **Software environment:** PX4 Autopilot 1.13.0
- **Report Time:** Jul 12, 2022
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**e99da22

**Steps for bug reproduction:**

- **Step 1:** Set `SYS_CTRL_ALLOC` to 1 and `DSHOT_CONFIG` not to be 0.<font color='red'>sitl中找不到这两个参数，连接飞控板后再尝试，找不到第二个参数，将第一个参数设置为1后，结果显示baro 0 missing错误</font>
- **Step 2:** Check status of modules in console.

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** The Dshot module does not replace the pwm_out module, and the pwm_out module is still running.

**Expected behavior:**
- **Expected behavior 1:** The Dshot module should start up and replace the pwm_out module when `SYS_CTRL_ALLOC` is set to 1 with Dshot configurations.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** The user looked into the startup script and tried to remove the `pwm_out start` line, which disabled the pwm_out module but did not start the dshot module.
- **URL of the flight log provided by the user:** Not provided.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** The developer `bkueng` suggested using the QGC UI to configure the output to Dshot.
- **Result of the operation after the user adopted suggestion 1:** The user followed the suggestion, fixed the issue, and acknowledged the possibility of using both PWM and DSHOT protocols at the same time.
