**Environment where the bug occurred:**

- **Hardware environment:** Pixhawk 4
- **Software environment:** PX4 Autopilot v1.8.2
- **Report Time:** Apr 16, 2019
- **PX4 Autopilot commit version:** commit c0a1f5b

**Steps for bug reproduction:**

- **Step 1:** Upload v1.8.2 stock firmware on Pixhawk 4.
- **Step 2:** Power cycle autopilot with the stock 4GB SD card.<font color='red'>需求4GB大小SD卡</font>
- **Step 3:** Connect QGroundControl.
- **Step 4:** Check if the SD card is mounted using the `mount` command on nsh.
- **Step 5:** Try to mount the SD card using `mount -t vfat /dev/mmcsd0 /mnt/fs`.

**Observed behavior by the user:**
- **Behavior after step 4:** Only `/etc` and `/proc` are mounted. `/fs/microsd` is not mounted.
- **Behavior after step 5:** Attempting to mount crashes the Pixhawk.

**Expected behavior:**
- **Expected behavior 1:** The SD card should be mounted.
- **Expected behavior 2:** `mount` command on NSH should return `/fs/microsd` as a mounted directory.
- **Expected behavior 3:** Identify and isolate if there is a hardware problem with Pixhawk 4.

**Additional information provided by the user for bug investigation:**
- **Actions taken by the user:** 
  - Tried using different SD cards formatted as FAT32.
  - Uploaded master and beta branches, which prevented the Pixhawk from booting with the SD card inserted.
  - Collected debug probe outputs (files provided).

**Communication between developers or other personnel and the user:**
- **Suggestion 1 provided by developers or other personnel:** Try with a different SD card.
- **Result of the operation after the user adopted suggestion 1:** Same effect; the issue persisted.
- **Suggestion 2 provided by developers or other personnel:** Collect startup output using a Dronecode debug probe.
- **Result of the operation after the user adopted suggestion 2:** User provided comparison debug probe files.
- **Suggestion 3 provided by developers or other personnel:** Try the current master branch for testing.
- **Result of the operation after the user adopted suggestion 3:** The problem persisted with the master branch.
- **Suggestion 4 provided by developers or other personnel:** Contact Holybro for possible hardware issues.
- **Result of the operation after the user adopted suggestion 4:** User contacted Holybro and awaited assistance.
