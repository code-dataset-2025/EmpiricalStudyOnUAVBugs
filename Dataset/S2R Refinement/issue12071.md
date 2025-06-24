**Environment where the bug occurred:**

- **Hardware environment:** Hex Cube, RTK GPS driver modified
- **Software environment:** Firmware version derived from 1.8.1 stable
- **Report Time:** May 25, 2019
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**8812738

**Steps for bug reproduction:**

- **Step 1:** Prepare the plane with RC, upload the mission, then plug out the SD card before manually taking off.
- **Step 2:** Fly the plane, then switch to mission mode.
- **Step 3:** In HIL with rotary wing, make the rotary wing execute a mission, then plug out the SD card.

**Observed behavior by the user:**

- **Behavior after step 1:** The plane flies to the only known point, creating a "8" flight path.
- **Behavior after step 2:** The plane continues flying to the 5th point and the commands from QGC become useless.
- **Behavior after step 3:** The rotary wing stops upon reaching the current waypoint. MAVLINK_MISSION and NAVIGATOR modules stop, COMMANDER module works, but switching mode in QGC is useless, and only RC can switch the mode to manual/altitude/position.

**Expected behavior:**

- **Expected behavior 1:** The plane should continue its mission without manual intervention.
- **Expected behavior 2:** The rotary wing should not stop mid-mission when the SD card is removed.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** User checked the code and suspected a datamanager problem, mentioning a potential semaphore block.
- **URL of the flight log provided by the user:** [Flight log](https://logs.px4.io/plot_app?log=34ff913a-5414-4046-87db-181a0ea7b507)

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** LorenzMeier asked for the branch code to be shared for further investigation.
- **Result of the operation after the user adopted suggestion 1:** JohnSnowball asked how to share the branch and mentioned that the problem persisted across multiple firmware versions.
  
- **Suggestion 2 provided by developers or other personnel:** @bkueng was asked to test and cross-fix by LorenzMeier.
- **Result of the operation after the user adopted suggestion 2:** @jorge789 tested on multiple modes and provided logs indicating no issues were found, which challenged the original observation by JohnSnowball.

- **Suggestion 3 provided by developers or other personnel:** @julianoes investigated the issue, suspected a semaphore problem, and detailed findings on semaphore and logger issues.
- **Result of the operation after the user adopted suggestion 3:** Further discussion and investigation by developers identified an area for potential fixes in the NuttX platform related to semaphore locking during SD card removal.
