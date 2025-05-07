**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned for the initial report. However, additional comments mention hardware like Tarot X6, Pixhawk Cube 2.1, and Here2 GNSS.
- **Software environment:** PX4 Autopilot, observed in versions around 1.9.2, 1.10.0 rc2, and on the SITL (Software In The Loop) test.
- **Report Time:** Dec 4, 2019
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**de6a2d3

**Steps for bug reproduction:**

- **Step 1:** Perform multiple takeoffs in SITL.
- **Step 2:** Observe for any yaw movement during takeoff.

**Observed behavior by the user:**

- **Behavior after step 1:** A random yaw back and forth is observed during some takeoffs in SITL.
  

**Expected behavior:**

- **Expected behavior 1:** The drone should not yaw during takeoff, maintaining a stable heading.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Provided multiple flight logs exhibiting the issue.
- **URL of the flight log provided by the user:** 
  - [Log 1](https://logs.px4.io/plot_app?log=907be591-f04b-4187-8e5a-153435b0bfe1)
  - [Log 2](https://logs.px4.io/plot_app?log=bb0b86a5-a23c-4acd-a88a-fda4a8b6b78c)

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** 
  - Comment by `mwiatt`: Noted similar yaw issues occurring around 2m altitude but didn't recall the issue on version 1.9.2.
  - Comment by `MaEtUgR`: Speculated on a recent change (\#13430) potentially affecting this issue.
  
- **Result of the operation after suggestion 1:** No result feedback from the initial speculations. However, discussion continued regarding potential causes including yaw resets due to inaccurate global heading estimates.
  
- **User's acknowledgement or actions:** The user `mwiatt` provided information reinforcing the behavior difference between version 1.9.2 and 1.10.0 and mentioned the context of flying in Mission mode as opposed to Manual.

- **Final Resolution:** Issue referenced as fixed in \#13965 as mentioned by `julianoes` on Jan 23, 2020.
