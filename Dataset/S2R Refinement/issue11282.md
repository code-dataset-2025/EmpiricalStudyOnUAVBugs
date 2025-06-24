**Environment where the bug occurred:**

- **Hardware environment:** nxp_fmuk66
- **Software environment:** PX4 Autopilot
- **Report time:** Jan 23, 2019
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**2ffb49b

**Steps for bug reproduction:**

- **Step 1:** Boot normally.
- **Step 2:** Remove and replace the SD card.
- **Step 3:** Type "reboot" on the console.

**Observed behavior by the user:**

- **Behavior after step 1:** System boots as expected.
- **Behavior after step 2:** System continues to operate.
- **Behavior after step 3:** System hangs.

**Expected behavior:**

- **Expected behavior 1:** The system should shutdown properly and not hang on reboot.
- **Expected behavior 2:** Callback on shutdown line 201 should be invoked.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Investigated the issue assuming the Work queue might be blocked; tagged another user for insight.
- **URL of the flight log provided by the user:** Provided by `redxeth`:
  - [Log 1](https://logs.px4.io/plot_app?log=6b2498a8-9dca-4188-ae70-cf94f29f2cad)
  - [Log 2](https://logs.px4.io/plot_app?log=e87514de-fc65-4c55-8451-9ba322496702)

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** `jarivanewijk` mentioned not removing/inserting SD card while powered and tested on the latest master with workqueue changes.
- **Result of the operation after the user adopted suggestion 1:** Consistent behavior as previous; temporary sensor failures reported.
- **Suggestion 2 provided by developers or other personnel:** `davids5` suggested testing with latest master (#13440).
- **Result of the operation after the user adopted suggestion 2:** `jarivanewijk` reported a new issue: FMU hangs at reboot without an SD card.
- **Suggestion 3 provided by developers or other personnel:** `davids5` asked if the unit had the latest bootloader.
- **Result of the operation after the user adopted suggestion 3:** `jarivanewijk` updated to the latest bootloader, resulting in no issues on the latest firmware, but problems persisted on stable 1.10.1 version.

