**Environment where the bug occurred:**

- **Hardware environment:** HOLYBRO_KAKUTEF7 
- **Software environment:** PX4 Autopilot 
- **Report time:** Dec 16, 2019
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**7abadab

**Steps for bug reproduction:**

- **Step 1:** Connect with QGroundControl.
- **Step 2:** Make a configuration change like "sys_has_mag".
- **Step 3:** Save & reboot.
- **Step 4:** Power on and check if the change was saved.

**Observed behavior by the user:**

- **Behavior after step 1:** Connected to QGroundControl.
- **Behavior after step 2:** Configuration change appears to be set.
- **Behavior after step 3:** System reboots.
- **Behavior after step 4:** The change was not saved, and the user sees an error "param auto save failed (-27)".

**Expected behavior:**

- **Expected behavior 1:** Configuration changes should be saved after reboot.
- **Expected behavior 2:** Power cycling should retain the saved changes.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Tried flashing the master version, checked output of dmesg, attempted `param reset`, and mentioned that the error is stopped but parameters are not saved.
- **URL of the flight log provided by the user:** Not provided.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** 
  - bkueng suggested flashing master and checking `dmesg` output.
- **Result of the operation after the user adopted suggestion 1:** User provided `dmesg` output, showing repeated errors and system information.

- **Suggestion 2 provided by developers or other personnel:** 
  - bkueng suggested using commands `param reset` and `param save`.
- **Result of the operation after the user adopted suggestion 2:** User reported that `param reset` stops the error but still does not save parameters.

- **Suggestion 3 provided by developers or other personnel:** 
  - julianoes inquired if the issue was resolved.
- **Result of the operation after the user adopted suggestion 3:** No response from the user, leading to the issue being marked stale and subsequently closed.

- **Continuation of issue by another user:** 
  - kh4lilo reported a similar issue on Jul 12, 2023, related to Kakute H7.
  - julianoes requested details on the param file and PX4 version.

- **Solution found by the subsequent user:** 
  - kh4lilo discovered that some params are forced during the init, specifically in `rcS` and `rc.mc_defaults` files, and modified these to resolve the issue.
