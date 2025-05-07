# Basic Information:
### Title:  Sporadic PARAM_VALUE message being sent through an Iridium interface #21496
### Issue status: Closed
### Author: lvanasse
### Issue open time: Apr 19, 2023
### Fixed by: #21510

# Report
### Report author: lvanasse
### Report Time: Apr 19, 2023
### Report Content:  
**Describe the bug**  
When using an Iridium interface with a MAVLink instance in Iridium mode, sporadic `PARAM_VALUE` MAVLink messages are sent through the Iridium interface. This is problematic because the user does not want these messages to be sent through that interface, or at least wishes to control this behavior.  

**Steps to reproduce the bug:**  
1. Connect an IridiumSBD module to the Pixhawk.  
2. Enable the IridiumSBD driver in the firmware.  
3. Comment out the commands in the `module.yaml` file of the IridiumSBD.  
4. Power everything up.  
5. Start the IridiumSBD driver using the command:  
   `iridiumsbd start -v -d /dev/ttyS5`  
6. Start the MAVLink instance using the command:  
   `mavlink start -d /dev/iridium -m iridium -b 115200`  
   (A custom MAVLink mode similar to the Iridium one is used).  
7. Observe that sporadic `PARAM_VALUE` messages are written onto the Iridium interface.  

**Observed behavior by the user:**  
- Occasionally, `PARAM_VALUE` messages are written onto the Iridium interface, which is not desired.  
- In some cases, the writing on the Iridium interface fails if there is no communication with the satellite constellation. This behavior is expected.  
- The user noted that the buffer sometimes resets and starts from the beginning, invalidating previous behavior.

**Expected behavior:**  
- The user expected to block the `PARAM_VALUE` messages from being written onto the Iridium interface.  
- Desired behavior includes implementing a circular buffer where streams overwrite themselves if the buffer is full.

**Additional information provided by the user for bug investigation:**  
- **Actions taken by the user:**  
  - Investigated the issue by analyzing the `MavlinkParametersManager` code.  
  - Determined that the `send_param()` function in the `MavlinkParametersManager` is responsible for sending the `PARAM_VALUE` message through the MAVLink instance.  
  - Identified that this function is indirectly called by the `MavlinkReceiver::run()` function when certain conditions are met.  
- **URL of the flight log provided by the user:**  
  - [Flight log](https://logs.px4.io/plot_app?log=3cd87690-3dd5-44c4-9d1c-de8da82a8b7b)  

**Environment where the bug occurred:**  
- **Hardware environment:** Pix32 V6, M8N GPS, and IridiumSBD 9603 module  
- **Software environment:** Not explicitly mentioned  
- **Report time:** Apr 19, 2023  
- **PX4 Autopilot commit version:** Not mentioned  
- **last commit before the reporting time:**0934d3b

# Communication between developers or other personnel and the user:
## Comment 1
- **Comment author:** lvanasse  
- **Comment time:** Apr 25, 2023  
- **Comment content:**  
  - Provided additional details about the issue and the functions involved (`send_param`, `send_untransmitted`, and `send_params`).  
  - Proposed creating a pull request (PR) to address the issue.

## Comment 2
- **Comment author:** DronecodeBot  
- **Comment time:** Apr 25, 2023  
- **Comment content:**  
  - Mentioned that this issue was referenced in the PX4 community discussion forums.  
  - [Relevant discussion link](https://discuss.px4.io/t/px4-community-q-a-april-26-2023/31839/3)  

**Resolution:**  
- The issue was fixed in PR #21510.  

**Additional Notes:**  
- The user was proactive in investigating the issue and provided a detailed analysis of the relevant functions.  
- The resolution was expedited, likely due to the user’s clear and thorough explanation.
