**Environment where the bug occurred:**

- **Hardware environment:** px4_fmu-v5, nxp_fmuk66-v3
- **Software environment:** Not mentioned
- **Report Time:** Oct 8, 2021
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**4be4522

**Steps for bug reproduction:**

- **Step 1:** Turn the drone on.
- **Step 2:** Prepare many MAVLINK packets with msgID 147 with different "sysID" and "compID".
- **Step 3:** Send a packet.
- **Step 4:** Out Of Bound (OOB) vulnerability occurs.
- **Step 5:** Turn the drone off.

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** N/A
- **Behavior after step 3:** N/A
- **Behavior after step 4:** OOB vulnerability occurs.
- **Behavior after step 5:** N/A

**Expected behavior:**

- **Expected behavior 1:** The system should handle MAVLINK packets appropriately without causing an OOB vulnerability.
- **Expected behavior 2:** The "cell_count" should not exceed the size of "battery_mavlink.voltages", preventing an OOB error.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user (if the user actively investigated the bug):** The user modified the condition in the `while` loop to avoid the crash by adjusting the condition sequence.
- **URL of the flight log provided by the user:** [Flight log](https://logs.px4.io/plot_app?log=0f0583c3-a609-4b61-a283-6e3df243141c)

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `dagar` noted that the line numbers don't match current master and asked for further clarification.
- **Result of the operation after the user adopted suggestion 1:** The user clarified the discrepancy was due to personal modifications and explained the issue further.
- **Suggestion 2 provided by developers or other personnel:** Developer `dagar` acknowledges understanding the OOB in the condition and plans to fix it.
- **Result of the operation after the user adopted suggestion 2:** The fix was implemented in commit #18411.
