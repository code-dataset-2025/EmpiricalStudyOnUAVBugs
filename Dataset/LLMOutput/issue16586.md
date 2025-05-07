需求：无人车机架、电机

**Environment where the bug occurred:**

- **Hardware environment:** Just a generic rover frame with Pixhawk 4 - PX4_FMU_V5 with a brushless motor and an ESC.
- **Software environment:** Not explicitly mentioned.
- **Report Time:** Jan 19, 2021
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**59a1148

**Steps for bug reproduction:**

- **Step 1:** Upload any mission to a rover that is working in stabilized mode.
- **Step 2:** Switch to mission mode (either from the transmitter or from QGroundControl (QGC)).
- **Step 3:** Observe the rover transitioning to mission mode as shown in QGC.
- **Step 4:** Monitor for actuator responses.

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** N/A
- **Behavior after step 3:** Rover transitions to mission mode as expected on QGC.
- **Behavior after step 4:** Actuators do not respond, and the rover stands still.

**Expected behavior:**

- **Expected behavior 1:** Rover should navigate the mission autonomously as it does in the Software In The Loop (SITL) simulation.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Investigated some parts of the source code, discussed with developers, and referenced logs where similar setups worked in previous software versions (1.10 and 1.10.1).
- **URL of the flight log provided by the user:**
  - [Log for the reported issue](https://review.px4.io/plot_app?log=a108e8e8-a0b8-41ce-93b5-8ed9ef1a7720)
  - [Logs for versions where it functioned correctly](https://review.px4.io/plot_app?log=c4644c1d-429c-45d7-bedf-6d7232049573) and [another link](https://review.px4.io/plot_app?log=dc6f2043-ca7f-4c29-b350-6d137e86e630)

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Check the assumptions in the code since it's not an algorithmic problem if it works in SITL.
- **Result of the operation after the user adopted suggestion 1:** Unclear, further debugging was required.
- **Suggestion 2 provided by developers or other personnel:** Consider debugging why zero actuator controls are being published.
- **Result of the operation after the user adopted suggestion 2:** No direct outcome noted, but further code and real vehicle testing were implied.
- **Further suggestions and results:** In-depth code inspection and debugging to ascertain the root cause behind the disparity between SITL and real vehicle performance.
