Here is the extracted information from your markdown document:

**Environment where the bug occurred:**

- **Hardware environment:** Cube Orange
- **Software environment:** QGroundControl (QGC) on Ubuntu
- **Report Time:** Dec 8, 2022
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**cfb670f

**Steps for bug reproduction:**

- **Step 1:** Build Main
- **Step 2:** Flash on Cube Orange
- **Step 3:** Fly the drone
- **Step 4:** Try to download log through QGC

**Observed behavior by the user:**

- **Behavior after step 1 - 3:** Not explicitly mentioned
- **Behavior after step 4:** QGC shows 'error' message when trying to download logs

**Expected behavior:**

- **Expected behavior 1:** Logs should successfully download from the Cube Orange when using QGC

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** User described the reproduction steps and reported the issue
- **URL of the flight log provided by the user:** Not provided

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Comment by ryanjAA suggesting saving and uploading Params and comparing to see if others do not have this issue
- **Result of the operation after the user adopted suggestion 1:** Not mentioned
- **Suggestion 2 provided by developers or other personnel:** Comment by TedObrien asking if a solution was found for the issue
- **Result of the operation after the user adopted suggestion 2:** Not mentioned
- **Suggestion 3 provided by developers or other personnel:** Comment by ripdk12 mentioning downloading logs is possible when connected via telemetry radio instead of USB
- **Result of the operation after the user adopted suggestion 3:** Not mentioned
- **Final resolution:** Fixed by issue \\\#20824, as noted by danielhonies
