**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned
- **Software environment:** PX4 Autopilot
- **Report Time:** Nov 8, 2017
- **PX4 Autopilot commit version:** v1.6.5-1632-gcf7140526

**Steps for bug reproduction:**

- **Step 1:** Run the command `mkdir -p tmp/repo`.
- **Step 2:** Navigate into the directory using `cd tmp/repo`.
- **Step 3:** Initialize a git repository with `git init`.
- **Step 4:** Add PX4/Firmware as a submodule using `git submodule add https://github.com/PX4/Firmware`.
- **Step 5:** Commit the changes using `git commit -am "Added submodule"`.
- **Step 6:** Change directory into Firmware using `cd Firmware`.
- **Step 7:** Update the submodule recursively using `git submodule update --init --recursive`.
- **Step 8:** Attempt to build using `make`.

**Observed behavior by the user:**

- **Behavior after step 1:** Directory created.
- **Behavior after step 2:** User is inside the `tmp/repo` directory.
- **Behavior after step 3:** Git repository initialized.
- **Behavior after step 4:** Submodule added to the repository.
- **Behavior after step 5:** Changes committed successfully.
- **Behavior after step 6:** Change directory to Firmware folder.
- **Behavior after step 7:** Submodules updated recursively.
- **Behavior after step 8:** Error encountered during build. Specific error: 
  ```
  CMake Error at src/lib/version/CMakeLists.txt:50 (message):      
  /home/jlecoeur/tmp/repo/Firmware/src/lib/.git/modules/Firmware is not a directory
  ```

**Expected behavior:**

- **Expected behavior 1:** Successful build of the PX4 Autopilot firmware when it's added as a submodule.
- **Expected behavior 2:** No CMake errors during the build process.
- **Expected behavior 3:** Directory structure set up correctly after updating submodules.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Described the issue, provided reproduction steps, and mentioned that the build works if cloned separately.
- **URL of the flight log provided by the user:** Not provided.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Acknowledgment of the issue, with a suggestion to add a check to CI once resolved.
- **Result of the operation after the user adopted suggestion 1:** N/A (The suggestion was more of a future action to prevent similar issues).
  
- **Suggestion 2 provided by developers or other personnel:** "Fixed in #8334" indicating that the issue was resolved.
- **Result of the operation after the user adopted suggestion 2:** Presumably positive as the issue was marked closed, but not explicitly documented in the comments.
