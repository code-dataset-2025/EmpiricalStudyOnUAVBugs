**Environment where the bug occurred:**

- **Hardware environment:** Pixhawk 4 Holybro
- **Software environment:** PX4 Autopilot v1.10.1 Stable
- **Report Time:** Jan 31, 2020
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**cfa74b9

**Steps for bug reproduction:**

- **Step 1:** Map the MoCap pose to the vision pose topic.<font color='red'>需求Mocap动捕系统</font>
- **Step 2:** Enable the vision pose estimate.
- **Step 3:** Start the copter in altitude mode and take off.
- **Step 4:** Switch to position mode.
- **Step 5:** Observe the copter holding its position stable for ~5 seconds until the issue occurs.

**Observed behavior by the user:**

- **Behavior after step 1:** MoCap pose is mapped to the vision pose topic.
- **Behavior after step 2:** Vision pose estimate is enabled.
- **Behavior after step 3:** Copter starts in altitude mode and takes off.
- **Behavior after step 4:** Copter switches to position mode.
- **Behavior after step 5:** The copter experiences an issue and possibly makes a 180° flip upside down.

**Expected behavior:**

- **Expected behavior 1:** The copter should hold its position in position mode.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Participated in discussions to provide clarification and additional context about the issue, planned to test with PX4 version 1.10.0.
- **URL of the flight log provided by the user:** 
  - [Log 1 (120Hz MoCap)](https://logs.px4.io/plot_app?log=92b60ea2-4b1e-4fac-9402-e1c797494866)
  - [Log 2 (30Hz MoCap)](https://logs.px4.io/plot_app?log=afa24f21-0f51-42a4-bd2e-9b90ef29b14c)

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `dagar` asked if there were any successful logs from an older version of PX4 and if the console was used during the issue.
- **Result of the operation after the user adopted suggestion 1:** The user indicated they would test on an older version and ensure the console was connected for future tests.
- **Suggestion 2 provided by developers or other personnel:** `dagar` proposed testing the master branch (upcoming v1.11.0) to help debug together if the failure could be reproduced.
- **Result of the operation after the user adopted suggestion 2:** Response from the user or outcome from this suggestion was not provided in the document.
