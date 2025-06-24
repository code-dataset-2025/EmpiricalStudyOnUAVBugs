**Environment where the bug occurred:**

- **Hardware environment:** Cube Black, Here2/Here3 GPS modules
- **Software environment:** PX4 firmware versions 1.11.1 and 1.10.1
- **Report Time:** Nov 5, 2020
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**91d1825

**Steps for bug reproduction:**

- **Step 1:** Flash Cube Black's firmware to either PX4 1.11.1 or 1.10.1.
- **Step 2:** Connect Here2 or Here3 to CAN1 or CAN2 port.
- **Step 3:** Observe Here2/3 lights turn blue before quickly turning off.
- **Step 4:** Use MAVLink Inspector to check GPS_RAW_INT messages with fix_type 0.

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** N/A
- **Behavior after step 3:** Here2/3 lights turn blue and then off.
- **Behavior after step 4:** GPS_RAW_INT messages display fix_type 0 indicating GPS_FIX_TYPE_NO_GPS.

**Expected behavior:**

- **Expected behavior 1:** GPS_RAW_INT messages should have a fix_type other than 0 due to the connected GPS module.
- **Expected behavior 2:** Here2/3 lights should be flashing green.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** 
  - Tested with both static and dynamic Node ID settings for GPS modules.
  - Checked for known issues related to Here2 and Here3 in similar configurations.
  - Verified module settings (rev 2.2) not having internal switch issues.
  - Consulted a colleague with more experience who tested the GPS outdoors.

- **URL of the flight log provided by the user:** Not provided.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by mattpaddock:** Ensure the internal switch on the Here2 is set to CAN mode.
- **Result of the operation after the user adopted suggestion 1:** Not applicable as the user already verified there was no issue with the internal switch.
  
- **Suggestion 2 provided by JacobCrabill:** Investigate uORB data being published for more details.
- **Result of the operation after the user adopted suggestion 2:** User discovered the GPS was working correctly outside and acknowledged a potential non-conformation to MAVLink spec by PX4.

- **Further communication:** User did not file a new issue regarding the MAVLink spec, as the company switched to Ardupilot.
