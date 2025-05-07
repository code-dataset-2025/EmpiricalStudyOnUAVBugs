需求：step5实机飞到30米

**Environment where the bug occurred:**

- **Hardware environment:** Pixracer, Pixhawk 4 mini, Pixhawk 4
- **Software environment:** PX4 Autopilot with commit version 7f3b170
- **Report Time:** Feb 7, 2019
- **PX4 Autopilot commit version:** 7f3b170<font color='red'>原报告需要实机飞行，且该提交编译sitl报错note:suggested time_.stop()->timer，改为timer后仍然报错</font>

**Steps for bug reproduction:**

- **Step 1:** Uploaded mission
- **Step 2:** Drone switched on
- **Step 3:** Vehicle armed
- **Step 4:** Took off
- **Step 5:** Elevated to 30 meters
- **Step 6:** Vehicle started spinning out of control
- **Step 7:** The vehicle came down and crashed

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** N/A
- **Behavior after step 3:** N/A
- **Behavior after step 4:** N/A
- **Behavior after step 5:** Vehicle started spinning out of control
- **Behavior after step 6:** The vehicle came down and crashed

**Expected behavior:**

- **Expected behavior 1:** The vehicle should maintain stable flight at 30 meters.
- **Expected behavior 2:** The vehicle should complete the mission without spinning or crashing.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Tested on different hardware platforms: Pixracer, Pixhawk 4 mini, Pixhawk 4
- **URL of the flight log provided by the user:**
  - Pixracer: [Flight log](https://review.px4.io/plot_app?log=4f0c2692-5f27-4d83-bfbd-765bf48a989e)
  - Pixhawk 4 Mini: [Flight log](https://review.px4.io/plot_app?log=53fa724b-906d-4e93-87fe-5a4f4c2a50b8)
  - Pixhawk 4: [Flight log](https://review.px4.io/plot_app?log=69f42b00-6259-4a97-96c1-bd8f06b4d29d)

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** `mhkabir` potentially linked the issue to #11376.
- **Result of the operation after the user adopted suggestion 1:** N/A
- **Suggestion 2 provided by developers or other personnel:** `dagar` conducted further investigation and identified issues related to math::max and navigator MissionBlock::get_time_inside().
- **Result of the operation after the user adopted suggestion 2:** Fixes worked in progress in #11411.
- **Suggestion 3 provided by developers or other personnel:** A review of packed structure usage was recommended.
- **Result of the operation after the user adopted suggestion 3:** The issue was ultimately addressed and resolved.
