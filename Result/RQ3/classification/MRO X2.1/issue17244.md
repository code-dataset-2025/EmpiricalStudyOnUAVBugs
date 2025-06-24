**Environment where the bug occurred:**

- **Hardware environment:** x2.1 Autopilot, Standard Plane vehicle type.
- **Software environment:** PX4 Autopilot v1.11.3
- **Report Time:** Mar 26, 2021
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**b1c9132

**Steps for bug reproduction:**

- **Step 1:** Connected a new X2.1, preinstalled with Ardupilot, to QGroundControl (QGC) and verified that the mag was detected.
- **Step 2:** Used QGC to change the firmware to PX4, which automatically loaded px4_fmu-v3.
- **Step 3:** Executed "uorb top" to check for the mag or IMUs, but none were shown.
- **Step 4:** Performed the x2.1 SD bootloader upgrade.
- **Step 5:** Used QGC to change the firmware, which automatically loaded auav-x21_default.px4.
- **Step 6:** Executed "uorb top" to check again; accels and gyros were shown but not the mag.
- **Step 7:** Completed QGC compass calibration but no compass was calibrated.
- **Step 8:** Changed the firmware using QGC and manually loaded mro_x21_default.px4 (1.11.3).
- **Step 9:** Executed "uorb top" once more; accels and gyros were shown but not the mag.
- **Step 10:** Completed QGC compass calibration again, still no compass was calibrated.
- **Step 11:** Repeated the entire process on a second X2.1 autopilot.

**Observed behavior by the user:**
- **Behavior after step 2:** PX4 firmware loaded px4_fmu-v3 unexpectedly.
- **Behavior after step 3:** "uorb top" did not display the mag or any IMUs.
- **Behavior after step 6 and 9:** "uorb top" showed both accels and gyros but omitted the mag.
- **Behavior after step 7 and 10:** No compass was calibrated, with mag IDs and mag_comp still at zero.

**Expected behavior:**
- **Expected behavior 1:** The onboard mag should appear in the mavlink console.
- **Expected behavior 2:** The onboard mag should be shown as calibrated after performing a QGC compass calibration.

**Additional information provided by the user for bug investigation:**
- **Actions taken by the user:** Conducted tests with the pre-installed Ardupilot, performed bootloader upgrade, and repeated the process on a second autopilot to confirm consistency of the issue.
- **Additional context:** User noted that he had similar issues on a third X2.1 but was able to see and calibrate external mags. With the X2.1-777, the mag was visible, but failed on other functionalities like PPM in.

**Communication between developers or other personnel and the user:**
- **Suggestion 1 provided by developers or other personnel:** Developer `dagar` questioned if the only internal mag is from the mpu9250 and acknowledged disabling the magnetometer in updates for performance reasons.
- **Result of the operation after the user adopted suggestion 1:** User confirmed the only mag is the mpu9250 and likes having it for preflight checks.
- **Suggestion 2 provided by developers or other personnel:** Developer `dagar` proposed trying out #17246.
- **Result of the operation after the user adopted suggestion 2:** User verified the solution worked, mentioned the mag showed up, field readings were sensible, calibration successful, and accels and gyros were still visible.
