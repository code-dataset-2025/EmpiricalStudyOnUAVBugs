Here is the detailed output for the provided bug report in the specified format:

---

**Environment where the bug occurred:**

- **Hardware environment:**  
  - Flight controller: CUAV V6X  
  - Drone type: Quad copter  
- **Software environment:**  
  - Firmware version: v1.14 (main branch Developer build master)  
  - Firmware v1.13 tested as a comparison (works fine)  
- **Report Time:** May 23, 2023  
- **PX4 Autopilot commit version:** Not mentioned  
- **last commit before the reporting time:**c903288

---

**Steps for bug reproduction:**

- **Step 1:** Flash the latest main branch (Developer build master) firmware in QGC.  
- **Step 2:** Set up the vehicle.  
- **Step 3:** Switch to Stabilized mode.  
- **Step 4:** Arm the vehicle.  
- **Step 5:** Push up throttle.  
- **Step 6:** Push down throttle.  

---

**Observed behavior by the user:**

- **Behavior after step 1:** Firmware flashed successfully.  
- **Behavior after step 2:** Vehicle setup completed.  
- **Behavior after step 3:** Stabilized mode enabled.  
- **Behavior after step 4:** Vehicle armed.  
- **Behavior after step 5:** Motor spin becomes very noisy and jerky.  
- **Behavior after step 6:** The motor spin remains noisy and jerky.  

---

**Expected behavior:**

- **Expected behavior 1:** Motors should spin smoothly with throttle pushed up.  
- **Expected behavior 2:** Motors should spin smoothly when throttle is pushed down.  
- **Expected behavior 3:** Motors should not exhibit noisy or jerky behavior at any throttle level.  

---

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:**  
  - Switched ESC PWM channels from `MAIN` to `AUX`.  
  - Re-flashed firmware to v1.14 and tested.  
  - Observed that the issue disappeared after the changes for three drones with the problem.  
  - Compared behavior with firmware v1.13, which worked fine consistently.  

- **URL of the flight log provided by the user:**  
  - Random bad motor spin video: `VID_20230522_171526_1.mp4`  
  - Random good motor spin video: `VID_20230523_111849_1.mp4`  
  - Video showing proper motor operation via QGC throttle: `VID_20230522_174228_1.mp4`  

- **Additional context provided:**  
  - The same issue occurred on another Hex Cube Orange flight controller drone with v1.14 firmware.  
  - v1.13 firmware consistently worked fine on both drones, with no restarting required.  

---

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:**  
  The user discovered and tested a solution: switching ESC PWM channels from `MAIN` to `AUX` and re-flashing the firmware to v1.14.  

- **Result of the operation after the user adopted suggestion 1:**  
  - Issue resolved for all three drones after several tests.  

- **Additional user follow-up:**  
  - The user planned further testing to confirm the fix is permanent.  

---
