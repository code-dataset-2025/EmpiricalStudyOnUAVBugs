# Basic Information:
### Title: Camera trigger not working with control allocation #20334 
### Issue status: Closed
### Author: Jaeyoung-Lim
### Issue open time: Sep 30, 2022

# Report
### Report author: Jaeyoung-Lim
### Report Time: Sep 30, 2022
### Report Content:   
**Describe the bug:**  
I have tried setting up the camera trigger with the control allocation, but I could not get it to work. I am using a Pixhawk 4 and attempting to trigger a Sony A7R camera using the Seagull UAV Sync2.  

**Expected behavior:**  
The camera triggers on command.  

**Steps for bug reproduction:**
- **Step 1:** Run `camera_trigger_test` in nsh.
- **Step 2:** Try to command the trigger using QGroundControl (QGC).  

**Observed behavior by the user:**
- **Behavior after step 1:** The camera does not trigger as expected.  
- **Behavior after step 2:** The camera does not respond to commands from QGC.  

**Additional information provided by the user for bug investigation:**
- **Actions taken by the user:** User shared outputs from the logs and `dmesg`, along with details of the hardware and settings.  
- **URL of the flight log provided by the user:** [Flight log](https://review.px4.io/plot_app?log=79032fc0-a74c-49ae-872e-f7e43db14428).

---

# Communication between developers or other personnel and the user:
### Suggestion 1 provided by developers or other personnel:
**Developer:** @bkueng  
**Suggestion:** This broke recently by reordering startup commands. Test PR #20362.

**Result of the operation after the user adopted suggestion 1:** No explicit response confirming the results of this test.

### Suggestion 2 provided by developers or other personnel:
**Developer:** @hamishwillee  
**Suggestion:** Verify whether the Seagull system requires two triggers as outlined in the [documentation](http://docs.px4.io/main/en/peripherals/camera.html#trigger-output-pin-configuration). Provide wiring details, trigger settings, and actuator screen images once resolved.  

**Result of the operation after the user adopted suggestion 2:**  
- User confirmed Seagull could work with one or two triggers. Two triggers were tried but with inconsistent results.  

### Suggestion 3 provided by developers or other personnel:
**Developer:** @saengphet  
**Suggestion:** Test on the master branch (as of Nov 22, 2022), which appears to fix the issue. Confirm compatibility and try merging fixes into v1.13.1.

**Result of the operation after the user adopted suggestion 3:**  
- Issue appears resolved on the current master branch (as of Nov 22, 2022). Further attempts were planned to merge the fix into v1.13.1.  

---

**Environment where the bug occurred:**
- **Hardware environment:** Pixhawk 4, Seagull UAV Sync2, Sony A7R camera.  
- **Software environment:** PX4 Autopilot v1.13.1.  
- **Report Time:** Sep 30, 2022.  
- **PX4 Autopilot commit version:** Not mentioned.  
- **last commit before the reporting time:**9b3cb6c

---

**Steps for bug reproduction:**
- **Step 1:** Run `camera_trigger_test` in nsh.  
- **Step 2:** Attempt to command the trigger using QGC.  

**Observed behavior by the user:**
- **Behavior after step 1:** The camera does not trigger as expected.  <font color='red'>执行结果需要连接相机才能验证</font>
- **Behavior after step 2:** The camera fails to respond to QGC commands.  

**Expected behavior:**

- **Expected behavior 1:** The camera should trigger upon executing the `camera_trigger_test` command.  
- **Expected behavior 2:** The camera should respond to commands issued through QGC.  

---

**Additional information provided by the user for bug investigation:**
- **Actions taken by the user:**  
  - User tested the configuration using `camera_trigger_test` and shared the outputs.  
  - User switched TRIG_INTERFACE settings from Seagull MAP2 to Generic PWM as a workaround.  
- **URL of the flight log provided by the user:** [Flight log](https://review.px4.io/plot_app?log=79032fc0-a74c-49ae-872e-f7e43db14428).  

**Communication notes:**  
- Multiple developers were involved, offering suggestions and workarounds.  
- The issue was resolved on the master branch as of Nov 22, 2022. Further testing and backporting to earlier versions were planned.
