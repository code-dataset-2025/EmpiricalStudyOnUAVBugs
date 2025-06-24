**Environment where the bug occurred:**

- **Hardware environment:** Cube Black
- **Software environment:** PX4 Autopilot with unspecified commit versions between 2f3174a and 532ccd1 demonstrated the issue, resolved at 4e0441a
- **Report Time:** Apr 7, 2020
- **PX4 Autopilot commit version:** Not explicitly mentioned, but related to commits between 2f3174a and 4e0441a
- **last commit before the reporting time:**47624a0

**Steps for bug reproduction:**

- **Step 1:** Flash a Cube Black with the master branch of PX4 Autopilot.
- **Step 2:** Reset all accelerometer offsets to 0 and scale to 1, then reboot.
- **Step 3:** Observe estimated orientation or sensors measures (while the Cube is leveled).

**Observed behavior by the user:**

- **Behavior after Step 1:** Not explicitly mentioned.
- **Behavior after Step 2:** Not explicitly mentioned.
- **Behavior after Step 3:** The first IMU measures acceleration as +9.81 m/s^2 instead of the expected -9.81 m/s^2. The scales of IMU 1 and 2 were negative during calibration.

**Expected behavior:**

- **Expected behavior 1:** The acceleration should measure about -9.81 m/s^2 when the Cube is leveled.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** The user provided specific conditions and steps for reproduction and investigated over different commits.
- **URL of the flight log provided by the user:** [Flight Log](https://logs.px4.io/plot_app?log=9531c76c-abd9-4656-9fd1-3d50dbc8ced5)

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `dagar` mentioned not experiencing the issue on current master (4e0441a) and queried if a new Cube was used due to recent hardware changes.
- **Result of the operation after the user adopted suggestion 1:** The user reported it works on commit 4e0441a, indicating resolution at this version.
- **Suggestion 2 provided by developers or other personnel:** Developer `dagar` further explained a potential issue with the sensor change in newer versions of Cube Black.
- **Result of the operation after the user adopted suggestion 2:** The user clarified using an older Cube, approximately one year old, discarding this as the cause.
