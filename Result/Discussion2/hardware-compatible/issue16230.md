**Environment where the bug occurred:**

- **Hardware environment:** Reproducible with bare board hooked up over USB (Pixhawk 4)
- **Software environment:** PX4 Autopilot latest master (commit version not mentioned)
- **Report Time:** Nov 19, 2020
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**71306f7

**Steps for bug reproduction:**

- **Step 1:** Fetch latest master f18e700.
- **Step 2:** Flash a Pixhawk 4 with `make fmu-v5 upload`.
- **Step 3:** When it boots, hear fast beeping all the time, and IO pins don't come up.
- **Step 4:** Use MAVLink shell.

**Observed behavior by the user:**

- **Behavior after step 1:** Not specified.
- **Behavior after step 2:** Not specified.
- **Behavior after step 3:** Fast beeping sounds constantly, and IO pins don't become operational.
- **Behavior after step 4:** Not specified.

**Expected behavior:**

- **Expected behavior 1:** IO chip should flash correctly.
- **Expected behavior 2:** Beeping should stop.
- **Expected behavior 3:** IO pins should become operational.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Not explicitly mentioned, reported a clue with dmesg output repeatedly showing "px4io bad sync".
- **URL of the flight log provided by the user:** [https://photos.app.goo.gl/YB4pTSUkK7eiz3FN7](https://photos.app.goo.gl/YB4pTSUkK7eiz3FN7)

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** `davids5` noted "I see the issue......"
- **Result of the operation after the user adopted suggestion 1:** Not specified as it was an acknowledgment.
- **Suggestion 2 provided by developers or other personnel:** `davids5` suspected a timing change but noted it wasn't that simple.
- **Result of the operation after the user adopted suggestion 2:** Not specified.
- **Other comments:** `MaEtUgR` thanked `davids5` for identifying the issue.
