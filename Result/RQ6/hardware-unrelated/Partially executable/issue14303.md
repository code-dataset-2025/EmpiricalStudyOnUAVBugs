**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned
- **Software environment:** PX4 Autopilot 
- **Report Time:** Mar 5, 2020
- **PX4 Autopilot commit version:** 2b087a9

**Steps for bug reproduction:**

- **Step 1:** Checkout the master branch on commit 2b087a9.
- **Step 2:** Run `make px4_sitl jmavsim`.
- **Step 3:** Immediately switch to altitude mode and take off by pushing up with the stick.<font color='red'>jmavsim中缺少遥感</font>
- **Step 4:** Refrain from moving the sticks and observe the drone's behavior.

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** N/A
- **Behavior after step 3:** The drone takes off.
- **Behavior after step 4:** The drone experiences fast and extreme pitch oscillation for multiple seconds.

**Expected behavior:**

- **Expected behavior 1:** The drone should have stable flight from the beginning without pitch oscillations.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** User suspects simulator issues related to setting sensor update rate according to HIL_SENSOR bitmask and intends to conduct further testing.
- **URL of the flight log provided by the user:** [Log file link](https://logs.px4.io/plot_app?log=44c727a2-9b7c-43e7-b86d-f4d58e5e50d3)

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `dagar` discusses past iterations involving the LPF and sensor data handling to approximate real system conditions.
- **Result of the operation after the user adopted suggestion 1:** N/A (the discussion is aimed at understanding the issue rather than providing a direct operational solution for the user).
- **Suggestion 2 provided by developers or other personnel:** Developer `LucaMex` shares observations about error occurrence in relation to lockstep usage.
- **Result of the operation after the user adopted suggestion 2:** N/A
- **Suggestion 3 provided by developers or other personnel:** Developer `TSC21` indicates that the issue is also reproducible in other environments like Gazebo.
- **Result of the operation after the user adopted suggestion 3:** N/A
