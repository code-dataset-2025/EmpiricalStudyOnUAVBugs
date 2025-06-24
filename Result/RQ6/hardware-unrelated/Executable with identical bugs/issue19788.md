**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned
- **Software environment:** PX4 Autopilot with usage of valgrind and SITL simulator.
- **Report Time:** Jun 9, 2022
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**46c9d1e

**Steps for bug reproduction:**

- **Step 1:** Add the following code into any module's main loop:
  ```c
  int a[3];        
  int i=10;        
  a[i] = 5;        
  a[i]--;        
  printf("%d\n",a[i]);
  ```
- **Step 2:** Run the modified code with valgrind to detect memory access violations.

**Observed behavior by the user:**
- **Behavior after step 1:** N/A
- **Behavior after step 2:** Valgrind does not report any memory access violation error.

**Expected behavior:**
- **Expected behavior 1:** Valgrind should detect a memory access violation type error when accessing out of bounds array indices.

**Additional information provided by the user for bug investigation:**
- **Actions taken by the user:** The user attempted to use valgrind to identify a memory access violation.
- **URL of the flight log provided by the user:** Not provided.

**Communication between developers or other personnel and the user:**
- **Suggestion 1 provided by developers or other personnel:** The report author, `acf986`, mentioned that valgrind cannot check stack arrays.
- **Result of the operation after the user adopted suggestion 1:** Acknowledged the limitation of valgrind in detecting such errors for stack arrays, as the issue was closed shortly after filing.<font color='red'>作者发现这不是一个bug</font>>
