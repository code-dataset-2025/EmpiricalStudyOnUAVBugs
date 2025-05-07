**Environment where the bug occurred:**

- **Hardware environment:** Tested on Dropix fmu-v2 flight controller, applicable to all Nuttx-based boards
- **Software environment:** PX4 Autopilot
- **Report time:** Mar 9, 2023
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**bd5838f

**Steps for bug reproduction:**

- **Step 1:** Take new SD card or delete dataman file on existing SD card.
- **Step 2:** Write large file(s) with non-zero content to SD card and delete them to fill all unused space with garbage.
- **Step 3:** Run PX4 with this SD card.
- **Step 4:** Check error messages on connection to Ground Control Station (GCS).
- **Step 5:** Download dataman file and view it in a hex editor.

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** Unused space on SD card is filled with garbage data.
- **Behavior after step 3:** PX4 runs with potentially corrupted data.
- **Behavior after step 4:** Error messages may appear when connecting to GCS.
- **Behavior after step 5:** The dataman file is filled with garbage data from deleted files except for the "compatibility key" at the file end.

**Expected behavior:**

- **Expected behavior 1:** The dataman file should be filled with zero bytes on creation.
- **Expected behavior 2:** PX4 should not process random data as valid dataman records.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Attempted to fill entire dataman file with zeros after creation.
- **URL of the flight log provided by the user:** Not provided.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** None explicitly provided, but the user investigated the issue by attempting a workaround.
- **Result of the operation after the user adopted suggestion 1:** Writing compatibility key failed when the dataman file was filled entirely with zeros; the user found a working solution by leaving the last kilobyte unfilled.
- **Suggestion 2 provided by developers or other personnel:** Mention of a solution in issue \\\#21594 by Igor-Misic.
- **Result of the operation after the user adopted suggestion 2:** Bug marked as solved.
