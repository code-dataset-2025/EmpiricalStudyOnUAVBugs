Here’s the detailed output based on the provided bug report:

---

# Basic Information:
### Title:  "Accel Range, hold still on arming" on default typhoon simulation #19853 
### Issue Status: Closed
### Author: elpiel
### Issue Open Time: Jun 30, 2022

# Report
### Report Author: elpiel
### Report Time: Jun 30, 2022
### Report Content:  
**Describe the bug:**  
On a clean setup using the Typhoon H480 in SITL, I cannot arm the drone because I get a pre-flight error: "Accel Range, hold still on arming."  

**To Reproduce:**  
- **Step 1:** Run a docker container using `jonasvautherin/px4-gazebo-headless` with Typhoon H480 & baylands (I've tried with PX4 versions 1.12 and 1.13) using the command `-v typhoon_h480 -w baylands`.  
- **Step 2:** Connect to the drone using a ground control software like QGroundControl.  
- **Step 3:** Arm the drone.  
- **Step 4:** A pre-flight check error will appear: `[PreFlightCheck] Preflight Fail: Accel Range, hold still on arming`.  

**Expected Behavior:**  
- **Expected behavior 1:** SITL should work out of the box without pre-flight errors.  

**Log Files and Screenshots:**  
[Log File](https://logs.px4.io/plot_app?log=3badaede-a782-4882-b5de-85d2ecea3148)  

**Drone (please complete the following information):**  
- Typhoon H480  

**Additional Context:**  
- Related issue: #10852  

# Comment
## Comment 1
### Comment Author: elpiel
### Comment Time: Aug 9, 2022
### Comment Content:  
This issue is caused by the image itself (`jonasvautherin/px4-gazebo-headless`) when a non-existing world is used. Using the empty world works just fine. I don't know why the image does not contain `baylands`, but I hope this is useful to someone. 😃  

---

**Environment where the bug occurred:**
- **Hardware environment:** Typhoon H480 simulation in SITL
- **Software environment:** PX4 Autopilot (versions 1.12 and 1.13)
- **Report Time:** Jun 30, 2022
- **PX4 Autopilot Commit Version:** Not mentioned  
- **last commit before the reporting time:**f16ea92

**Steps for Bug Reproduction:**
- **Step 1:** Run a docker container using `jonasvautherin/px4-gazebo-headless` with Typhoon H480 & baylands (`-v typhoon_h480 -w baylands`).
- **Step 2:** Connect to the drone using QGroundControl.
- **Step 3:** Arm the drone.
- **Step 4:** Observe the pre-flight check error: `[PreFlightCheck] Preflight Fail: Accel Range, hold still on arming`.

**Observed Behavior by the User:**
- **Behavior after step 1:** Docker container runs successfully.
- **Behavior after step 2:** Connection to the drone is established.
- **Behavior after step 3:** Attempt to arm the drone initiates the pre-flight check.
- **Behavior after step 4:** The pre-flight check fails with the error: "Accel Range, hold still on arming."

**Expected Behavior:**
- **Expected behavior 1:** Drone should arm without errors in SITL.
- **Expected behavior 2:** SITL should work seamlessly with the default configurations.

**Additional Information Provided by the User for Bug Investigation:**
- **Actions taken by the user:** The user tested with different versions of PX4 (1.12 and 1.13) and identified that using an "empty world" bypasses the issue.  
- **URL of the flight log provided by the user:** [Flight Log](https://logs.px4.io/plot_app?log=3badaede-a782-4882-b5de-85d2ecea3148)  

**Communication Between Developers or Other Personnel and the User:**
- **Suggestion 1 provided by the user (to others):** Using an empty world in the `jonasvautherin/px4-gazebo-headless` image resolves the issue.
- **Result of the operation after the user adopted suggestion 1:** Issue resolved when using an empty world.
