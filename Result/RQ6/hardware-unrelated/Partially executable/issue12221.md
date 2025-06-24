**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned
- **Software environment:** PX4 Autopilot with commit 43e3fc7 and later up to b0176dc
- **Report Time:** Jun 9, 2019
- **PX4 Autopilot commit version:** 43e3fc7 and later up to b0176dc

**Steps for bug reproduction:**

- **Step 1:** Load commit version and ensure a totally clean build/initialization using the following commands:

    ```bash
    cd <FIRMWARE LOCATION>
    git checkout <COMMIT UNDER TEST>
    make clean
    git submodule update
    rm ~/.ros/eeprom/parameters
    make px4_sitl_default gazebo_typhoon_h480
    ```

    <font color='red'>rm ~/.ros/eeprom/parameters这步出错，找不到该文件</font>

- **Step 2:** Execute `roslaunch px4 mavros_posix_sitl.launch vehicle:=typhoon_h480`

- **Step 3:** Arm / transition to offboard mode

- **Step 4:** Send position target

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** N/A
- **Behavior after step 3:** N/A
- **Behavior after step 4:** Unstable position control behavior, with error message "Critical navigation failure! Check sensor calibration" logged. Z position control is very poor, with high oscillations upon new z position setpoints.

**Expected behavior:**

- **Expected behavior 1:** Stable position control behavior, similar to behaviour observed in commit 4a4d323

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** The user noted stable performance with the Iris model and mentioned the issue might be related to not clearing parameter files between different build levels.
- **URL of the flight log provided by the user:** 
  - Stable behavior: [Log](https://logs.px4.io/plot_app?log=6c788665-95f7-4b2b-a963-9ad58911024c)
  - Unstable behavior: [Log](https://logs.px4.io/plot_app?log=894c8553-18b1-4fc1-ad4a-d1587485637e)

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** FlavioTonelli clarified that the issue was still open despite the weekly digest implying otherwise.
- **Result of the operation after the user adopted suggestion 1:** N/A (user acknowledged the clarification)
  
- **Suggestion 2 provided by developers or other personnel:** Jaeyoung-Lim inquired if the issue persisted and mentioned current master performs correctly.
- **Result of the operation after the user adopted suggestion 2:** The user confirmed the issue persisted with the latest master and reiterated the importance of following clean build steps.

- **Suggestion 3 provided by developers or other personnel:** Jaeyoung-Lim intended to investigate further acknowledging the current workload may delay this.
- **Result of the operation after the user adopted suggestion 3:** No immediate resolution but later Jaeyoung-Lim reported successfully flying without issues, advising to reopen if the problem persists.
