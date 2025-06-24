**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned
- **Software environment:** PX4 Autopilot, exact commit version not mentioned
- **Report Time:** Jul 12, 2019
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**53c5b6d

**Steps for bug reproduction:**

- **Step 1:** Start SITL jMAVSim or Gazebo.
- **Step 2:** Set the parameter `MIS_TAKEOFF_ALT` to 0.5.
- **Step 3:** Issue the command `commander takeoff`.

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** N/A
- **Behavior after step 3:** The quadcopter does not take off; it auto-disarms instead.<font color='red'>同样不起飞，但不同的是不会自动disarm</font>

**Expected behavior:**

- **Expected behavior 1:** The quadcopter should take off even if the altitude is set to a relatively low value.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** User utilized `git bisect` to identify possible problematic commit; pointed to commit `bb055fd`.
- **URL of the flight log provided by the user:** [URL provided](https://logs.px4.io/plot_app?log=b5802f74-4a52-42f2-8f31-0bbf01fa84e9)

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** `@bresch` suggested checking if the issue still exists after changes to waypoint tracking logic.
- **Result of the operation after the user adopted suggestion 1:** `@julianoes` tested and found improvements; takeoff at 0.5m and 0.3m worked, 0.2m was inconsistent, and 0.1m stayed grounded but overall much better.
  
- **Suggestion 2 provided by developers or other personnel:** `@bresch` inquired why the Navigator wasn't raising concerns, referencing the `MIS_TAKEOFF_ALT` logic in the code.
- **Result of the operation after the user adopted suggestion 2:** Not explicitly mentioned, but `@julianoes` provided the parameter setting location in MAVSDK code.

No further suggestions or results mentioned in subsequent comments.
