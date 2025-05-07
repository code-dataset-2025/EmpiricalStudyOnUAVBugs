**Environment where the bug occurred:**

- **Hardware environment:** HW arch: PX4_FMU_V4, MCU: STM32F42x, rev. 5
- **Software environment:** OS: NuttX, OS version: Release 10.0.0, FW git-hash: 38bc46f, FW version: 1.12.0, FW git-branch: master
- **Report Time:** Apr 22, 2021
- **PX4 Autopilot commit version:** not mentioned
- **last commit before the reporting time:**d631a5d

**Steps for bug reproduction:**

- **Step 1:** Arm the drone.
- **Step 2:** Observe the SD logging behavior across various flight controllers.

**Observed behavior by the user:**

- **Behavior after step 1:** SD logging stops shortly after the drone is armed.
- **Behavior after step 2:** Error messages indicating write failures to the SD card are observed.

**Expected behavior:**

- **Expected behavior 1:** A proper logfile should be created according to the SD log settings.
- **Expected behavior 2:** Logging should continue without stopping shortly after arming.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** The user observed that extended PWM limits seem to interfere with logging and also identified formatting the SD card as FAT32 as a potential workaround.
- **URL of the flight log provided by the user:** Not provided. Various logs were recalled and error messages shared in the comments.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** @davids5 acknowledged the issue and explored potential SD card or driver-related problems, tested with various hardware setups, and adjusted timeout settings for the SD cards.
- **Result of the operation after the user adopted suggestion 1:** Users reported improvements with specific types of SD cards (e.g., SanDisk Extreme) and suggested configurations.
- **Suggestion 2 provided by developers or other personnel:** @davids5 and others suggested trying different cluster sizes for SD card formatting and adjusting logger buffer sizes.
- **Result of the operation after the user adopted suggestion 2:** The logging issues were mostly resolved with adjustments in SD card formatting and logger settings.
- **Suggestion 3 provided by developers or other personnel:** Multiple firmware updates and driver adjustments were proposed to permanently resolve the issue.
- **Result of the operation after the user adopted suggestion 3:** Final fixes were integrated, and the issue was considered resolved as the specific changes were implemented and tested successfully by users.
