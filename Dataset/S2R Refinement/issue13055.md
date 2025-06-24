**Environment where the bug occurred:**

- **Hardware environment:** Hexacopter platform
- **Software environment:** PX4 Autopilot 1.9.2
- **Report Time:** Sep 30, 2019
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**2989ce9

**Steps for bug reproduction:**

- **Step 1:** Drone switched on.
- **Step 2:** Send a message_interval to limit some message.
- **Step 3:** Open QGC and mavlink_inspector and observe the sys_status transmission rate.

**Observed behavior by the user:**

- **Behavior after step 1:** Drone is on, no interaction observed yet.
- **Behavior after step 2:** Messages are limited as per the set message_interval.
- **Behavior after step 3:** sys_status isn't being transmitted or is transmitted at a very low rate (sometimes 1 or 2 messages over 30-40 seconds, often none).

**Expected behavior:**

- **Expected behavior 1:** sys_status should not be "removed" when limiting another message with message_interval.
- **Expected behavior 2:** Using message_interval for the sys_status message should correctly set the desired transmission rate of sys_status.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** The user confirmed the issue exists in the master and v1.10 beta versions as well; tested commands on the command line; verified the system with mavlink status tools; identified that some messages could not be throttled by message_interval.
- **URL of the flight log provided by the user:** Not provided.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `dagar` suggested trying the current master or v1.10 beta.
- **Result of the operation after the user adopted suggestion 1:** User tested on the suggested versions and experienced the same issue, with some messages that can't be throttled and sys_status not being transmitted as expected.
  
- **Suggestion 2 provided by developers or other personnel:** `dagar` requested output from running mavlink status + mavlink status streams.
- **Result of the operation after the user adopted suggestion 2:** User provided a snapshot of command line outputs showing the sys_status rate issue.

**Final Outcome:**

The user identified that the issue stemmed from their misunderstanding of the unit used in the message_interval command, which should be in microseconds (us) rather than hertz (Hz). Once corrected, sys_status and message transmission behaved as expected, leading to the closure of the issue with gratitude for the clarity provided.
