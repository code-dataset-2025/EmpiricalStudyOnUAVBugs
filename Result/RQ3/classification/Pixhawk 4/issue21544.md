**Environment where the bug occurred:**

- **Hardware environment:** Hexacopter with Pixhawk 4
- **Software environment:** PX4 v1.13.2
- **Report Time:** May 3, 2023
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**9e5420b

**Steps for bug reproduction:**

- **Step 1:** Fly the hexacopter in Position mode.<font color='red'>需要hexacopter六轴飞行器类机架，stil中没有此类模型</font>
- **Step 2:** Observe the drone's behavior during flight.

**Observed behavior by the user:**

- **Behavior after step 1:** The drone started to spin uncontrollably, leading to a crash.
- **Behavior after step 2:** User observed a "Critical: Mag timeout error" in the error logs.

**Expected behavior:**

- **Expected behavior 1:** The drone should maintain stable flight in Position mode.
- **Expected behavior 2:** The drone should not experience uncontrollable spinning.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** 
  - Recalibrated the compass and replaced the Holybro M8N due to a "Mag timeout error."
  - Conducted tests without propellers to diagnose the issue further.
  - Changed cables suspected to be short-circuited and checked the motor tightness.

- **URL of the flight log provided by the user:**
  - [Log of crash](https://logs.px4.io/plot_app?log=5a129e78-ebf0-4ae1-a331-69c0af8ec51a)
  - [Log of previous flight 1](https://logs.px4.io/plot_app?log=a977375d-2e7f-4f74-bd5a-b9bf3b7155a3)
  - [Log of previous flight 2](https://logs.px4.io/plot_app?log=82b4db9e-08ad-4fc9-bd0f-3867701895f8)
  - [Log of test 1](https://logs.px4.io/plot_app?log=35ca6c2d-bd17-4dfc-8623-24aca53d2e6a)
  - [Log of test 2](https://logs.px4.io/plot_app?log=5ce89b7d-708f-42c7-9459-37c620d6f304)
  - [Log of subsequent test](https://logs.px4.io/plot_app?log=47a86a01-f5d1-4091-827c-fda1c99754d8)

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** N/A (The comments were mainly informational and from the user, Katawann, without intervention from other developers in the report).
- **Result of the operation after the user adopted suggestion 1:** N/A
- **Suggestion 2 provided by developers or other personnel:** N/A
- **Result of the operation after the user adopted suggestion 2:** N/A
- **Final conclusion by the user:** The spinning problem resulted from motors not being adequately tightened, which was corrected to prevent further issues.
