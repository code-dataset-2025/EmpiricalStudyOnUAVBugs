**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned
- **Software environment:** PX4 Autopilot
- **Report time:** Oct 12, 2022
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**bdd043f

**Steps for bug reproduction:**

- **Step 1:** Reproduce in Software In The Loop (SITL)
- **Step 2:** Use a tiltrotor model

**Observed behavior by the user:**

- **Behavior after step 1:** There is often some leftover (unallocated) yaw torque<font color='red'>log格式发生变化，缺少相同的图像对比来反映是否发生bug</font>
- **Behavior after step 2:** The leftover yaw torque exists even though the tilts are not saturating

**Expected behavior:**

- **Expected behavior 1:** No unallocated yaw torque unless actuators are actually saturating
- **Expected behavior 2:** Avoid having a frozen integrator for half of the flight

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Identified that the unsaturation method likely doesn't work well because it's very customized for pure multicopters
- **URL of the flight log provided by the user:** Not provided

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `sfuhrer` suggested either moving to a customized allocation for tiltrotors or making the desaturation less multicopter-specific
- **Result of the operation after the user adopted suggestion 1:** Not directly adopted, but considered as a clean solution
- **Suggestion 2 provided by developers or other personnel:** `sfuhrer` proposed parametrizing the thresholds for saturation detection as a short-term fix
- **Result of the operation after the user adopted suggestion 2:** Not explicitly mentioned
- **Suggestion 3 provided by developers or other personnel:** Developer `bkueng` suggested letting the allocation publish saturation values in the fixed range of [-1, 1] for gradual reduction by the rate controller and using a more appropriate desaturation logic for tiltrotors
- **Result of the operation after the user adopted suggestion 3:** Not explicitly mentioned, but solution similar to the discussion was implemented as indicated by the closing of the issue with reference to \#20518
