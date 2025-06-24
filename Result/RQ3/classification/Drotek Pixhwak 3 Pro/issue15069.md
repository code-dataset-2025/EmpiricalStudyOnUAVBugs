**Environment where the bug occurred:**

- **Hardware environment:** Drotek p3 pro FC with Drotek power management pro
- **Software environment:** PX4 Autopilot version 1.10, QGroundControl (QGC)
- **Report Time:** Jun 9, 2020
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**13d983d

**Steps for bug reproduction:**

- **Step 1:** Use Drotek p3 pro FC.
- **Step 2:** Connect Drotek power management pro to power ports 1 and 2 on Drotek p3 pro FC.
- **Step 3:** Set scaling factors according to the manufacturer.
- **Step 4:** Apply voltage to the drone.
- **Step 5:** Use a voltmeter to verify same input voltage for autopilot ADCs from the power-manager individual outputs.
- **Step 6:** Turn on the drone and observe voltage measurements in QGC.

**Observed behavior by the user:**

- **Behavior after step 6:** Battery 1 shows correct voltage (~49V for a fresh 12S lipo), but Battery 2 shows a lower voltage (~41V).

**Expected behavior:**

- **Expected behavior 1:** Battery 1 should show correct voltage (~50V for a full 12S battery).
- **Expected behavior 2:** Battery 2 should show correct voltage (~50V for a full 12S battery).
- **Expected behavior 3:** Battery percentage estimate should be stable, and the system should describe how it handles two batteries.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** User verified power-monitor outputs with a voltmeter to ensure the values were equal; observed consistent multiplication factor discrepancy between voltage measurements of the two batteries.
- **URL of the flight log provided by the user:** Not provided, but user mentioned the issue was observed during all ground testing.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `helgeanl` suggested that the issue might be due to incorrect data interpretation by QGC rather than the flight controller. They suggested checking `uorb` messages or `battery_status` mavlink message for accurate data.
- **Result of the operation after the user adopted suggestion 1:** Not explicitly mentioned, but `helgeanl` noted that the battery estimation on the flight controller was correct, hinting that the issue lay with QGC's interpretation.
- **Suggestion 2 provided by developers or other personnel:** `LorenzMeier` asked if the problem persisted and suggested filing a new issue with QGC's issue tracker if the issue remained, referencing this one.
- **Result of the operation after the user adopted suggestion 2:** Not documented within the provided communication.
