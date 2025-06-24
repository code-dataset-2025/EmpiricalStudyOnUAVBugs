# Basic Information:
### Title: Hardware detection doesn't work on Cube Black with CAN1 connected #21102
### Issue status: Closed
### Author: julianoes
### Issue open time: Feb 9, 2023
### Fixed by: #21342

# Report
### Report author: julianoes
### Report Time: Feb 9, 2023
### Report Content:  
**Describe the bug:**  
When a CAN peripheral like Here3+ is connected to CAN1 on CubeBlack, the hardware detection fails and the sensors are not started correctly.  
With CAN connected, the output is:  
```bash
bad version detected, forcing to fmu-v2        
FMUv2 ver 0x8 : Rev 0 V2        
```
And sometimes it even gets detected as a Mini:  
```bash
FMUv2 ver 0xA : Rev 0 V2M        
```
Without CAN connected, it is correct:  
```bash
FMUv2 ver 0xE : Rev 0 V30        
```

**To Reproduce:**  
1. Flash `px4-fmu-v3` to CubeBlack.  
2. Connect something to CAN like Here3+.  
3. Power on using USB.  
4. Check boot output (e.g., on CONS 3-pin port, pin closest to Cube is GND, then Rx, then Tx).  

**Relevant code section:**  
This issue pertains to the detection code in the file:  
`PX4-Autopilot/boards/px4/fmu-v3/src/init.c`.  

# Bug Details

### Environment where the bug occurred:
- **Hardware environment:** CubeBlack, CAN peripheral (e.g., Here3+).
- **Software environment:** PX4 Autopilot running `px4-fmu-v3`.
- **Report Time:** Feb 9, 2023.
- **PX4 Autopilot commit version:** Not mentioned.
- **last commit before the reporting time:**b9f9f25

### Steps for bug reproduction:
- **Step 1:** Flash `px4-fmu-v3` to CubeBlack.  
- **Step 2:** Connect a CAN peripheral (e.g., Here3+) to CAN1.  
- **Step 3:** Power on using USB.  
- **Step 4:** Check the boot output (e.g., via the CONS 3-pin port).  

### Observed behavior by the user:
- **Behavior after step 3:** The hardware is incorrectly detected with outputs like:
  - `bad version detected, forcing to fmu-v2`  
    `FMUv2 ver 0x8 : Rev 0 V2`
  - Sometimes, it gets detected as Mini:  
    `FMUv2 ver 0xA : Rev 0 V2M`.  
- **Behavior after step 4:** When CAN is not connected, the output is correct:  
  `FMUv2 ver 0xE : Rev 0 V30`.

### Expected behavior:
- **Expected behavior 1:** The hardware should be correctly detected when a CAN peripheral is connected to CAN1 on CubeBlack.  
- **Expected behavior 2:** Sensor initialization should proceed without issues regardless of the CAN connection.

### Additional information provided by the user for bug investigation:
- **Actions taken by the user:** Provided relevant code section and reproduction steps.  
- **URL of the flight log provided by the user:** Not provided.

### Communication between developers or other personnel and the user:
- **Suggestion 1 provided by developers or other personnel:** User tagged developer `@davids5` for input.  
- **Result of the operation after the user adopted suggestion 1:** Not mentioned.  

# Fix:
The issue was fixed by pull request #21342.
