**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned
- **Software environment:** Not explicitly mentioned
- **Report Time:** Sep 20, 2022
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**a96187c

**Steps for bug reproduction:**

- **Step 1:** Start plane SITL simulation by executing `make px4_sitl gazebo_plane`.
- **Step 2:** Command the takeoff using `commander takeoff`.

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** The vehicle immediately goes into failsafe, enters RTL (Return-to-Launch), and then crashes.

**Expected behavior:**

- **Expected behavior 1:** Vehicle should either take off or reject the takeoff command.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Included steps for reproducing the issue.
- **URL of the flight log provided by the user:** [Flight log](https://review.px4.io/plot_app?log=0314e693-cb1e-4675-a7ef-bad36473a129)

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Bug fixed in issue #20172 as mentioned by user `bkueng`.
- **Result of the operation after the user adopted suggestion 1:** N/A (No specific result mentioned, but the issue was marked as fixed in a subsequent commit).
