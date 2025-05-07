**Environment where the bug occurred:**

- **Hardware environment:** Simulation
- **Software environment:** Master branch of PX4 Autopilot as of Mar 25, 2020
- **Report Time:** Mar 25, 2020
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**44bec26

**Steps for bug reproduction:**

- **Step 1:** Change parameters: `BAT_LOW_THR` to 30%, `BAT_EMERGEN_THR` to 20%, `BAT_CRIT_THR` to 10%, `COM_LOW_BAT_ACT` to 3, `RTL_RETURN_ALT` to 100m, `SIM_BAT_MIN_PCT` to 0%.<font color='red'>未注明运行环境是哪个仿真环境或是实机</font>
- **Step 2:** Take-off.
- **Step 3:** Fly to another location.
- **Step 4:** Climb to 20m.
- **Step 5:** Wait until the battery reaches ~30% and start landing.

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** N/A
- **Behavior after step 3:** N/A
- **Behavior after step 4:** N/A
- **Behavior after step 5:** The emergency return-to-launch (RTL) was initiated, starting with climbing, interrupting the landing process.

**Expected behavior:**

- **Expected behavior 1:** If the drone has already started landing, it should not initiate RTL.
- **Expected behavior 2:** It should not re-initiate the landing process once it's started.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** The user manually controlled the drone with RC to land it.
- **URL of the flight log provided by the user:** [Log File](https://review.px4.io/plot_app?log=c50117f1-3f81-4141-af5f-5e905ea239e5)

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** @julianoes referred the issue to @RomanBapst for possibly better insights.
- **Result of the operation after the user adopted suggestion 1:** N/A, as this was just an assignment to another developer.
- **Suggestion 2 provided by developers or other personnel:** None explicitly mentioned in the comments.
- **Result of the operation after the user adopted suggestion 2:** N/A

Note: The issue was automatically marked as stale twice due to inactivity but was considered still relevant by the user.
