**Environment where the bug occurred:**

- **Hardware environment:** Pixhawk with Taranis Q X7 + FrSky X8R (as mentioned by hardeman), Pixhawk 2 (as mentioned by wluker), possibly Pixhawk 2 copies (as mentioned by HVKHVK)
- **Software environment:** PX4 Autopilot version 1.9.0, issue also mentioned in versions 1.9.1 and higher by other users
- **Report Time:** Jun 12, 2019
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**048cca7

**Steps for bug reproduction:**

- **Step 1:** Power on everything
- **Step 2:** Observe stick movements in QGroundControl (QGC)<font color='red'>需要实际RC来控制</font>
- **Step 3:** Try to execute commands like arming or mode switch

**Observed behavior by the user:**

- **Behavior after step 1:** Everything powers on
- **Behavior after step 2:** Stick movements are visible in QGC
- **Behavior after step 3:** Commands (like arming or mode switch) are not executed sometimes

**Expected behavior:**

- **Expected behavior 1:** PX4 should consistently respond to arming commands
- **Expected behavior 2:** PX4 should consistently respond to mode switch commands

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** User mentions the problem occurs sporadically and not reproducible every time; provided equipment and setup details
- **URL of the flight log provided by the user:**
  - https://review.px4.io/plot_app?log=a7c08c8a-a018-47fc-a6dd-5b85665dfacc
  - https://review.px4.io/plot_app?log=9c83ed28-6056-486d-8b3b-0bb99ef2dbd9
  - https://review.px4.io/plot_app?log=12c942df-f99a-4f57-89bc-3a242c0c1d3e

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** @dagar suggested getting a log from boot by setting the parameter `SDLOG_MODE` to 2
- **Result of the operation after the user adopted suggestion 1:** User did not provide logs initially, but other users later provided logs
- **Suggestion 2 provided by developers or other personnel:** @julianoes suggested checking the output of `px4io status` for more information
- **Result of the operation after the user adopted suggestion 2:** There were no follow-up logs or status outputs capturing the issue explicitly

Note: The issue was eventually closed due to lack of follow-up, but similar issues appeared in later versions as noted by other users.
