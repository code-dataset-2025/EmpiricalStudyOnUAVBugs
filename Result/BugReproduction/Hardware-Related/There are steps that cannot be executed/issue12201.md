**Environment where the bug occurred:**

- **Hardware environment:** Pixracer, Pixhawk 4
- **Software environment:** Ubuntu 16.04, Ubuntu 18.04, Raspbian
- **Report Time:** Jun 6, 2019
- **PX4 Autopilot commit version:** e12acc4 (with a previous fine revision, 8b71bb4)

**Steps for bug reproduction:**

- **Step 1:** Make sure no MAVLink receivers (QGroundControl, MAVROS, etc.) are running on your PC.
- **Step 2:** Connect your flight controller to a PC via USB.
- **Step 3:** Wait for the flight controller to boot (let it pass bootloader + wait for 1-2 sec).
- **Step 4:** Try to connect to the flight controller via MAVLink (using QGroundControl/MAVROS/mavlink_shell script). It turns out this was a bug in Ubuntu 16.04.<font color='red'>作者查明是ubuntu16.04下的bug，在18.04下执行到这一步无问题</font>

Alternatively:

- **Step 1:** Provide power to your flight controller through its power port.
- **Step 2:** Wait for the flight controller to boot + 1-2 sec.
- **Step 3:** Connect the flight controller to a PC via USB.
- **Step 4:** Try to connect to the flight controller via MAVLink.

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** N/A
- **Behavior after step 3:** N/A
- **Behavior after step 4:** The underlying serial device (/dev/ttyACM0 on Linux) appears in the system, but MAVLink connection is not established. (QGroundControl suggests rebooting the vehicle, mavlink_shell doesn't go anywhere past "Connecting to MAVLINK..." message)

**Expected behavior:**

- **Expected behavior 1:** MAVLink connection should be established.
- **Expected behavior 2:** QGroundControl should display the current FCU status.
- **Expected behavior 3:** MAVROS should report heartbeats.
- **Expected behavior 4:** mavlink_shell should display nsh > prompt.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Identified that the issue was present in v1.8.2, harder to notice due to a timing difference; bisected the bug to a specific commit; observed differences in behavior on different OS versions.
- **URL of the flight log provided by the user:** Not provided.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `julianoes` tried reproducing the issue and asked about hardware or host computer-specific issues.
- **Result of the operation after the user adopted suggestion 1:** User `sfalexrog` acknowledged the reply and noted that the issue was not present on Ubuntu 18.04, but persisted with external power, providing further testing insights.
- **Suggestion 2 provided by developers or other personnel:** Suggestions from `julianoes` and `davids5` involved looking at the commit and trying to address the timing/order of `mavlink` startup.
- **Result of the operation after the user adopted suggestion 2:** Not directly applicable, but `mcsauder` worked on identifying fixes and orders for startup scripts solving the issue in master but not in v1.9.1.
- **Suggestion 3 provided by developers or other personnel:** `davids5` suggested code changes to avoid infinite loops when the USB is unplugged.
- **Result of the operation after the user adopted suggestion 3:** Discussion on proper startup sequence and behavior when devices are plugged/unplugged led to a submitted fix PR #12428 by `mcsauder`, confirming the solution through follow-up testing.
