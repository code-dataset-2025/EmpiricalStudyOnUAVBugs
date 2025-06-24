**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned
- **Software environment:** PX4 Autopilot with commit 53b3dfa64ea85876014c5743004b47173bb88007
- **Report Time:** Aug 27, 2020
- **PX4 Autopilot commit version:** commit 53b3dfa64ea85876014c5743004b47173bb88007

**Steps for bug reproduction:**

- **Step 1:** Checkout to the commit 53b3dfa64ea85876014c5743004b47173bb88007.
- **Step 2:** Execute `make px4_sitl gazebo_rover`.
- **Step 3:** Open QGroundControl (QGC) and enable virtual sticks.
- **Step 4:** Arm the vehicle in manual mode, then move around sticks.
- **Step 5:** Switch to Hold mode. Click on the map and slide the "GO TO" bar.

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** N/A
- **Behavior after step 3:** N/A
- **Behavior after step 4:** Nothing happens when moving the sticks in manual mode.
- **Behavior after step 5:** Nothing happens when clicking on the map and sliding the "GO TO" bar in Hold mode.

**Expected behavior:**

- **Expected behavior 1:** The rover should respond to manual control inputs.
- **Expected behavior 2:** The rover should move to the set position when the "GO TO" bar is used in Hold mode.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** None explicitly mentioned, but included steps for reproducing the issue and mentioned checking out to the previous commit where the functionalities worked.
- **URL of the flight log provided by the user:** Not provided.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `dagar` acknowledged the report and mentioned looking into it.
- **Result of the operation after the user adopted suggestion 1:** N/A (no action taken by the user as the suggestion was simply an acknowledgment).

- **Suggestion 2 provided by developers or other personnel:** #15664 (implied fix but detailed content not described).
- **Result of the operation after the user adopted suggestion 2:** Issue was fixed, implying successful resolution with the mentioned fix.
