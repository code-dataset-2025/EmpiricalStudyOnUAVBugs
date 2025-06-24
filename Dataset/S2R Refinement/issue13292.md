**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned
- **Software environment:** PX4 Autopilot with commit 6a0f5249f825effc6a516596aea7ccc4b8c70cc2
- **Report Time:** Oct 28, 2019
- **PX4 Autopilot commit version:** 6a0f5249f825effc6a516596aea7ccc4b8c70cc2

**Steps for bug reproduction:**

- **Step 1:** Start SITL.
- **Step 2:** Open QGC (version 3.5.4) and go to the Settings -> Power tab.

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** A warning is displayed: "Parameters are missing from firmware. You may be running a version of firmware QGC does not work correctly with or your firmware has a bug in it. Missing params: -1:BAT_A_PER_V, -1:BAT_V_DIV."

**Expected behavior:**

- **Expected behavior 1:** No warning should be displayed when navigating to the Power tab in QGC.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Identified the commit causing the issue and provided details of the commit and author.
- **URL of the flight log provided by the user:** Not provided.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `dagar` suggested shifting the analog battery parameters for SITL.
- **Result of the operation after the user adopted suggestion 1:** Not mentioned.

- **Suggestion 2 provided by developers or other personnel:** `dagar` mentioned maintaining a list of parameters that QGC depends on and discussed longer-term solutions for QGC with different power modules.
- **Result of the operation after the user adopted suggestion 2:** Not applicable as the discussion was about future solutions rather than immediate actions.

- **Suggestion 3 provided by developers or other personnel:** `dagar` proposed considering automated testing and updating QGC for future systems without analog power modules.
- **Result of the operation after the user adopted suggestion 3:** Not applicable as this was a proposal for consideration, not immediate action.
