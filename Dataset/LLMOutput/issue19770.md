**Environment where the bug occurred:**

- **Hardware environment:** Holybro Pixhawk 4 (FMUv5), FMUv6X, FMUv6C
- **Software environment:** PX4 Master branch
- **Report Time:** Jun 7, 2022
- **PX4 Autopilot commit version:** 639222d

**Steps for bug reproduction:**

- **Step 1:** Power on the flight controller (using PX4 Master) with GPS attached.
- **Step 2:** Open QGroundControl (QGC); observe the message "Preflight Fail: height estimate not stable" and a height display of `--.-- m`.<font color='red'>此处错误不一致，为magnetometer 2 error和pre-arm check error</font>
- **Step 3:** Wait a few minutes.<font color='red'>等待后错误也没有消失</font>
- **Step 4:** Observe that the error goes away a couple of minutes after the GPS achieves 3D fix.
- **Step 5:** Remove the GPS and reboot the system; the error does not occur.<font color='red'>拔掉gps重启后错误同样消失</font>

**Observed behavior by the user:**

- **Behavior after step 1:** "Preflight Fail: height estimate not stable" appears, and height displays as `--.-- m`.
- **Behavior after step 3:** No immediate change in behavior.
- **Behavior after step 4:** Error disappears after GPS achieves 3D fix.
- **Behavior after step 5:** Error does not occur when the GPS is removed and the system is rebooted.

**Expected behavior:**

- **Expected behavior 1:** The preflight error "Preflight Fail: height estimate not stable" should not occur.
- **Expected behavior 2:** The height value in QGC should display correctly.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:**
  - Tested on multiple hardware setups, including FMUv5, FMUv6X, and FMUv6C.
  - Mentioned that the issue was not present in the FMUv6C build from May 10, 2022.
  - Provided logs and identified commit 639222d as the cause of the problem.

- **URL of the flight log provided by the user:**
  - Log after boot with the problematic commit: [Log link](https://logs.px4.io/plot_app?log=006f8348-9c12-4285-a0a3-50c93d04c17b)
  - Log from one commit before the problematic commit (drone switches to Altitude mode, vertical movement reported): [Log link](https://logs.px4.io/plot_app?log=585a7fda-a70c-4391-a8c5-66fdad38681e)
  - Log with the problematic commit (drone does not switch to Altitude mode, vertical movement not reported): [Log link](https://logs.px4.io/plot_app?log=ffd970f3-74b0-414c-b751-3aa6753a7dec)

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:**
  - Developer `MaEtUgR` identified that the issue is caused by commit 639222d.
  - It was discovered that this commit reports the innovations of all sensors, including those not in use, which causes altitude to be declared invalid when preflight checks act on GPS altitude without a valid fix.

- **Result of the operation after the user adopted suggestion 1:**
  - No direct action by the user, but the problematic commit was identified and logged.

- **Suggestion 2 provided by developers or other personnel:**
  - Developer `MaEtUgR` discussed how, prior to the commit, the setup would switch to Altitude mode before connecting to the ground station, which no longer occurred post-commit.

- **Result of the operation after the user adopted suggestion 2:**
  - No immediate resolution mentioned, but this behavior reinforced the identification of the issue with the specific commit.

- **Further communication:**
  - Developer `MaEtUgR` actively tested and provided multiple logs for investigation.
  - Developer `bresch` brought in additional expertise from `@MaEtUgR`.
  - Developer `vincentpoont2` sought input from `@dagar` and others for a collaborative investigation.
