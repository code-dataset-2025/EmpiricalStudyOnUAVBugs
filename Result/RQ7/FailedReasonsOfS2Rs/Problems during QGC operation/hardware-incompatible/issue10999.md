**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned
- **Software environment:** PX4 1.8.2 with temporary terraranger fix (bus change)
- **Report Time:** Dec 6, 2018
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**d42fe18

**Steps for bug reproduction:**

- **With QGC:**
  - **Step 1:** Missconfigure sensor to trigger "MAG inconsistent," "High ACC bias," or any other preflight check error.<font color='red'>需要磁力传感器（同时需要飞控和外部GPS来触发不一致）</font>
  - **Step 2:** Power the copter with QGroundControl (QGC).
  - **Step 3:** Ear the feedback, see the LED.
  - **Step 4:** Try to arm, it fails.<font color='red'>QGC界面显示GPS错误，无法操作使其arm</font>
  
- **Without QGC:**
  - **Step 1:** Missconfigure sensor to trigger "MAG inconsistent," "High ACC bias," or any other preflight check error the same way as before.
  - **Step 2:** Power the copter without QGroundControl.
  - **Step 3:** Try to arm, it fails.
  - **Step 4:** Connect QGroundControl.
  - **Step 5:** Ear the feedback, see the LED.
  - **Step 6:** Try to arm, it fails.

**Observed behavior by the user:**

- **With QGC:**
  - **Behavior after step 1:** N/A
  - **Behavior after step 2:** Audible feedback is provided, and the LED blinks red indicating a preflight check failure.
  - **Behavior after step 3:** User observes feedback, LED status.<font color='red'>可能存在硬件不同，没有提及的LED和声音效果</font>
  - **Behavior after step 4:** Arming fails.

- **Without QGC:**
  - **Behavior after step 1:** N/A
  - **Behavior after step 2:** Silent failure, without LED or sound feedback for preflight errors.
  - **Behavior after step 3:** Arming fails.
  - **Behavior after step 4:** N/A
  - **Behavior after step 5:** Audible feedback provided, and the LED blinks red post-connecting QGC.
  - **Behavior after step 6:** Arming fails.

**Expected behavior:**

- **Expected behavior 1:** Have LED & sound feedback when a preflight check fails, even without a ground control station connected.
- **Expected behavior 2:** Continuation of LED/sound feedback for failed preflight checks until successful arming or cause resolution.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Explanation of behavior differences with and without QGroundControl.
- **URL of the flight log provided by the user:** Not provided.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `dagar` suggested consolidating the preflight checks and queried about improvements on current light and sound feedback.
- **Result of the operation after the user adopted suggestion 1:** User provided feedback suggesting beeping for failed checks and blinking when unable to arm, noting possible temporal issues with sensors at boot.
  
- **Suggestion 2 provided by developers or other personnel:** Developer `stale` marked the issue as stale and closed it after no additional activity.
- **Result of the operation after the user adopted suggestion 2:** N/A (no direct action by the user as the suggestion was automatic closure due to inactivity).
