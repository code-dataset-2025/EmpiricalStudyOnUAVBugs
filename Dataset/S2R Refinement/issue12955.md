**Environment where the bug occurred:**

- **Hardware environment:** FMU V5 Test bench
- **Software environment:** Latest master branch of PX4 Autopilot as of Sep 13, 2019
- **Report Time:** Sep 13, 2019
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**d4f984f

**Steps for bug reproduction:**

1. Choose a topic that has been published (Run `uorb top` to find some such topics).
2. Run the command `listener <topic>` and `listener <topic> -i 0 -n 10` and observe correct behavior.
3. Run the command `listener <topic> -n 10` and observe "never published."

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** The listener command shows correct topic data.
- **Behavior after step 3:** The listener command shows "never published" for topics that have been published.

**Expected behavior:**

- **Expected behavior 1:** The listener command should display the correct topic data regardless of the arguments used.
- **Expected behavior 2:** The listener command should not display "never published" if the topic has been published.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Provided detailed command outputs and mentioned related issue #12799.
- **URL of the flight log provided by the user:** Not provided.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `dagar` acknowledged the issue and mentioned planning to fix it, indicating awareness from the related issue #12799.
- **Result of the operation after the user adopted suggestion 1:** N/A (no specific corrective action suggested beyond acknowledgment).
