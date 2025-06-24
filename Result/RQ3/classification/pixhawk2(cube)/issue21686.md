**Environment where the bug occurred:**

- **Hardware environment:** Large fixed wing. FCU is a CubePilot Orange, using the internal IMUs.
- **Software environment:** PX4 Autopilot v1.14.0-beta2
- **Report Time:** Jun 6, 2023
- **PX4 Autopilot commit version:** commit 18898f1

**Steps for bug reproduction:**

- **Step 1:** Download the logfile attached.
- **Step 2:** Run the script `python3 Tools/ecl_ekf/process_logdata_ekf.py <logfile>`.
- **Step 3:** Script crashes without creating any output.

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** N/A
- **Behavior after step 3:** Script exits with an exception about 'reject_mag_x'.

**Expected behavior:**

- **Expected behavior 1:** Plots and metadata to be generated according to the documentation.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Modified the script to print out the exception stack trace.
- **URL of the flight log provided by the user:** [Log file](https://logs.px4.io/plot_app?log=eb988feb-08ae-4957-89a9-2257532c0916)

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** `duckythescientist` suggested the issue might be due to a change in the logging format and recommended changing references from `reject_mag_*` to `fs_bad_mag_*` under `Tools/ecl_ekf`.
- **Result of the operation after the user adopted suggestion 1:** The user `tylertian123` reported being able to proceed with the analysis after making the suggested changes.
- **Suggestion 2 provided by developers or other personnel:** `bresch` acknowledged the oversight and requested a pull request (PR) with the changes suggested by `duckythescientist`.

