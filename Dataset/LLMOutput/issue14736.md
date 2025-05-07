**Environment where the bug occurred:**

- **Hardware environment:** Black Cube (px4_fmu-v3_default) running latest PX4 master branch
- **Software environment:** Not explicitly mentioned
- **Report Time:** Apr 22, 2020
- **PX4 Autopilot commit version:** not mentioned
- **last commit before the reporting time:**172e435

**Steps for bug reproduction:**

- **Step 1:** Power the Black Cube via USB.
- **Step 2:** Attach a Here2 GPS to CAN1 (the "real" CAN1).
- **Step 3:** Connect to serial console via an FTDI adapter.
- **Step 4:** Call `uavcan status` to ensure UAVCAN is running (expecting many node-spin and vehicle_air_data errors).
- **Step 5:** Execute a command like `uavcan param list <nodeid>` several times.

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** N/A
- **Behavior after step 3:** N/A
- **Behavior after step 4:** Node-spin and vehicle_air_data errors appear.
- **Behavior after step 5:** The Cube hardfaults after 2-5 calls, leading to a reboot.

**Expected behavior:**
- **Expected behavior 1:** `uavcan param` commands should run without causing a hardfault.
- **Expected behavior 2:** The system should remain stable and not reboot after executing the commands.

**Additional information provided by the user for bug investigation:**
- **Actions taken by the user:** Verified with different settings of UAVCAN_ENABLE parameter and monitored the console output.
- **uavcan status error messages and hardfault logs were provided:** Specific content not detailed in the markdown.

**Communication between developers or other personnel and the user:**
- **Suggestion 1 provided by developers or other personnel:** Developer `dagar` suggested that the issue might be due to missing locking in uavcan param helpers.
- **Result of the operation after the user adopted suggestion 1:** A potential fix was worked on (#14741), but it did not resolve the problem.
  
- **Suggestion 2 provided by developers or other personnel:** Developer `dagar` planned to reproduce the issue locally with a debugger to investigate further.
- **Result of the operation after the user adopted suggestion 2:** Additional issues related to memory corruption were noted, but detailed outcomes of the debugger investigation are not documented here.
  
- **Suggestion 3 provided by developers or other personnel:** Developer `amikhalev` suggested a potential stack overflow issue that might have been resolved by #15864.
- **Result of the operation after the user adopted suggestion 3:** The issue was marked as probably fixed in master, with a request to reopen the issue if the problem persisted.
