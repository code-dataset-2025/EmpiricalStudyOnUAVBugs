**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned
- **Software environment:** Ubuntu 18.04 with Gazebo 9
- **Report Time:** Dec 31, 2018
- **PX4 Autopilot commit version:** Not explicitly mentioned
- **last commit before the reporting time:**29bfdb0

**Steps for bug reproduction:**

- **Step 1:** Clone the upstream master branch.
- **Step 2:** Issue the command `make px4_sitl_rtps gazebo`.<font color='red'>编译出错，安装fastrtps后仍出错报错信息指向对pthread_create等未定义的引用，可能是不同库间的版本问题</font>
- **Step 3:** Observe the output on the nsh console.

**Observed behavior by the user:**

- **Behavior after step 1:** N/A
- **Behavior after step 2:** N/A
- **Behavior after step 3:** The nsh console displays repetitive warning messages indicating connection timeouts and semaphores errors.

**Expected behavior:**

- **Expected behavior 1:** A clean console output without repeated warnings.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** The user suspected recent changes in SITL and lockstep feature might have caused the issue and sought guidance from other developers on what might be causing the issue.
- **URL of the flight log provided by the user:** Not provided.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Developer `julianoes` pointed out two oddities about the timeout and unclear error message.
- **Result of the operation after the user adopted suggestion 1:** Not explicitly mentioned, the discussion continued around finding the cause.
  
- **Suggestion 2 provided by developers or other personnel:** Developer `LorenzMeier` mentioned that the issue involved handling of ETIMEDOUT and suggested checking for sign errors. He also worked on a patch.
- **Result of the operation after the user adopted suggestion 2:** A potential fix was identified, and a specific commit (98ae018) was suggested to be the problem. A patch (#11122) was created to address it.

- **Suggestion 3 provided by developers or other personnel:** `julianoes` suggested specific changes to the cmake file and highlighted related compile errors needing fixes.
- **Result of the operation after the user adopted suggestion 3:** It seems proactive investigations and fixes were proposed, though the final confirmation of the resolution was not provided in the comments.
