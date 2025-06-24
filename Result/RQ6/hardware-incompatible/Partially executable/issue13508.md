Here’s the extracted report based on the given format for the issue titled **EKF gps hgt timeout - reset to baro #13508**:

---

**Environment where the bug occurred:**

- **Hardware environment:** FMUv5
- **Software environment:** PX4 Autopilot
- **Report Time:** Nov 18, 2019
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**a172c3c

---

**Steps for bug reproduction:**

- **Step 1:** Encounter an environment where GPS data lags, possibly due to timing issues.<font color='red'>GPS数据延迟无法模拟</font>
- **Step 2:** Observe the `_gps_hgt_intermittent` flag being set to `true`.
- **Step 3:** Monitor the condition `_gps_hgt_intermittent = !((_time_last_imu - gps_init.time_us) < 2 * GPS_MAX_INTERVAL)`.

---

**Observed behavior by the user:**

- **Behavior after step 1:** The GPS height intermittency flag `_gps_hgt_intermittent` is activated despite a seemingly stable GPS connection.
- **Behavior after step 2:** EKF switches to barometric altitude (`reset to baro`), leading to GPS data being disregarded.
- **Behavior after step 3:** Issue appears difficult to reproduce, but a timing-related inconsistency is suspected.

---

**Expected behavior:**

- **Expected behavior 1:** The GPS connection should remain stable without triggering the `_gps_hgt_intermittent` flag unless there is an actual issue.
- **Expected behavior 2:** EKF should not reset to barometric altitude unless GPS data is genuinely unstable.

---

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** None explicitly mentioned in the report.
- **URL of the flight log provided by the user:** [Flight log link](https://review.px4.io/plot_app?log=d8997f75-e796-4a42-9b90-ea5c06a3d54d)

---

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** 
  - **Comment by `stale`:** The issue was marked as stale multiple times due to inactivity, with a note thanking the user for their contributions.
  - **Comment by `julianoes`:** Acknowledged the issue and flagged it for `@bresch`.
  - **Comment by `bresch`:** Mentioned that the issue has not been observed again and decided to close it.

- **Result of the operation after the user adopted suggestion 1:** 
  - No further input was received from the user, and the issue was closed.

---

Let me know if you need additional formatting or details!
