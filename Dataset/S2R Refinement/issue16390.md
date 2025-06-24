需求：step2需要四轴飞行器机架（这里是Twins V1）,step1内容看不懂

**Environment where the bug occurred:**

- **Hardware environment:** Pixhawk Holybro V4, Twins V1 Quadcopter with PM07 powerboard
- **Software environment:** PX4 Autopilot v1.11.2
- **Report Time:** Dec 15, 2020
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**5ccb8b4

**Steps for bug reproduction:**

- **Step 1:** Use the internal EKF2 estimator and feed 30Hz MoCap pose information via the mavlink vision topic.
- **Step 2:** Takeoff and let the copter hover in position control for a while.
- **Step 3:** Wait until the Pixhawk restarts (occurs after 20 seconds to 2 minutes).

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** N/A
- **Behavior after step 3:** The Pixhawk reboots, motors turn off, and the multicopter performs a hard landing.

**Expected behavior:**

- **Expected behavior 1:** The PX4/Pixhawk V4 should not restart.
- **Expected behavior 2:** The multicopter should maintain stable flight in position control without interruption.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Conducted tests to verify if the issue was related to the SD card by performing a sd_bench -r 50 test and removing the SD card.
- **URL of the flight log provided by the user:**
  - First file: [Short ~4 second period](https://logs.px4.io/plot_app?log=fab2c889-e3c8-4ff6-a6cf-6b5af31cd0ba)
  - Second file: [Longer flight period with software error notification](https://logs.px4.io/plot_app?log=a288b862-a60b-426c-af81-cf5b57629769)
  - Third file: [Short ~4 second period](https://logs.px4.io/plot_app?log=b5f2e049-dfbb-4b8b-bc7f-2b91eb25634a)

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `dayjaby` suggested verifying the SD card performance using sd_bench -r 50.
- **Result of the operation after the user adopted suggestion 1:** Chris-Bee found that the writing times were between 30-900ms, but the issue persisted without the SD card.
- **Suggestion 2 provided by developers or other personnel:** Developer `dagar` asked if any modifications were made to PX4 v1.11.2 and inquired about the method used to flash PX4.
- **Result of the operation after the user adopted suggestion 2:** Chris-Bee confirmed no modifications were made and that QGC was used for flashing.
- **Suggestion 3 provided by developers or other personnel:** N/A
- **Result of the operation after the user adopted suggestion 3:** The root cause was identified: incorrect wiring to the FMU DEBUG port, which was resolved by disconnecting the incorrect connections.
