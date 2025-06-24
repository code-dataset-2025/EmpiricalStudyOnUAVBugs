**Environment where the bug occurred:**

- **Hardware environment:** Pixhawk 2 fmuv2, Unmanned Pixhawk Autopilot Kit
- **Software environment:** PX4 Autopilot with FW Version 1.7.2 custom build
- **Report Time:** May 5, 2020
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**682aa70

**Steps for bug reproduction:**

- **Step 1:** Perform a catapult launch with the setup described.
- **Step 2:** Attempt to observe PWM signal sent to the ESC and motor during launch.

**Observed behavior by the user:**

- **Behavior after step 1:** During 55 test flights, there were 2 instances of misfire at catapult launch. It appeared that PWM signals were not sent to the ESC and motor did not start.
- **Behavior after step 2:** In some launches, the motor failed to start, indicating potential issues with PWM signal dispatch.

**Expected behavior:**

- **Expected behavior 1:** The motor should consistently start upon catapult launch.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** 
  - Provided flight logs for both misfires and successful launches.
  - Investigated and considered parameters like LAUN_CAT_A (Catapult accelerometer threshold) potentially being set too high.
  - Explored if the issue could be related to GPS connectivity, especially concerning arming options without GPS.
  - Mentioned a temporary fix involving 'px4io stop' and 'px4io start' commands.

- **URL of the flight log provided by the user:**
  - [Log of misfire](https://review.px4.io/plot_app?log=530849b9-21cb-4097-9acb-cf0d311b97bf)
  - [Another log of misfire](https://review.px4.io/plot_app?log=b78cdaff-b13b-43a9-8d57-0168c43b90e7)
  - [Successful launch log](https://review.px4.io/plot_app?log=fb8b6e04-6f15-4f3d-af5d-467ec1546217)

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `julianoes` suggested comparing logs of successful and unsuccessful launches to identify differences and mentioned the acceleration spike.
- **Result of the operation after the user adopted suggestion 1:** User `MartinStokelj` provided additional successful launch logs for comparison.

- **Suggestion 2 provided by developers or other personnel:** Developer `dagar` suggested syncing with the master branch to add more px4io logging.
- **Result of the operation after the user adopted suggestion 2:** Pending actions as the internal px4io state wasn't logged, thus more monitoring instrumentation was recommended.
