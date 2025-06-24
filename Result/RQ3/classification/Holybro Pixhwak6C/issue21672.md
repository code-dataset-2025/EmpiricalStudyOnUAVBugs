**Environment where the bug occurred:**

- **Hardware environment:** Holybro s500v2 kit with Pixhawk 6C
- **Software environment:** Latest master branch of PX4 Autopilot (specific commit version not mentioned)
- **Report Time:** Jun 2, 2023
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**2f448e9

**Steps for bug reproduction:**

- **Step 1:** Switch on the drone.
- **Step 2:** Ensure the status on QGroundControl is "Ready To Fly."
- **Step 3:** Take off.

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** N/A
- **Behavior after step 3:** Only one motor is spinning.

**Expected behavior:**

- **Expected behavior 1:** All four motors should spin.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Upgraded firmware using the command `make px4_fmu-v6c_default upload`; provided screenshots from PWM info and PX4IO status.
- **URL of the flight log provided by the user:** Not provided.

**Communication between developers or other personnel and the user:**

There is no information on communication between developers or others and the user provided in the document.
