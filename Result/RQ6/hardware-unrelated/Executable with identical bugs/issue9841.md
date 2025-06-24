**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned
- **Software environment:** Not explicitly mentioned
- **Report Time:** Jul 5, 2018
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**532a970

**Steps for bug reproduction:**

- **Step 1:** Monitor the sending of `POSITION_TARGET_GLOBAL_INT`.

**Observed behavior by the user:**

- **Behavior after step 1:** Only a single packet per change is seen when monitoring `POSITION_TARGET_GLOBAL_INT`.<font color='red'>实际上并非一个bug</font>

**Expected behavior:**

- **Expected behavior 1:** The system should not rely on a single packet expecting it to always arrive to the GCS due to potential unreliability of wireless communication.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Not explicitly mentioned, but referenced a commit by `@dagar`.
- **URL of the flight log provided by the user:** Not provided.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** `dagar` suggested that limiting irrelevant data from being published over a limited data link is beneficial and proposed combining it with another publication to achieve the desired behavior.
- **Result of the operation after the user adopted suggestion 1:** User `superware` raised concerns about limited data bandwidth and the reliability of wireless links in transmitting single packets.
  
- **Suggestion 2 provided by developers or other personnel:** `dagar` suggested checking mavlink status as most serial links automatically scale back transmit rates and recommended reevaluating areas of the mavlink spec concerning missing messages.
- **Result of the operation after the user adopted suggestion 2:** Not explicitly mentioned.
