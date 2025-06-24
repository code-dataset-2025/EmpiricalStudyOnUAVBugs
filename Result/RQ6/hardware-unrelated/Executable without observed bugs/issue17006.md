**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned
- **Software environment:** Not explicitly mentioned
- **Report Time:** Mar 2, 2021
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**72a3c05

**Steps for bug reproduction:**

- **Step 1:** Start `make px4_sitl jmavsim`.
- **Step 2:** Wait until the simulated GPS is accepted.
- **Step 3:** Command a takeoff.
- **Step 4:** Observe pitch oscillations when looking at either the level hovering vehicle's attitude in the visualization or the attitude indicator of the ground station.

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** N/A
- **Behavior after step 3:** N/A
- **Behavior after step 4:** Small but steady and fast oscillations in pitch in hover flight.

**Expected behavior:**

- **Expected behavior 1:** Nice smooth normal flight without oscillations.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** 
  - Investigated the influence of the IMU_DGYRO_CUTOFF value on the oscillations.
  - Explored the pitch gyro sensitivity with the default D-term gain.
- **URL of the flight log provided by the user:** 
  - TEST Flight 1: IMU_DGYRO_CUTOFF = 0 [https://logs.px4.io/plot_app?log=a13b6a53-1006-4d2a-bdbb-ff03040768ee](https://logs.px4.io/plot_app?log=a13b6a53-1006-4d2a-bdbb-ff03040768ee)
  - TEST Flight 2: IMU_DGYRO_CUTOFF = 10 [Default] [https://logs.px4.io/plot_app?log=f69ff845-f6fa-4704-a35f-57b922441f70](https://logs.px4.io/plot_app?log=f69ff845-f6fa-4704-a35f-57b922441f70)
  - TEST Flight 3: IMU_DGYRO_CUTOFF = 15 [https://logs.px4.io/plot_app?log=5c5ce078-834f-41fd-b03a-a4c9f6ae8c0f](https://logs.px4.io/plot_app?log=5c5ce078-834f-41fd-b03a-a4c9f6ae8c0f)

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `dagar` mentioned that the current defaults are intended to be relatively safe and suggested looking into vehicle_angular_acceleration in a typical user setup.
- **Result of the operation after the user adopted suggestion 1:** User `MaEtUgR` identified that IMU_DGYRO_CUTOFF being too low was the issue causing oscillations.
  
- **Suggestion 2 provided by developers or other personnel:** Discussion on the effect of IMU_DGYRO_CUTOFF on pitch sensitivity and the symmetry of the jMAVsim drone, showing caution in drawing conclusions without real-world test data.
- **Result of the operation after the user adopted suggestion 2:** User `MaEtUgR` noted that by adjusting IMU_DGYRO_CUTOFF, the flight behavior improved, indicating it should be set higher, possibly around 30.

- **Suggestion 3 provided by developers or other personnel:** User `mehmetyldz87` shared test results showing performance improvements with higher IMU_DGYRO_CUTOFF values.
- **Result of the operation after the user adopted suggestion 3:** Further confirmation that increasing IMU_DGYRO_CUTOFF improves pitch stability in the simulation.
