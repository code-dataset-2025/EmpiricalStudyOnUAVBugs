**Environment where the bug occurred:**

- **Hardware environment:** Pixhawk4 + GPS pixhawk 4 + Holybro telemetry
- **Software environment:** PX4 Autopilot v1.11.0-beta1
- **Report Time:** Apr 14, 2020
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**d5e0a52

**Steps for bug reproduction:**

- **Step 1:** Configure MAV_1_CONFIG to TELEM2 with firmware version v1.11.0-beta1.<font color='red'>需要电调</font>
- **Step 2:** Use "mavlink inspector" in QGC to observe GPS_RAW_INT.
- **Step 3:** Attempt to change the flight mode from ALTITUDE to POSITION.
- **Step 4:** Repeat steps with different configurations as outlined in test cases (e.g., enable/disable MAV_1_CONFIG or MAV_2_CONFIG and test with different telemetry ports).

**Observed behavior by the user:**

- **Behavior after step 1:** GPS signal appears unstable, fluctuating between 0 and 5 Hz.
- **Behavior after step 2:** GPS data shows fluctuations, resulting in an inability to change the flight mode to POSITION, and lack of visible Green GPS LED light.
- **Behavior after step 3:** Flight mode change from ALTITUDE to POSITION is unsuccessful.
- **Behavior after step 4:** Similar errors and GPS warning messages are observed depending on the configuration used.

**Expected behavior:**

- **Expected behavior 1:** GPS signal should remain constant or nearly constant, similar to the behavior observed with older firmware versions (v1.8.2, v1.9.2, v1.10.2).
- **Expected behavior 2:** Successful change of flight mode from ALTITUDE to POSITION.
- **Expected behavior 3:** Visible Green GPS LED light indicating stable GPS signal.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Compared configurations with different firmware versions and provided flight logs for various test cases.
- **URL of the flight log provided by the user:** 
  - [Case 1 log](https://review.px4.io/plot_app?log=9764baca-ec06-40aa-b1ba-79719d0b75fc)
  - [Case 2 log](https://review.px4.io/plot_app?log=a670c429-592e-4e52-a200-b811bd45f14d)
  - [Case 3 log](https://review.px4.io/plot_app?log=98b8c1ec-d492-48b5-823a-870af29e5686)
  - [Case 7 log](https://review.px4.io/plot_app?log=29bea816-da9d-4cd4-b042-c0fdb14e489d)

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `bkueng` acknowledged the issue and mentioned being able to reproduce it, suggesting disabling TX DMA (CONFIG_USART3_TXDMA) on Telem2.
- **Result of the operation after the user adopted suggestion 1:** Not explicitly mentioned, awaiting further tests.
- **Suggestion 2 provided by developers or other personnel:** Developer `davids5` isolated the problem and suggested re-testing with `#15528`.
- **Result of the operation after the user adopted suggestion 2:** Not mentioned, as `#15528` was a proposal for re-testing rather than a solution yet verified.
