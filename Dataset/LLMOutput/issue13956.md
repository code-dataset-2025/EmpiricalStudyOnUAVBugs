**Environment where the bug occurred:**

- **Hardware environment:** PixRacer, PixRacer FMUV4_K66, FMUv5, NXP_FMUK66_V3
- **Software environment:** PX4 Autopilot with reference to multiple flight logs (no specific commit version mentioned)
- **Report Time:** Jan 15, 2020
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**d6cff80

**Steps for bug reproduction:**

- **Step 1:** Drone switched on.
- **Step 2:** Upload mission to the vehicle.
- **Step 3:** Take off in Mission Mode.
- **Step 4:** All commands sent from QGroundControl (Armed and takeoff).
- **Step 5:** Once all waypoints are completed, switch vehicle to RTL (Return to Launch).
- **Step 6:** Upon landing, the vehicle does not descend vertically but drifts with the wind.

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** N/A
- **Behavior after step 3:** Vehicle takes off in Mission Mode.
- **Behavior after step 4:** N/A
- **Behavior after step 5:** Vehicle initiates RTL.
- **Behavior after step 6:** Vehicle does not descend vertically; it drifts away with the wind.

**Expected behavior:**

- **Expected behavior 1:** The vehicle should land vertically and disarm upon completion of the mission.
- **Expected behavior 2:** Maintain position against wind when descending.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Monitored multiple flights and collected flight logs.
- **URL of the flight log provided by the user:**
  - [Log 1](https://review.px4.io/plot_app?log=67a2120c-a473-43a3-a556-6a542f62f7b1)
  - [Log 2](https://review.px4.io/plot_app?log=719ab88b-d993-47c8-a9ca-eaf429d4577e)
  - [Log 3](https://review.px4.io/plot_app?log=b0f1f872-fc9e-41ee-89e3-4e146862efc7)
  - [Log 4](https://review.px4.io/plot_app?log=a8a1391c-06c0-475e-943a-48bea5da2e24)
  - [Log 5](https://review.px4.io/plot_app?log=792db7ac-8738-4bdd-8a03-aa6d88b371b3)

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `julianoes` acknowledged the issue and expressed concern over GPS velocity accuracy errors.
- **Result of the operation after the user adopted suggestion 1:** User `devararendy` noted the issue but questioned the GPS velocity errors despite having 18 satellites.
- **Suggestion 2 provided by developers or other personnel:** Developer `MaEtUgR` provided a detailed analysis of the underlying issue related to RTL mode not handling horizontal drift correctly during high winds.
- **Result of the operation after the user adopted suggestion 2:** Investigation was ongoing to find an appropriate fix.
