**Environment where the bug occurred:**

- **Hardware environment:** Tarot X6 (with Tarot retracts), Pixhawk Cube 2.1, Here2 GNSS
- **Software environment:** QGroundControl (QGC) 3.5.5, PX4 1.9.2
- **Report Time:** Oct 30, 2019
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**a6a8877

**Steps for bug reproduction:**

- **Step 1:** Power on and wait for GPS lock.
- **Step 2:** Upload mission. Mission End is set to "Return to Launch" using `gear-test.txt`.
- **Step 3:** Take off in mission mode.
- **Step 4:** Verify during testing at two locations, 4 flights each.

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** N/A
- **Behavior after step 3:** Landing gear properly retract upon takeoff.
- **Behavior after step 4:** During landing, gear do not start to deploy until the copter is around 1m above the ground.

**Expected behavior:**

- **Expected behavior 1:** Landing gear should be commanded to deploy when `RTL_DECEND_ALT`, `LAND_ALT_1`, or `LAND_ALT_2` is reached.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Investigated the code and identified potential cause in `_prepareLandSetpoints()` of `AutoMapper2` task in the PX4 code.
- **URL of the flight log provided by the user:** [Link to log](https://logs.px4.io/plot_app?log=c57c04e0-a6bd-4f04-9fe2-eb986cbcc1b4)

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `MaEtUgR` provided information on the source of the altitude check for automatic landing gear triggering.
- **Result of the operation after the user adopted suggestion 1:** The cause of the delay in gear deployment was identified, and the user found the trigger altitude hardcoded to 2m.
- **Suggestion 2 provided by developers or other personnel:** None explicitly mentioned related to further changes or fixes.
- **Result of the operation after the user adopted suggestion 2:** The linked pull request was merged, and the issue was closed as confirmed by the user `mwiatt` and `FlavioTonelli`.
