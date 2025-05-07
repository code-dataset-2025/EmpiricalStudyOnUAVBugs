**Environment where the bug occurred:**

- **Hardware environment:** Pixhawk 4
- **Software environment:** PX4 Autopilot
- **Report Time:** Jul 31, 2018
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**6d662c5<font color='red'>该版本无法编译，论坛中修复方法所缺的.h文件所属网页已经不存在，使用距离最近的realease代替</font>

**Steps for bug reproduction:**

- **Step 1:** Select 'Quad H4 680' airframe on QGroundControl (QGC).<font color='red'>在QGC中找不到该机架，更换至发报告前版本QGC也同样找不到</font>

**Observed behavior by the user:**

- **Behavior after step 1:** Pixhawk does the start-up tune but thereafter, no communication with the PC via USB is possible, and parameters can't be changed.

**Expected behavior:**
- **Expected behavior 1:** Pixhawk should allow for parameter changes via USB after airframe selection.
- **Expected behavior 2:** Communication with the PC should be maintained after selecting any airframe.

**Additional information provided by the user for bug investigation:**
- **Actions taken by the user:** Recovering the Pixhawk was only possible by placing an `rc.txt` file on the SD card with the 'param reset' command.
- **URL of the flight log provided by the user:** Not provided.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `dagar` asked if the user had successfully used the airframe before.
- **Result of the operation after the user adopted suggestion 1:** User `BazookaJoe1900` clarified that they did not possess or use the airframe and only intended to view its parameters.
