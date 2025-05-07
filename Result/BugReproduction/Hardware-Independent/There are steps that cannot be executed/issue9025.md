**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned
- **Software environment:** PX4 Autopilot
- **Report time:** Mar 5, 2018
- **PX4 Autopilot commit version:** not mentioned
- **last commit before the reporting time:**5de5d6e

**Steps for bug reproduction:**

- **Step 1:** Run the command `./Tools/docker_run.sh "make tests"` in Docker.<font color='red'>拉取被拒绝，docker镜像可能已经不存在</font>
- **Step 2:** Observe test results.

**Observed behavior by the user:**

- **Behavior after step 1:** Tests pass on the first run.
- **Behavior after step 2:** On subsequent runs, tests fail, particularly the "controllib" test with an error message indicating "controllib FAILED." The MAVLink layer outputs unexpected messages.

**Expected behavior:**

- **Expected behavior 1:** Tests should consistently pass on each run without failure.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** The user noted that running `make clean` between test runs resolves the issue. Additionally, a temporary solution involving removing and recreating the `tmp` directory was mentioned.

**Communication between developers or other personnel and the user:**
- **Suggestion 1 provided by developers or other personnel:** Developer `dagar` suggested that the problem could be related to the test parameters not being restored to their original state after testing.
- **Result of the operation after the user adopted suggestion 1:** The issue was temporarily resolved by cleaning the build or removing the temporary directory before subsequent test runs.
- **Suggestion 2 provided by developers or other personnel:** `dagar` later mentioned fixing the issue related to parameters not being restored in a subsequent commit.
- **Result of the operation after the user adopted suggestion 2:** Subsequent tests did not fail due to this issue, though a new failure was noted on Windows, which was later attributed to a fluke.
