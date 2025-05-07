Here is the extracted and formatted information for the given bug report:

---

**Environment where the bug occurred:**

- **Hardware environment:** Any VTOL which needs to shut down motors during fixed-wing flight and doesn't use PWM control for the motors.
- **Software environment:** Not explicitly mentioned.
- **Report Time:** Jan 20, 2021.
- **PX4 Autopilot commit version:** Not mentioned.
- **last commit before the reporting time:**9a06695

**Steps for bug reproduction:**

- **Step 1:** Observe that `VtolType::set_motor_state` calls `apply_pwm_limits` directly, opening a PWM device.
- **Step 2:** Note that UAVCAN and other communication protocols are ignored.

**Observed behavior by the user:**

- **Behavior after step 1:** PWM devices are opened and managed, but UAVCAN ESCs are ignored.
- **Behavior after step 2:** The parameter `VT_FW_MOT_OFFID` does not disable the motors using UAVCAN or other non-PWM protocols.

**Expected behavior:**

- **Expected behavior 1:** Setting `VT_FW_MOT_OFFID` should disable motors irrespective of the communication protocol (e.g., UAVCAN or PWM).
- **Expected behavior 2:** The parameter should function seamlessly for all ESC types as suggested by the documentation.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** User suggested architectural changes, such as managing motor state directly in the `MultiRotorMixer` and sending motor enable/disable messages from `vtol_att_control`. They also questioned whether the motor slew rate could replace the current workaround for ramping down propellers in tiltrotor configurations.
- **URL of the flight log provided by the user:** Not provided.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:**  
  Developer `taileron` mentioned that this issue also applies to PWM outputs on the FMU, which remain on and are not managed.
- **Result of the operation after the user adopted suggestion 1:** N/A (no operation changes described).
  
- **Suggestion 2 provided by developers or other personnel:**  
  User `pjdewitte` proposed addressing the issue in the `MultiRotorMixer` to take motor slew rate into account and simplify the system by removing tiltrotor-specific workarounds.
- **Result of the operation after the user adopted suggestion 2:** N/A (suggestion under discussion).

- **Suggestion 3 provided by developers or other personnel:**  
  Developer `bkueng` noted that with recent changes (#19990), the system now has more flexibility, and the issue should be resolved.
- **Result of the operation after the user adopted suggestion 3:** Issue closed, implying the problem was likely resolved.

---
