# Basic Information:
### Title: Ubuntu toolchain setup script fails #14888 
### Issue status: Closed
### Author: dfarnainekl
### Issue open time: May 11, 2020
### Fixed by: #14922

# Report
### Report author: dfarnainekl
### Report Time: May 11, 2020
### Report Content:  
**Describe the bug**  
When running the Ubuntu setup script (`Tools/setup/ubuntu.sh`) on Ubuntu 20.04, the script stops running at this line:  
[Tools/setup/ubuntu.sh#L144](https://github.com/PX4/Firmware/blob/0a4e7142ee7baa14cc50ea86d5a13b1933d5d5e4/Tools/setup/ubuntu.sh#L144).  

**To Reproduce**  
1. Run the `ubuntu.sh` script on Ubuntu 20.04.  
2. After installing the NuttX dependencies, the script stops.  
3. Modify the line linked above by replacing it with `GCC_FOUND_VER=0`.  
4. The installation continues as expected.  

---

**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned
- **Software environment:** Ubuntu 20.04 with `bash` version 5.0.16(1)-release
- **Report Time:** May 11, 2020
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**c07b687

**Steps for bug reproduction:**

- **Step 1:** Run the Ubuntu setup script (`Tools/setup/ubuntu.sh`) on Ubuntu 20.04.  
- **Step 2:** Observe the script stopping at the line linked in the report.  <font color='red'>使用该提交没有停在这一行</font>
- **Step 3:** Replace the line in question with `GCC_FOUND_VER=0`.  
- **Step 4:** Run the script again, and the installation continues as expected.  

**Observed behavior by the user:**
- **Behavior after step 1:** Script stops running after installing NuttX dependencies.  
- **Behavior after step 2:** Same issue occurs as described.  
- **Behavior after step 3:** With the modification, the installation proceeds without issue.  

**Expected behavior:**
- **Expected behavior 1:** The script should complete the installation without requiring manual modification.  

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:**  
  - Modified the script line causing the issue by replacing it with `GCC_FOUND_VER=0`.  
  - Reported using a fresh download of the repository and verified their `bash` version (`5.0.16(1)-release`).  

---

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:**  
  Developer `julianoes` asked the user to check again (May 14, 2020).  

  - **Result of the operation after the user adopted suggestion 1:**  
    The user reported a new error: `./ubuntu.sh: line 149: [: missing ']` (May 15, 2020). The toolchain installation proceeded even when it was already installed.  

- **Suggestion 2 provided by developers or other personnel:**  
  Developer `julianoes` asked the user how they downloaded the `ubuntu.sh` file and suggested using the one from the repository (May 15, 2020).  

  - **Result of the operation after the user adopted suggestion 2:**  
    The user confirmed they used a fresh download of the repository but suggested the issue might be related to differences in their `bash` version.  

- **Suggestion 3 provided by developers or other personnel:**  
  Developer `hamishwillee` reproduced the issue in a VM and speculated the problem was related to the Grep of the version and the addition of "+x" in the script (May 18, 2020).  

  - **Result of the operation after the user adopted suggestion 3:**  
    Developer `julianoes` confirmed they could reproduce the error after overlooking it initially (May 18, 2020).  

---

This concludes the report summary. Let me know if further breakdowns or details are needed!
