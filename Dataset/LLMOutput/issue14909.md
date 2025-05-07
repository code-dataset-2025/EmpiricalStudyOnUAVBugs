Here’s the extracted and formatted information for the bug report you provided:

---

# Basic Information:
### Title: NAV_DELAY not working properly #14909  
### Issue status: Closed  
### Author: julianoes  
### Issue open time: May 15, 2020  
### Fixed by: #15222  

# Report
### Report author: julianoes  
### Report Time: May 15, 2020  
### Report Content:  
**Describe the bug**  
When a NAV_DELAY mission item is used, a multicopter oscillates back and forth around the waypoint where it is supposed to wait.  

**To Reproduce**  
1. Can be reproduced in SITL jMAVSim.  
2. Use the provided plan file: `delay.zip`.  

**Expected behavior**  
1. The drone should hold its position without oscillating.  

**Log Files and Screenshots**  
- Log file: [https://logs.px4.io/plot_app?log=f284d761-8709-4701-bb26-1dba665b187a](https://logs.px4.io/plot_app?log=f284d761-8709-4701-bb26-1dba665b187a).  

---

**Environment where the bug occurred:**  
- **Hardware environment:** Not explicitly mentioned.  
- **Software environment:** SITL with jMAVSim and PX4 Autopilot.  
- **Report time:** May 15, 2020.  
- **PX4 Autopilot commit version:** Not mentioned.  
- **last commit before the reporting time:**328477f

**Steps for bug reproduction:**  
- **Step 1:** Run SITL using jMAVSim.  
- **Step 2:** Use the provided plan file (`delay.zip`).  

**Observed behavior by the user:**  
- **Behavior after step 1:** N/A.  
- **Behavior after step 2:** The drone oscillates back and forth around the waypoint where it is supposed to wait.  

**Expected behavior:**  
- **Expected behavior 1:** The drone should hold its position.  
- **Expected behavior 2:** No oscillation or erratic movement should occur.  

**Additional information provided by the user for bug investigation:**  
- **Actions taken by the user:** Provided a `.plan` file for reproduction and a flight log for analysis.  
- **URL of the flight log provided by the user:** [Flight log link](https://logs.px4.io/plot_app?log=f284d761-8709-4701-bb26-1dba665b187a).  

---

**Communication between developers or other personnel and the user:**  

- **Comment 1:**  
  **Author:** bresch  
  **Time:** May 20, 2020  
  **Content:** Noted that the issue does not occur if a waypoint hold time of 30s is used instead of a delay waypoint of 30s.

- **Comment 2:**  
  **Author:** bresch  
  **Time:** May 20, 2020  
  **Content:** Mentioned a strange behavior in the `.plan` file where the current and next waypoint latitude and longitude are almost identical but not exactly the same.

- **Comment 3:**  
  **Author:** dayjaby  
  **Time:** May 20, 2020  
  **Content:** Explained that before a certain commit, the behavior was hidden by scaling factors. Also noted that setting XY to zero still left the drone stuck near the waypoint and expressed eagerness to see a solution.

- **Comment 4:**  
  **Author:** dayjaby  
  **Time:** Jun 4, 2020  
  **Content:** Asked if bresch had time to address the issue or could provide guidance, as they lacked experience with guidance logic in `FlightTask`.

- **Comment 5:**  
  **Author:** bresch  
  **Time:** Jun 25, 2020  
  **Content:** Suggested understanding the difference between a waypoint with hold time and a delay waypoint. Questioned the necessity of the delay waypoint over hold time.  

- **Comment 6:**  
  **Author:** dayjaby  
  **Time:** Jun 26, 2020  
  **Content:** Explained that the delay waypoint is the most generic way to make the drone wait and outlined a use case where it is needed (e.g., performing multiple mission items at a single waypoint). Highlighted that using hold time in such cases would require stacking multiple waypoints, which is discouraged.  

---
