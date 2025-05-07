**Environment where the bug occurred:**

- **Hardware environment:** omnibusf4 board, multiple Hobbywing XRotor Flight Controllers
- **Software environment:** PX4 Autopilot
- **Report Time:** Feb 5, 2019
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**4025207

**Steps for bug reproduction:**

- **Step 1:** Make `omnibus_f4sd_default`.
- **Step 2:** Make `omnibus_f4sd_default upload`.
- **Step 3:** Reboot board.
- **Step 4:** Plug into computer and open QGC (QGroundControl).

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** N/A
- **Behavior after step 3:** N/A
- **Behavior after step 4:** The board does not boot and does not connect to QGC. An error message suggests letting the system fully boot and restarting QGC.

**Expected behavior:**

- **Expected behavior 1:** The board should boot successfully.
- **Expected behavior 2:** The board should connect to QGC.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Tried several versions including V1.8.0, V1.8.2, and V1.9; removed some unneeded drivers to fit the firmware; tested on multiple computers and SD cards; attempted using the latest bootloader.
- **URL of the flight log provided by the user:** https://i.imgur.com/wimiZiO.png

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** `bkueng` suggested ensuring the latest bootloader and firmware were used due to a breaking change in PX4/PX4-Bootloader#124.
- **Result of the operation after the user adopted suggestion 1:** User tried the latest bootloader but still faced the same connection issue, as noted in the provided log URL.
- **Suggestion 2 provided by developers or other personnel:** `bkueng` requested exact instructions on how everything was flashed and details about the error received.
- **Result of the operation after the user adopted suggestion 2:** No further response or solution was provided in the document.
- **Suggestion 3 provided by developers or other personnel:** The issue was marked as stale by `stale` due to inactivity. Later, it was closed.
