**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned
- **Software environment:** PX4 Autopilot
- **Report Time:** Sep 23, 2019
- **PX4 Autopilot commit version:** [commit 41516fbd5532cdb5c8beb2e519ca4d8e5247a579](https://github.com/PX4/Firmware/blob/41516fbd5532cdb5c8beb2e519ca4d8e5247a579/src/modules/vtol_att_control/standard.cpp#L460)

**Steps for bug reproduction:**

- **Step 1:** Perform a transition in Software In The Loop (SITL).
- **Step 2:** Check the logs for throttle behavior after transition.

**Observed behavior by the user:**

- **Behavior after step 1:** Transition completes.
- **Behavior after step 2:** Fixed-wing (FW) throttle briefly drops to 0 after the front transition is completed.<font color='red'>执行后转换有这种情况（不知道是否正常），但报告中提到的前转换过程中没有</font>

**Expected behavior:**

- **Expected behavior 1:** Throttle should smoothly transition from transition throttle to the user-commanded throttle in stabilized mode or match the throttle output from TECS.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** User provided a hypothesis about the cause related to throttle setpoints not being initialized correctly before they're used after transitioning.
- **URL of the flight log provided by the user:** Not provided.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Comment by `sfuhrer` suggesting the issue might have surfaced due to recent workload queue (wq) changes.
- **Result of the operation after the user adopted suggestion 1:** Not applicable; the suggestion was an observation, not an actionable step.
- **Suggestion 2 provided by developers or other personnel:** None provided.
- **Result of the operation after the user adopted suggestion 2:** Not applicable.
- **Suggestion n provided by developers or other personnel:** Issue was acknowledged to be related to another issue (#13030) and its respective pull request that fixed it (#13031).
- **Result of the operation after the user adopted suggestion n:** Issue was closed as it was resolved by the related pull request.
