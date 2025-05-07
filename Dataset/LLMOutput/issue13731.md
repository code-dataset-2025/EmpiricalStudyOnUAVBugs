# Basic Information:
### Title: Kakute F7 - baro sensor #0 missing #13731
### Issue status: Closed
### Author: sevet
### Issue open time: Dec 11, 2019
### Fixed by: #13755

# Report
### Report author: sevet
### Report Time: Dec 11, 2019
### Report Content:
**Describe the bug:**
The user encountered a pre-arm check failure with the error: "baro sensor #0 missing." The issue was identified on the Kakute F7 board and compiled from the source on Dec 11, 2019.

**Steps to reproduce:**
1. Compile the firmware from the source.
2. Flash the firmware onto the board.
3. Calibrate and set up all necessary configurations.
4. Attempt to arm the vehicle.

**Observed behavior by the user:**
- Failing the pre-arm check with the error: "baro sensor #0 missing."
- The altitude does not change on the map in QGroundControl when elevating the quad.

**Expected behavior:**
1. The barometer should function correctly to provide altitude data.
2. The vehicle should successfully pass the pre-arm check and arm without errors.

# Environment where the bug occurred:
- **Hardware environment:** HOLYBRO_KAKUTEF7
- **Software environment:** 
  - **OS:** NuttX Release 8.2.0
  - **Toolchain:** GNU GCC 7.3.1
  - **Firmware version:** 1.10.0
  - **PX4 Autopilot commit version:** 944bf54d84815cb668aa5975fd5820386ebe14a7
- **Report Time:** Dec 11, 2019

# Steps for bug reproduction:
- **Step 1:** Compile the firmware from the source.
- **Step 2:** Flash the compiled firmware onto the Kakute F7 board.
- **Step 3:** Calibrate and configure all required sensors and systems.
- **Step 4:** Attempt to arm the vehicle.
- **Step 5:** Elevate the quad and observe the altitude readings on QGroundControl.

# Observed behavior by the user:
- **Behavior after Step 1:** N/A
- **Behavior after Step 2:** N/A
- **Behavior after Step 3:** N/A
- **Behavior after Step 4:** The pre-arm check fails with the error: "baro sensor #0 missing."
- **Behavior after Step 5:** The altitude reading in QGroundControl does not change when elevating the quad.

# Expected behavior:
- **Expected behavior 1:** The barometer should function and provide altitude data.
- **Expected behavior 2:** The vehicle should pass the pre-arm check and arm successfully.

# Additional information provided by the user for bug investigation:
- **Actions taken by the user:** The user attempted to manually start the barometer using the command `bmp280 -I start`, but it did not resolve the issue.
- **Error during configuration saving:** The user reported an error during parameter auto-save: `ERROR [parameters] param auto save failed (-27).`
- **Provided dmesg output:** Detailed dmesg logs, including system and hardware details, were included for debugging.

# Communication between developers or other personnel and the user:
### Suggestion 1 provided by developers or other personnel:
**Comment by `dagar` (Dec 11, 2019):**
- Suggested the user run `dmesg` from the console to obtain boot output for debugging.

**Result of the operation after the user adopted suggestion 1:**
- The user provided detailed `dmesg` logs but encountered issues running the `dmsg` command and mentioned configuration saving errors.

### Suggestion 2 provided by developers or other personnel:
**Comment by `dagar` (Dec 11, 2019):**
- Suggested manually starting the barometer using the command `bmp280 -I start`.

**Result of the operation after the user adopted suggestion 2:**
- The user attempted the suggestion, but it did not resolve the issue.

### Suggestion 3 provided by developers or other personnel:
**Comment by `bkueng` (Dec 17, 2019):**
- Mentioned that the issue was fixed in commit #13755.

# Outcome:
The issue was resolved with the commit #13755.
