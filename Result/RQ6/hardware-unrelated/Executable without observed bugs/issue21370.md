**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned
- **Software environment:** PX4 Autopilot with commit da4644c20adce8aeedd5be432fc88b1b115d7eb9
- **Report time:** Mar 25, 2023
- **PX4 Autopilot commit version:** da4644c20adce8aeedd5be432fc88b1b115d7eb9

**Steps for bug reproduction:**

- **Step 1:** Checkout to the commit da4644c20adce8aeedd5be432fc88b1b115d7eb9.
- **Step 2:** Execute `make px4_sitl gazebo-classic`.
- **Behavior:** Soon after startup, the "Failsafe Flighttask activated" error will appear.

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** "Failsafe Flighttask activated" error occurs soon after startup.

**Expected behavior:**

- **Expected behavior 1:** The Failsafe Flighttask error should not be triggered.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** The user performed a bisecting process, discussed changes in task activation patterns, and narrowed down the issue to a specific commit.
- **URL of the flight log provided by the user:** Not provided.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer @MaEtUgR discussed the reason behind the failsafe mode activation and confirmed ease of reproduction.
- **Result of the operation after the user adopted suggestion 1:** N/A (no explicit action from the user beyond communication acknowledgment).

- **Suggestion 2 provided by developers or other personnel:** @MaEtUgR provided insights on potential causes, the mechanism of switching tasks, and possible historical checks duplications.
- **Result of the operation after the user adopted suggestion 2:** N/A (The suggestions were more informative discussions rather than directive actions).
