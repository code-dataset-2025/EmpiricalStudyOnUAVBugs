**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned
- **Software environment:** PX4 Autopilot after the introduction of FlightTasks
- **Report Time:** Sep 4, 2018
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**060463e

**Steps for bug reproduction:**

- **Step 1:** Takeoff using mode takeoff
- **Step 2:** Fly around in position mode
- **Step 3:** Issue land or RTL command

**Observed behavior by the user:**

- **Behavior after step 1:** Normal takeoff
- **Behavior after step 2:** Normal flight in position mode
- **Behavior after step 3:** The quadcopter flies directly towards home latitude/longitude/altitude, and logging either dies completely or drops out.

**Expected behavior:**

- **Expected behavior 1:** The quadcopter should land or return to launch (RTL) as per the issued commands without flying directly towards the home position.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** The user noticed that the problem seems to be related to takeoff mode, and provided a log link: https://review.px4.io/plot_app?log=7955d3de-31c9-4434-b30d-cb31fadefb32
- **URL of the flight log provided by the user:** https://review.px4.io/plot_app?log=7955d3de-31c9-4434-b30d-cb31fadefb32

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `dagar` asked about the frequency of logging failures and suggested looking into SD card issues.
- **Result of the operation after the user adopted suggestion 1:** The user planned to test with a different SD card.
- **Suggestion 2 provided by developers or other personnel:** Developer `bkueng` suggested trying a different SD card.
- **Result of the operation after the user adopted suggestion 2:** The user acknowledged and agreed to test with a different SD card. 
- **Additional Update:** The user reported that they hadn't seen the issue since September as FlightTasks had seen improvements and closed the issue thereafter.
