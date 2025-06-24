**Environment where the bug occurred:**

- **Hardware environment:** Hexarotor drone with Hex Here2 antenna
- **Software environment:** PX4 Autopilot with commit version based on bcce75e
- **Report Time:** Jul 16, 2020
- **PX4 Autopilot commit version:** bcce75e (April master commit)

**Steps for bug reproduction:**

- **Step 1:** Conduct flight test with the hexarotor.
- **Step 2:** Observe behavior during flight (potential interaction with the safety button).

**Observed behavior by the user:**
- **Behavior after step 1:** Motors stopped suddenly, causing the hexarotor to crash.
- **Behavior after step 2:** No log data was extensively mentioned regarding further behaviors post-crash.

**Expected behavior:**
- **Expected behavior 1:** Motors should continue running during flight unless manually commanded to stop.
- **Expected behavior 2:** The safety switch should not allow disarming in flight.

**Additional information provided by the user for bug investigation:**
- **Actions taken by the user:** User provided log from the flight and mentioned inspecting the electrical setup, particularly the safety button and GPS antenna.
- **URL of the flight log provided by the user:** [Flight log](https://review.px4.io/plot_app?log=f177f3be-1ffc-4040-a86d-5831aefa752c)

**Communication between developers or other personnel and the user:**
- **Suggestion 1 provided by developers or other personnel:** Developer `dagar` suggested investigating the safety button as a potential cause and mentioned adding logging data he wished would help.
- **Result of the operation after the user adopted suggestion 1:** FlavioTonelli confirmed the safety button was part of the GPS antenna and inspected potential damage.
  
- **Suggestion 2 provided by developers or other personnel:** `Dagar` indicated agreement that disarming in-flight should be prevented and began looking into making it a default setting change.
- **Result of the operation after the user adopted suggestion 2:** Agreement on the need for preventing disarming in-flight and that the safety button issue might've been unresolved due to insufficient logging at the time.

Overall, this report led to discussions on making the safety switch logic more robust in future updates.
