**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned
- **Software environment:** Not explicitly mentioned
- **Report Time:** Mar 17, 2022
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**ff16131

**Steps for bug reproduction:**

- **Step 1:** Start SITL
- **Step 2:** Try the example script available at https://github.com/mavlink/MAVSDK-Python/blob/main/examples/takeoff_and_land.py with the latest mavsdk from pip installed.
- **Step 3:** Run the script once.
- **Step 4:** Run the script again.

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** N/A
- **Behavior after step 3:** The script runs successfully and performs takeoff and landing.
- **Behavior after step 4:** The script refuses to arm, displaying the message "Mode not suitable for takeoff" as the system remains in Land mode.

**Expected behavior:**

- **Expected behavior 1:** The takeoff and land example should allow for multiple successful executions without requiring manual intervention or encountering errors.
- **Expected behavior 2:** The system should correctly recognize and switch from Land mode to Takeoff mode upon repeated execution of the script.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** User identified related issues to the observed behavior (\\\#19291).
- **URL of the flight log provided by the user:** Not provided.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer MaEtUgR referenced issue \#19449 stating it might hotfix/unblock this issue and suggested improvements in workflow by switching the mode first before arming in the future.
- **Result of the operation after the user adopted suggestion 1:** Not explicitly stated in the comments today, but acknowledgment by julianoes suggests it might have resolved or provided insight into the issue.

