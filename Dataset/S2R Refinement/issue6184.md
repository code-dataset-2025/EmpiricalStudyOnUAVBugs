**Environment where the bug occurred:**

- **Hardware environment:** Pixracer
- **Software environment:** PX4 Autopilot, origin/master at 3a17c07
- **Report Time:** Dec 27, 2016
- **PX4 Autopilot commit version:** 3a17c07

**Steps for bug reproduction:**

- **Step 1:** Build and load upstream master onto the Pixracer.
  - Commands:
    1. `git fetch origin`
    2. `git checkout master`
    3. `git reset --hard origin/master`
    4. `make distclean`
    5. `make px4fmu-v4_default upload`
- **Step 2:** Connect the debug cable to the serial port.
- **Step 3:** Establish an nsh console connection using a serial terminal.
- **Step 4:** Repeatedly enter `listener sensor_gyro`.

**Observed behavior by the user:**

- **Behavior after Step 1:** N/A
- **Behavior after Step 2:** N/A
- **Behavior after Step 3:** N/A
- **Behavior after Step 4:** The `sensor_gyro` topic occasionally displayed invalid values for the `device_id`, instead of the ID for the ICM-20608 or MPU9250 gyro.

**Expected behavior:**

- **Expected behavior 1:** The `sensor_gyro` topic should consistently display the correct device ID for the gyro (ICM-20608 or MPU9250).

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Conducted tests using both the `sensor_correction-wip` branch and the `origin/master` to verify the issue; shared specific steps to reproduce the issue.
- **URL of the flight log provided by the user:** Not provided.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `LorenzMeier` noted that the field was not yet implemented on NuttX and mentioned plans to address this issue in future system evolution; suggested a temporary workaround.
- **Result of the operation after the user adopted suggestion 1:** No specific result mentioned, as the suggestion was to temporarily hack around the issue.
- **Suggestion 2 provided by other personnel:** Developer `mhkabir` inquired about whether the issue was still present months later.
- **Result of the operation after the user adopted suggestion 2:** User `priseborough` confirmed that the issue was resolved, and the `sensor_gyro` and `sensor_accel` topics now contained consistent sensor IDs.
