**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned
- **Software environment:** Not explicitly mentioned
- **Report Time:** Nov 5, 2021
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**88489ae

**Steps for bug reproduction:**

- **Step 1:** Run SITL Plane in a windy environment (set wind speed to 14m/s).
- **Step 2:** Upload a mission with a takeoff waypoint upwind.

**Observed behavior by the user:**
- **Behavior after step 1:** N/A
- **Behavior after step 2:** The vehicle does not use TECS pitch setpoints, which results in the airspeed getting invalidated and potentially causes a crash.

**Expected behavior:**
- **Expected behavior 1:** The vehicle should employ TECS pitch setpoints in takeoff mode.
- **Expected behavior 2:** The vehicle should not result in a crash due to invalidated airspeed.

**Additional information provided by the user for bug investigation:**
- **Actions taken by the user:** Included detailed code snippets indicating where the issue might be occurring, steps to reproduce the issue in a simulated environment, and provided context around the specific conditions leading to the bug.
- **URL of the flight log provided by the user:** [Flight log](https://logs.px4.io/plot_app?log=4f360063-83eb-43bd-81f1-0749f89a9e4e)

**Communication between developers or other personnel and the user:**
- Not explicitly mentioned in the provided document.
