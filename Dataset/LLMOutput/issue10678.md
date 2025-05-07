**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned
- **Software environment:** Not explicitly mentioned
- **Report Time:** Oct 11, 2018
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**55b9f76

**Steps for bug reproduction:**

- **Step 1:** Submit a PR.<font color='red'>需要对仓库提交PR，评论中提及CI tool的错误已被修复，与项目本身无关</font>
- **Step 2:** Wait for CI tools to complete.

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** Clang Tidy failures occur in files not touched by the active PR.

**Expected behavior:**

- **Expected behavior 1:** Only files impacted by the PR should be those able to cause issues.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** The user mentioned they would do some digging into fixing the bug they filed.
- **URL of the flight log provided by the user:** Not provided.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** @dagar suggested that retrying once after a CI failure might be acceptable.
- **Result of the operation after the user adopted suggestion 1:** Not explicitly mentioned.
- **Suggestion 2 provided by developers or other personnel:** @lamping7 originally intended to close the issue as they hadn't noticed further failures, but later identified a failure in PR #10774 and asked @dagar for ideas.
- **Result of the operation after the user adopted suggestion 2:** Not explicitly mentioned, but the issue was later suggested to be closed by the original reporter, mcsauder, as they felt the CI failures had been resolved.
