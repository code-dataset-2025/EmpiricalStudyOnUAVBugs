Here is the structured bug report based on the provided information:

---

# Basic Information:
### Title:  mavlink - reading to undefined memory  #12900 
### Issue status: Closed
### Author: BazookaJoe1900
### Issue open time: Sep 4, 2019
### Fixed by: Not explicitly mentioned

# Report
### Report author: BazookaJoe1900
### Report Time: Sep 4, 2019
### Report Content:   
First, I am not sure if this bug should be here or in mavlink.... I write it here, but it can be moved.    
I am not 100% sure about if my assumption is right.  
**Describe the bug:**    
I played with @julianoes PR (posix: add fuzz testing using MAVLink messages #12896) and think that I might have encountered a critical bug in `mavlink_helper.h`, line 502  
[Reference Code](https://github.com/mavlink/c_library_v2/blob/d5d131cf710ceaa93d26884ea12de8de95804985/mavlink_helpers.h#L501)  

When the fuzz sends a `msgid` that is higher than the maximum message ID in the `mavlink_message_crcs[mid].msgid` table, the `mid` parameter can access an undefined address due to exceeding the bounds of the array.  

**Code causing the issue:**  
```cpp
high = sizeof(mavlink_message_crcs) / sizeof(mavlink_message_crcs[0])
```

**Proposed fix:**  
```cpp
high = sizeof(mavlink_message_crcs) / sizeof(mavlink_message_crcs[0]) - 1
```

This table demonstrates how `low`, `high`, and `mid` values iterate when the `msgid` is higher than the highest ID in the table (assuming the number of messages is 186):  

| **low** | **high** | **mid** |  
|---------|----------|---------|  
| 0       | 186      | 93      |  
| 93      | 186      | 140     |  
| 140     | 186      | 163     |  
| 163     | 186      | 175     |  
| 175     | 186      | 181     |  
| 181     | 186      | 184     |  
| 184     | 186      | 185     |  
| 185     | 186      | 186 -> Error (calls `mavlink_message_crcs[186].msgid`) |  

**To Reproduce:**  
1. Run `posix: add fuzz testing using MAVLink messages #12896`.  

---

**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned
- **Software environment:** Not explicitly mentioned
- **Report Time:** Sep 4, 2019
- **PX4 Autopilot commit version:** Not mentioned  
- **last commit before the reporting time:**c8d13ba

---

**Steps for bug reproduction:**

- **Step 1:** Run `posix: add fuzz testing using MAVLink messages #12896`.<font color='red'>这一步在原文中指向一个pull，执行完pull中的命令报错fatal error: implicit conversion from 'int' to 'float' changes value from 2147483647 to 2147483648 [-Wimplicit-int-float-conversion]</font>
- **Step 2:** Send a `msgid` higher than the maximum message ID in `mavlink_message_crcs[mid].msgid` table.
- **Step 3:** Observe memory access error when `mid` exceeds bounds.

---

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** N/A
- **Behavior after step 3:** Access to undefined memory location leading to potential crash or undefined behavior.

---

**Expected behavior:**

- **Expected behavior 1:** The program should handle `msgid` values higher than the maximum message ID gracefully, without accessing undefined memory.
- **Expected behavior 2:** No crashes or undefined behavior should occur.

---

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Identified the root cause and provided a proposed fix.
- **URL of the flight log provided by the user:** Not provided.

---

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** @julianoes suggested patching the issue and referenced a related patch: [pymavlink PR #343](https://github.com/ArduPilot/pymavlink/pull/343/files).
  - **Result of the operation after the user adopted suggestion 1:** Fix was merged in Mavlink (as per user feedback).
- **Suggestion 2 provided by developers or other personnel:** @julianoes mentioned that the `c_library_v2` submodule still needed an update.
  - **Result of the operation after the user adopted suggestion 2:** Not explicitly mentioned; discussion continued about whether the process was automated.
- **Suggestion 3 provided by developers or other personnel:** @julianoes pointed to a bot-created branch (#12998) for submodule updates.
  - **Result of the operation after the user adopted suggestion 3:** Not applicable, as it was handled automatically by the bot.

---

This bug report summarizes the issue, provides reproduction steps, expected and observed behaviors, and captures the discussion around the resolution.
