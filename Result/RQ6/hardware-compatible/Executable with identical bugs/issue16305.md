**Environment where the bug occurred:**

- **Hardware environment:** Quadplane with Pixhawk 4
- **Software environment:** PX4 Autopilot v1.11.2 and master
- **Report Time:** Nov 30, 2020
- **PX4 Autopilot commit version:** not mentioned
- **last commit before the reporting time:**378b41a

**Steps for bug reproduction:**

- **Step 1:** Switch on the drone.
- **Step 2:** Execute `make px4_sitl gazebo_standard_vtol` for SITL or use a real drone.
- **Step 3:** Upload the mission "RC club many transitions.zip."
- **Step 4:** Start the mission.
- **Step 5:** Observe the yaw after back transitions.

**Observed behavior by the user:**
- **Behavior after step 1:** N/A
- **Behavior after step 2:** N/A
- **Behavior after step 3:** N/A
- **Behavior after step 4:** N/A
- **Behavior after step 5:** The VTOL yaws towards due north (0° yaw setpoint) after back transitions, instead of maintaining the expected heading.<font color='red'>yaw angle确实存在360度的转变https://logs.px4.io/plot_app?log=36419d45-eaba-4d63-9c3a-361dc18e21b7</font>

**Expected behavior:**

- **Expected behavior 1:** The drone should keep its current heading.
- **Expected behavior 2:** The drone should use the heading as calculated normally in the MPC trajectory generation.
- **Expected behavior 3:** The drone should weathervane.

**Additional information provided by the user for bug investigation:**
- **Actions taken by the user:** Conducted a git bisect to identify the source of the change causing the issue.
- **URL of the flight log provided by the user:**
  - Real quadplane: [Link](https://logs.px4.io/plot_app?log=3b4e3749-8b0e-44a2-9e9b-74b329b3dbab) (ignore after 6:00)
  - SITL, v1.11.2: [Link](https://logs.px4.io/plot_app?log=21bdc8c9-9cfc-4964-90aa-2f123ebb70f6)
  - SITL, master: [Link](https://logs.px4.io/plot_app?log=cc6301a2-0a6f-4100-a973-128cb7784ddf)
  - SITL, v1.11.2, other flight modes: [Link](https://logs.px4.io/plot_app?log=74ae49e6-1d82-4a2f-81ee-2fb387cacd1c) (no enforced 0° yaw)

**Communication between developers or other personnel and the user:**
- **Suggestion 1 provided by developers or other personnel:** User ThomasRigi identified the issue as a change in commit 574b482 and mentioned a fix in pull request #16335.
- **Result of the operation after the user adopted suggestion 1:** N/A (no specific result mentioned, but the issue was closed, indicating resolution).
