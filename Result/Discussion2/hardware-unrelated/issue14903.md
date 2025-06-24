**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned
- **Software environment:** Not explicitly mentioned
- **Report Time:** May 14, 2020
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**19bbea7

**Steps for bug reproduction:**

- **Step 1:** Set parameters `NAV_RCL_ACT` to `0` and `NAV_DLL_ACT` to `0`.
- **Step 2:** Set `MIS_TAKEOFF_ALT` to `2.5`.
- **Step 3:** Execute the command `commander takeoff`.
- **Step 4:** Use the command `listener local_position -n 1`.

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** N/A
- **Behavior after step 3:** The multicopter does not reach the correct takeoff altitude and switches to HOLD mode prematurely.
- **Behavior after step 4:** N/A (the step is for observation)

**Expected behavior:**

- **Expected behavior 1:** The multicopter should reach the specified takeoff altitude of `MIS_TAKEOFF_ALT` as it used to.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Noted the apparent relation with `MIS_TAKEOFF_ALT - NAV_MC_ALT_RAD` and attempted a "fix" by setting `NAV_MC_ALT_RAD` to `0.05`.
- **URL of the flight log provided by the user:** [Flight Log](https://logs.px4.io/plot_app?log=eaae3517-b6bd-460a-be32-a2eae6506eb0)

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `julianoes` tagged `@MaEtUgR` possibly for awareness or action.
- **Result of the operation after the user adopted suggestion 1:** N/A

- **Suggestion 2 provided by developers or other personnel:** `stale` bot automated message marking the issue as stale due to inactivity.
- **Result of the operation after the user adopted suggestion 2:** N/A; issue closed later by the author `julianoes` noting that the discrepancy was minor (5 cm) and parameter dependence was resolved.
