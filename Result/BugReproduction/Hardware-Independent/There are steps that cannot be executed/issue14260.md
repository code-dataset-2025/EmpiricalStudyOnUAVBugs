**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned
- **Software environment:** PX4 Autopilot version v1.9.2
- **Report Time:** Feb 28, 2020
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**f5000a9

**Steps for bug reproduction:**

- **Step 1:** Export parameters from the attached file.<font color='red'>从log文件导入参数</font>
- **Step 2:** Set up the environment for EKF2 replay.
- **Step 3:** Run `px4_sitl none`.
- **Step 4:** Examine the generated log file.
- **Step 5:** Expect drag innovations to exist.
- **Step 6:** Export parameters from the generated log file.

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** N/A
- **Behavior after step 3:** Log file is relatively long.
- **Behavior after step 4:** Drag innovations are zeroed.
- **Behavior after step 5:** EKF2_AID_MASK is 1 instead of 33.

**Expected behavior:**

- **Expected behavior 1:** Drag innovations should exist in the generated log file.
- **Expected behavior 2:** EKF2_AID_MASK should be 33 in the generated log file.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Not explicitly mentioned, but the user provided detailed steps and a URL for the flight log.
- **URL of the flight log provided by the user:** `log_27_2020-2-27-14-45-24.ulg.zip`

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** `vanurag` suggested adding 'replay tryapplyparams' in `rc.replay` before `ekf2 start`.
- **Result of the operation after the user adopted suggestion 1:** Not explicitly mentioned.
- **Suggestion 2 provided by developers or other personnel:** `bkueng` requested a pull request and mentioned that EKF does not take parameters after it's started.
- **Result of the operation after the user adopted suggestion 2:** Not explicitly mentioned.
- **Suggestion 3 provided by developers or other personnel:** Issue was automatically marked as stale, no further action indicated.
