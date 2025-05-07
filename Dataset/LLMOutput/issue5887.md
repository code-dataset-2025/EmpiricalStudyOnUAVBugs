**Environment where the bug occurred:**

- **Hardware environment:** Raspberry Pi 3 (RPi3) with Navio2
- **Software environment:** PX4 Autopilot running on Emlid RT kernel Raspbian
- **Report Time:** Nov 21, 2016
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**7a69895

**Steps for bug reproduction:**

- **Step 1:** Add the binary execution to `rc.local` on RPi3.
- **Step 2:** Implement the command `cd /home/pi && ./px4 px4.config > startup.log`.

**Observed behavior by the user:**

- **Behavior after step 1:** Successfully starts PX4, but leads to high CPU utilization.
- **Behavior after step 2:** Higher CPU utilization compared to starting PX4 from shell or SSH.

**Expected behavior:**

- **Expected behavior 1:** PX4 autopilot should start with lower CPU utilization when initiated through `rc.local`.
- **Expected behavior 2:** CPU utilization should be consistent regardless of the start method (auto-start vs. manual start).

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** The user attempted auto-start implementation and observed differences in CPU utilization.
- **URL of the flight log provided by the user:** Not provided.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `bkueng` suggested modifying the command to include the `-d` flag to start PX4 in daemon mode: `cd /home/pi && ./px4 -d px4.config > px4.log`.
- **Result of the operation after the user adopted suggestion 1:** Not explicitly mentioned, but implying that it resolves the high CPU usage as the suggestion was added to the DevGuide as a fix.

