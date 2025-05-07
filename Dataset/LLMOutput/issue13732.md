**Environment where the bug occurred:**

- **Hardware environment:** Durandal flight controller, Holybro GPS, F450 frame, Holybro 915Mhz telemetry
- **Software environment:** PX4 Autopilot v1.10.0 (beta) (commit d6ffdc0), QGroundControl (QGC) 3.5.6
- **Report Time:** Dec 11, 2019
- **PX4 Autopilot commit version:** v1.10.0 (beta) (d6ffdc0)

**Steps for bug reproduction:**

- **Step 1:** Make sure you have the latest QGC 3.5.6.
- **Step 2:** Flash firmware Master branch on the Durandal flight controller.
- **Step 3:** Upload a mission to the vehicle.
- **Step 4:** Observe the error message "Mission transfer failed".

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** N/A
- **Behavior after step 3:** N/A
- **Behavior after step 4:** Mission transfer failed error message appears. The mission fails to load when using USB, both with and without the battery connected, but works via telemetry.

**Expected behavior:**

- **Expected behavior 1:** Mission should be uploaded successfully via USB without errors.
- **Expected behavior 2:** All flight logs should be saved and accessible on SD card after flights.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Formatted the SD card, attempted connections using USB and battery, and tested via telemetry.
- **URL of the flight log provided by the user:** 
  - [Log 1](https://review.px4.io/plot_app?log=0a193cd7-9b3b-483f-86de-aea71489b32b)
  - [Log 2](https://review.px4.io/plot_app?log=62b6b784-7e3a-41c2-a47b-b27791a90635)
  - Additional logs provided in comments.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** @davids5 asked for more details about what was connected during the failure.
- **Result of the operation after the user adopted suggestion 1:** Additional information was provided by @Tony3dr regarding failed connections and issues with logs not saving.
- **Suggestion 2 provided by developers or other personnel:** @davids5 suggested testing using a powered USB hub and no battery.
- **Result of the operation after the user adopted suggestion 2:** The mission was uploaded successfully with a powered hub, but a new error appeared: "Preflight fail, Baro Sensor #0".
- **Suggestion 3 provided by developers or other personnel:** @davids5 requested a retest with commit #14592.
- **Result of the operation after the user adopted suggestion 3:** Not mentioned in the document.
