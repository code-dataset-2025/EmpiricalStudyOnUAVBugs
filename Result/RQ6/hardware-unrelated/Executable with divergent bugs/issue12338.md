**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned
- **Software environment:** PX4 Autopilot
- **Report Time:** Jun 26, 2019
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**49966f4

**Steps for bug reproduction:**

- **Step 1:** Set `MPC_THR_HOVER` to a value of 59 (instead of the correct 0.59).
- **Step 2:** In QGroundControl (QGC), this value has to be entered as 5900, but in a startup script, it can be entered as 59.

**Observed behavior by the user:**

- **Behavior after step 1:** An incorrect `MPC_THR_HOVER` value gets passed unconstrained to the manual thrust setpoint.
- **Behavior after step 2:** The thrust setpoint can result in a value of 50, where the mixer expects values between 0 and 1.0.<font color='red'>修改为59后，无人机不受控制笔直向上爬升，但log中Actuator controls的图表值范围仍在0-1，而非报告中描述的超过1。https://review.px4.io/plot_app?log=a58e0a35-e177-4b0a-a3ae-8810da71f6af</font>

**Expected behavior:**

- **Expected behavior 1:** The hover thrust setpoint should not exceed 1.0 or `MPC_THR_MAX`.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** None explicitly mentioned, but acknowledged a mistake in setting the parameter incorrectly.
- **URL of the flight log provided by the user:** [Flight log](https://review.px4.io/plot_app?log=4a38b5fc-4684-4b16-9313-16dcda6294cd)

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** The user mentioned that it was a "dumb mistake" due to incorrect entry. No official suggestions or communication from developers are documented in the provided content.

