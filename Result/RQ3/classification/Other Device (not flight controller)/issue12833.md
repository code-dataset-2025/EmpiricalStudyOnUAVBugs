**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned
- **Software environment:** PX4 Autopilot
- **Report Time:** Aug 28, 2019
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**be368f3

**Steps for bug reproduction:**

- **Step 1:** Drone switched on.
- **Step 2:** Uploaded mission.
- **Step 3:** Took off.

**Observed behavior by the user:**

- **Behavior after step 4:** Parameters did not bind correctly to low-medium-high settings of the 3-way switch.<font color='red'>三档开关绑定不同参数需要遥控器</font>

**Expected behavior:**

- **Expected behavior 1:** Low-0: Altitude following
- **Expected behavior 2:** Medium-1: Terrain following
- **Expected behavior 3:** High-2: Terrain hold

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Attempted to tune parameters in QGroundControl; discussed potential with similar feature in ArduCopter.
- **URL of the flight log provided by the user:** Not provided.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** `julianoes` suggested the issue might stem from parameters of int type with tuning and encouraged debugging in code, perhaps using HITL simulation.
- **Result of the operation after the user adopted suggestion 1:** No explicit response from the user regarding taking action.
  
- **Suggestion 2 provided by developers or other personnel:** `Seeelefant` suggested the creation of a continuous parameter (like ArduCopter's RNGFND_GAIN) that interpolates between height measures in the PX4.
- **Result of the operation after the user adopted suggestion 2:** `julianoes` indicated focus should remain on fixing the reported bug rather than implementing new parameters.

- **Suggestion 3 provided by developers or other personnel:** Issue marked as stale due to inactivity.
