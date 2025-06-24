# Basic Information:
### Title: DMA issue on fmuv6x with neopixel driver #20693
### Issue status: Closed
### Author: sebglatz
### Issue open time: Dec 1, 2022

# Report
### Report author: sebglatz
### Report Time: Dec 1, 2022
### Report Content:   
**Describe the bug:**  
Running the neopixel driver on a Holybro Pixhawk 6x does not produce the expected signal. The user employed the `srgbled_dma.cpp` version of the driver with the latest PX4 release (v1.13.2).

### **Environment where the bug occurred:**
- **Hardware environment:** Holybro Pixhawk 6x on baseboard mini, powered with USB-C.
- **Software environment:** PX4 Autopilot version 1.13.2.
- **Report Time:** Dec 1, 2022.
- **PX4 Autopilot commit version:** Not mentioned.
- **last commit before the reporting time:**c5dc122

### **Steps for bug reproduction:**
1. Add the following to `fmu-v6x/src/board_config.h`:
    ```bash
    \\\\#  define BOARD_HAS_N_S_RGB_LED          10        
    \\\\#  define S_RGB_LED_DMA                  DMAMAP_TIM5_CH4 /* Note, this is DMAMUX1 and DMA-Mux-Index 101 */        
    \\\\#  define S_RGB_LED_TIMER                5   /* timer 5   */        
    \\\\#  define S_RGB_LED_CHANNEL              4   /* channel 4  */        
    // \\\\#  define S_RGB_LED_CHANNELN           1   /* channel 4N */        
    \\\\#  define S_RGB_LED_TIM_GPIO             GPIO_TIM5_CH4OUT_2 /* PI0 aka FMU_CH1*/
    ```
2. Build and flash the firmware.
3. Run the following command in `nsh`:
   ```
   neopixel start
   ```

### **Observed behavior by the user:**
- **Behavior after step 1:** N/A
- **Behavior after step 2:** N/A
- **Behavior after step 3:** Signal on FMU_CH1 is either constantly zero, or, with DMA-debug-prints enabled and DMA on the serial console disabled, an irregular non-constant signal is observed. This signal does not match the expected PWM-like behavior.

### **Expected behavior:**
1. A PWM-like signal on pin FMU_CH1 with two different duty cycles:
   - Total bit time: 1200 ns.
   - 0b1: (600 ns | 600 ns).
   - 0b0: (300 ns | 900 ns).

### **Additional information provided by the user for bug investigation:**
- **Actions taken by the user:**
   - Debugging through print statements in `stm32h7/stm32_dma.c` (caused serial console to freeze unless DMA on the console was disabled).
   - Attempted reconfiguration of the serial console without DMA to avoid freezing issues.
- **URL of the flight log provided by the user:**  
  [Log link](https://logs.px4.io/plot_app?log=b063b920-a603-4820-9d73-71acd0f30f78)

---

# Communication between developers or other personnel and the user:

### **Suggestion 1 provided by developers or other personnel:**
- **Author:** davids5  
- **Time:** Mar 16, 2023  
- **Content:** Asked if the user validated that the `dma_handle` from `stm32_dmachannel(S_RGB_LED_DMA)` was not null.  

**Result of the operation after the user adopted suggestion 1:**  
- The user confirmed the `dma_handle` was not null but still faced the issue of LEDs not being driven and planned further testing with an oscilloscope.

---

### **Suggestion 2 provided by developers or other personnel:**
- **Author:** davids5  
- **Time:** Mar 20, 2023  
- **Content:** Suggested examining the DMA map and referenced the STM32H7 reference manual to determine DMA compatibility with TIM12. Mentioned that synchronous DMA requests might not be wired to the DMA mux for TIM12.

**Result of the operation after the user adopted suggestion 2:**  
- User clarified that TIM12-based DMA was incompatible for their application and moved to PWM_FMU5, which resolved some issues. LEDs turned on, but a reset issue persisted.

---

### **Suggestion 3 provided by developers or other personnel:**
- **Author:** davids5  
- **Time:** Mar 21, 2023  
- **Content:** Proposed two debugging approaches to resolve the reset voltage problem:
  1. Modify the last DMA bit to ensure the output is pulled low.
  2. Adjust the size of `bits` and DMA configuration to delay completion until the timer finishes.

**Result of the operation after the user adopted suggestion 3:**  
- Successfully resolved the reset issue, leading to stable LED operation. However, the user observed timing glitches in LED commands and suspected buffered data or preloaded bits.

---

### **Suggestion 4 provided by developers or other personnel:**
- **Author:** davids5  
- **Time:** Mar 24, 2023  
- **Content:** Recommended testing with `pwm_out_main` to isolate issues with the PWM output driver. Also requested a detailed list of DMA assignments.

**Result of the operation after the user adopted suggestion 4:**  
- User isolated the issue to the neopixel driver's interaction with startup scripts (`rc.board_defaults` or `rc.sensors`). Suspected that resources required by the driver were unavailable during initialization and suggested delaying its startup.

---

# Final Observations and Status:
1. The issue was eventually resolved for individual LED control using PWM_FMU5.
2. Persistent problems with driver stability during startup (green LED behavior and FCU crashes) require additional debugging and potential startup delays.
3. Users in the community continued to seek guidance on GPIO mappings and neopixel driver configurations.

**Bug Status:** Closed  
**Resolution:** Partial workaround achieved; further enhancements to the neopixel driver and documentation may be required.
