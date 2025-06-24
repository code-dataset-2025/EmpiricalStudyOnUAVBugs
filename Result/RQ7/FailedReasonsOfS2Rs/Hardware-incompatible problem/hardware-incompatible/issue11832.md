**Environment where the bug occurred:**

- **Hardware environment:** Pixhawk 2.1 cube
- **Software environment:** PX4 Autopilot version 1.8.2
- **Report Time:** Apr 10, 2019
- **PX4 Autopilot commit version:** not mentioned
- **last commit before the reporting time:**f0ce064

**Steps for bug reproduction:**

- **Step 1:** Run the cube with temperature calibration bits enabled using stock firmware version 1.8.2 until all temperatures stabilize. Check the temperatures on each sensor.
- **Step 2:** Modify the firmware to disable the Green LED_RING, ensure LED_BLUE() never turns on, and set px4io GPIO_LED1 to push-pull to force the heater off.<font color='red'>pixhawk4中没有类似cube中的加热器</font>
- **Step 3:** Run the same temperature stabilization test as in step 1 and note the differences in sensor temperatures.

**Observed behavior by the user:**
- **Behavior after step 1:** Initial temperatures are observed with the heater not fully off.
- **Behavior after step 2:** The heater is forced off, but specific sensor temperature outcomes after this step were not mentioned. 
- **Behavior after step 3:** A reduction of 20-25°C in sensor temperatures was observed.

**Expected behavior:**
- **Expected behavior 1:** The heater should be fully off when modified as per the steps, resulting in lowered sensor temperatures.
- **Expected behavior 2:** The internal cube sensors should remain within their operational temperature specifications during temperature calibration.

**Additional information provided by the user for bug investigation:**
- **Actions taken by the user:** Modified code files to disable heater and LEDs, experimented with different configurations on Pixhawk 2.1 hardware.
- **URL of the flight log provided by the user:** Not provided.

**Communication between developers or other personnel and the user:**
- **Suggestion 1 provided by developers or other personnel:** Developer `davids5` requested testing with #11833 addressing only the heater issue and suggesting the user disable the hardware-specific light ring by undefining `GPIO_LED4`.
- **Result of the operation after the user adopted suggestion 1:** Not explicitly mentioned.
- **Suggestion 2 provided by developers or other personnel:** No additional suggestion beyond the initial test request.
- **Result of the operation after the user adopted suggestion 2:** N/A.
- **Suggestion n provided by developers or other personnel:** The issue was closed by `LorenzMeier`, with advice to re-open a separate issue for the ring if needed.
