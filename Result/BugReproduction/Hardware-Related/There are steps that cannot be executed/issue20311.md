# Basic Information:
### Title:  px_uploader.py does not use monotonic clocks #20311 
### Issue status: Closed
### Author: fkaiser
### Issue open time: Sep 27, 2022
### Fixed by: #20352

# Report
### Report author: fkaiser
### Report Time: Sep 27, 2022
### Report Content:   
**Describe the bug**  
The `px_uploader.py` script used for flashing PX4 boards sometimes times out during the erasing phase if the system clock is updated (e.g., due to network synchronization) while flashing. This happens because the script uses the `time()` function to compute the timeout, which is affected by system clock changes.  

It is suggested to use the monotonic clock from Python’s `time` module, as recommended by [PEP 418](https://peps.python.org/pep-0418/), to avoid this issue. However, the monotonic clock is only reliably available as of Python 3.5.

**Steps to reproduce:**  
To reproduce the issue, adjust the system clock during the flashing process as follows (ensure proper caution is taken):  

1. Build the code:  
   ```bash
   make <target>.px4
   ```
2. Check the current time:  
   ```bash
   timedatectl
   ```
3. Disable automatic time synchronization (re-enable it after testing):  
   ```bash
   sudo timedatectl set-ntp 0
   ```
4. Start the flashing process:  
   ```bash
   python3 px_uploader.py --port <target port> --baud-bootloader <target baudrate> <target>.px4
   ```
5. During the erasing step of flashing, manually change the system time:  
   ```bash
   sudo timedatectl set-time 2022-12-05
   ```
6. Observe the timeout error during flashing.

**Expected behavior:**  
The flashing process should complete successfully without being affected by changes in the system clock.

**Log Files and Screenshots:**  
Not provided.

---

# Environment where the bug occurred:
- **Hardware environment:** Not explicitly mentioned.<font color='red'>实际需要飞控板</font>
- **Software environment:** Python 3.x (minimum version 3.3; monotonic clock fully supported from version 3.5).
- **Report Time:** Sep 27, 2022.
- **PX4 Autopilot commit version:** Not mentioned.
- **last commit before the reporting time:**70d73c8

---

# Steps for bug reproduction:
- **Step 1:** Build the PX4 firmware using `make <target>.px4`.
- **Step 2:** Check the current system time using `timedatectl`.
- **Step 3:** Disable automatic time synchronization using `sudo timedatectl set-ntp 0`.
- **Step 4:** Start the flashing process with the `px_uploader.py` script.<font color='red'>执行时出错找不到端口</font>
- **Step 5:** Change the system clock during the erasing phase using `sudo timedatectl set-time <new time>`.
- **Step 6:** Observe the timeout error.

---

# Observed behavior by the user:
- **Behavior after step 1:** N/A
- **Behavior after step 2:** System time displayed as expected.
- **Behavior after step 3:** Automatic time synchronization disabled successfully.
- **Behavior after step 4:** Flashing process starts normally.
- **Behavior after step 5:** Timeout error occurs when the system clock is updated during the erasing phase.

---

# Expected behavior:
- **Expected behavior 1:** The flashing process should not time out or fail due to system clock updates.
- **Expected behavior 2:** The script should use a monotonic clock for timeout calculations to ensure robustness.

---

# Additional information provided by the user for bug investigation:
- **Actions taken by the user:** Suggested using Python’s monotonic clock and provided steps to reproduce the issue.
- **URL of the flight log provided by the user:** Not provided.

---

# Communication between developers or other personnel and the user:

### Comment 1:
- **Author:** dagar  
- **Time:** Sep 27, 2022  
- **Content:** Suggested updating the script to use Python’s monotonic clock and opening a pull request.

### Comment 2:
- **Author:** fkaiser  
- **Time:** Oct 4, 2022  
- **Content:** Confirmed that the pull request to fix the issue was created (#20352).

### Comment 3:
- **Author:** junwoo091400  
- **Time:** Oct 6, 2022  
- **Content:** Acknowledged the issue and expressed thanks for the report, with plans to comment on the pull request.

---
