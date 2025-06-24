**Environment where the bug occurred:**

- **Hardware environment:** Duo Tailsitter
- **Software environment:** PX4 Autopilot with branch modification from tag v1.8.1
- **Report Time:** Jan 15, 2019
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**d8ab059

**Steps for bug reproduction:**

- **Step 1:** Put the aircraft in position mode (multi-rotor).
- **Step 2:** Arm the aircraft.
- **Step 3:** Raise throttle input to be above 50%.
- **Step 4:** Raise the aircraft itself by hand.
- **Step 5:** Flip the transition switch from MC to FW.
- **Step 6:** Flip the aircraft from vertical to horizontal orientation (this is a tailsitter).
- **Step 7:** Accelerate the airflow in the front of the aircraft from 0 m/s to transition airspeed gradually.

**Observed behavior by the user:**

- **Behavior after step 7:** The aircraft switches from MC to FW and throttle drops to zero.

**Expected behavior:**

- **Expected behavior 1:** Throttle should not drop to zero.
- **Expected behavior 2:** Aircraft should remain controllable after transition.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Identified potential issues in the code, specifically with the handling of the _thrust_transition variable. Attempted fixes and conducted bench tests.
- **URL of the flight log provided by the user:** 
  - [Flight with throttle drop](https://logs.px4.io/plot_app?log=5f2f02c7-d2bd-4ff3-9d10-c48c87272d2f)
  - [Flight without throttle drop](https://logs.px4.io/plot_app?log=4eed6594-9aaf-4026-a571-202857b4c387)
  - [Bench-test attempts](https://logs.px4.io/plot_app?log=cade9885-e8c0-48e0-a730-1658fb1c69c4), [1](https://logs.px4.io/plot_app?log=e38fdf1f-58cd-4fd9-8ce1-a964cee2b72e), [2](https://logs.px4.io/plot_app?log=2ac76818-9c41-4b5e-b865-1a74b5623578), [3](https://logs.px4.io/plot_app?log=fe89ef0b-9b6d-4473-8810-911d028d638d), [4](https://logs.px4.io/plot_app?log=ebd3c67a-2ebf-4028-ac8d-216dc5e25822)

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** `dagar` asked for the closest commit reference as the issue was not on PX4/master.
- **Result of the operation after the user adopted suggestion 1:** `tecnic08` mentioned it was a slight modification from tag v1.8.1.
- **Suggestion 2 provided by developers or other personnel:** `tecnic08` suggested modifying _thrust_transition value to avoid throttle dropping to zero.
- **Result of the operation after the user adopted suggestion 2:** Conducted bench tests to verify the fix.
- **Suggestion 3 provided by developers or other personnel:** `tecnic08` proposed providing a parameter to limit the sink rate, preventing the throttle from dropping to zero.
- **Result of the operation after the user adopted suggestion 3:** Confirmed it addressed the issue.

