**Environment where the bug occurred:**

- **Hardware environment:** WSL on Windows 10, tested on Ubuntu running directly on hardware
- **Software environment:** Not explicitly mentioned
- **Report time:** Oct 7, 2022
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**30150f7

**Steps for bug reproduction:**

- **Step 1:** Clone the PX4-Autopilot repository using `git clone https://github.com/PX4/PX4-Autopilot.git --recursive`.
- **Step 2:** Run the setup script with `./PX4-Autopilot/Tools/setup/ubuntu.sh`.
- **Step 3:** Execute `HEADLESS=1 make px4_sitl gazebo_boat`.

**Observed behavior by the user:**

- **Behavior after step 1:** Repository is cloned.
- **Behavior after step 2:** Environment is set up.
- **Behavior after step 3:** The simulation hangs with the output:

  ```bash
  INFO  [dataman] data manager file './dataman' size is 7866640 bytes
  PX4 SIM HOST: localhost
  INFO  [simulator_mavlink] Waiting for simulator to accept connection on TCP port 4560
  ```

**Expected behavior:**

- **Expected behavior 1:** PX4 SITL startup process should continue and connect to Gazebo for the boat model.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** 
  - User tested on Ubuntu running directly on hardware and observed the same behavior.
  - User verified that the bug does not exist in version v1.13.0 of PX4 by checking out that branch and following the same steps.
  - User found that the bug also occurs on the tag `pr-rover-ratesp`.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Jaeyoung-Lim mentioned that the issue was fixed in `PX4/PX4-SITL_gazebo-classic#917`.
- **Result of the operation after the user adopted suggestion 1:** Not mentioned in this document.
