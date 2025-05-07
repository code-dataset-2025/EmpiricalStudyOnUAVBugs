**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned
- **Software environment:** Linux Ubuntu 16.04, PX4 Autopilot v1.8.0-beta1
- **Report Time:** May 23, 2018
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**04cc5c5

**Steps for bug reproduction:**

- **Step 1:** Clone the repository using command: 
  
  ```bash
  git clone --recursive http://github.com/PX4/Firmware -b v1.8.0-beta1 PX4.1.8.0b
  ```
- **Step 2:** Go to the directory: 
  ```bash
  cd PX4.1.8.0b
  ```
- **Step 3:** Build using:<font color='red'>可以执行并出现仿真界面但会出现ERROR [sensors] no ADC found: /dev/adc0 (9)</font>
  
  ```bash
  make -j8 posix gazebo_iris_opt_flow
  ```
- **Step 4:** Launch using:
  
  ```bash
  roslaunch mavros px4.launch fcu_url:="udp://:14540@127.0.0.1:14557"
  ```
- **Additional Steps:** Run a mission: `goto(3,0,0)`, `goto(6,0,0)`, `goto(0,0,0)`<font color='red'>这一步命令无法执行，飞机无法执行arm以外的操作</font>

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** N/A
- **Behavior after step 3:** With PX4Flow, real-time factor drops to as low as 0.02 when the copter moves.
- **Behavior during mission:** When hovering, real-time factor is 1.0; without PX4Flow, it remains 1.0.

**Expected behavior:**

- **Expected behavior 1:** Real-time factor should stay at 1.0 during the whole offboard mission even with PX4Flow.
- **Expected behavior 2:** Consistent simulation performance between v1.7.3 and v1.8.0-beta1 with PX4Flow in use.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** User provided detailed steps for reproducing the issue and comparisons between different versions.
- **URL of the flight log provided by the user:** Not provided.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `dagar` suggested profiling using tools like flamegraphs and checking the results using top or htop.
- **Result of the operation after the user adopted suggestion 1:** User AlexisTM mentioned interest in using flamegraphs but no follow-up result provided.

- **Suggestion 2 provided by developers or other personnel:** `TSC21` suggested using the `asphalt_plane` world instead.
- **Result of the operation after the user adopted suggestion 2:** `AlexisTM` confirmed the issue persists as both branches use the same world; `mhkabir` mentioned that the issue specifically occurs in the `uneven_ground` world.

- **Suggestion 3 provided by developers or other personnel:** Discussion on potentially submitting a workaround PR and understanding the terrain model impact on performance.

- **Result of the operation after the user adopted suggestion 3:** In later comments, `AlexisTM` reported that changing to the `even_ground` world resolved the issue, indicating it could be closed.
