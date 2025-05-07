**Environment where the bug occurred:**

- **Hardware environment:** In-air GPS device (no base station required) with access to System Console
- **Software environment:** Not explicitly mentioned
- **Report Time:** Mar 25, 2019
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**ed2d4f6

**Steps for bug reproduction:**

- **Step 1:** Clone the external repository.
- **Step 2:** Go to PX4-firmware and clean the build.
  ```bash
  cd <px4-src-dir>
  make clean
  ```
- **Step 3:** Add PX4_INFO logging at specific lines in the code.
- **Step 4:** Build your target and upload, including the external module-repo.
  ```bash
  make <target> EXTERNAL_MODULES_LOCATION=<path to external_module> upload
  ```
- **Step 5:** Open System console and turn on the drone: You should see the gps-read print.
- **Step 6:** Open mavlink-shell.
  ```bash
  ./Tools/mavlink_shell.sh
  ```
- **Step 7:** Start gps_injection_app from the mavlink-shell.
  ```bash
  nsh> gps_injection_app start
  ```

**Observed behavior by the user:**
- **Behavior after step 7:** The gps-driver becomes occupied with writing to the Rover and does not perform any read operations, resulting in GPS loss during data bursts from the Base.

**Expected behavior:**
- **Expected behavior 1:** Reading from the GPS device should continue despite writing to the device.

**Additional information provided by the user for bug investigation:**
- **Actions taken by the user:** 
  - Added logging to observe the writing and reading operations on the GPS device.
  - Proposed a workaround by reading data from the Rover after a predefined amount of data is written to it.
- **URL of the flight log provided by the user:** None provided.

**Communication between developers or other personnel and the user:**
- **Suggestion 1 provided by developers or other personnel:** Limit the maximum duration inside the while loop or the maximum number of messages processed.
- **Result of the operation after the user adopted suggestion 1:** A modified implementation with limited while-loop iterations to guarantee sequential message handling.
- **Suggestion 2 provided by developers or other personnel:** Modify the logic to prevent messages from being lost by checking buffer space before writing.
- **Result of the operation after the user adopted suggestion 2:** A solution was tested and confirmed that prevented GPS-loss by guaranteeing read operations, but concerns remained about complete message transmission.
- **Further discussions:** 
  - Suggestions to reconstruct messages based on the flag in the Mavlink message indicating message fragmentation.
  - Reports and solutions were tested on private forks, with eventual agreement to create a pull request based on a suggested solution for better handling of the loop execution.
