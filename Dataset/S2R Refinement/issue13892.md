**Environment where the bug occurred:**

- **Hardware environment:** Pixhawk 3 Pro v4, DJI F450 Frame, CUAV GPS
- **Software environment:** Stable and Master firmware for PX4 Autopilot
- **Report Time:** Jan 8, 2020
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**5f1121c

**Steps for bug reproduction:**

- **Step 1:** Turn on RC.
- **Step 2:** Activate Binding mode (RC will make beeping sounds).
- **Step 3:** With the vehicle turned on, unplug the receptor.
- **Step 4:** Press Binding button and keep pressed.
- **Step 5:** Plug in receptor (without letting the binding button go) and ensure both red and green lights of the receptor are on.
- **Step 6:** Disable binding mode on RC.
- **Step 7:** Confirm binding by having the receptor with a solid green light on and confirm by moving flight modes switches.

**Observed behavior by the user:**

- **Behavior after step 1-7:** The vehicle did not connect to RC, preventing the user from binding or calibrating the RC.

**Expected behavior:**

- **Expected behavior 1:** Vehicle should connect to RC.
- **Expected behavior 2:** User should be able to bind the RC.
- **Expected behavior 3:** RC calibration should be possible.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Suspected an electrical issue and mentioned replacing a flight controller due to bad vibrations and mag data.
- **URL of the flight log provided by the user:** PR13837 (https://review.px4.io/plot_app?log=51c918b7-763c-41c8-b7c8-4a162be0fd3d), Master (https://review.px4.io/plot_app?log=e9b18b85-685e-4f30-8931-9bfdafbc159a), along with several others for additional context.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Initially, no explicit suggestion was provided, but the issue was acknowledged and tested by `Junkim3DR`.
- **Result of the operation after the user adopted suggestion 1:** `Junkim3DR` confirmed that only the Stable firmware worked correctly.
  
- **Suggestion 2 provided by developers or other personnel:** Later tests indicated that both Stable and Master firmware versions started working as expected as logged by `Junkim3DR`.
- **Result of the operation after the user adopted suggestion 2:** `Tony3dr` confirmed the issue was resolved and closed the issue.
