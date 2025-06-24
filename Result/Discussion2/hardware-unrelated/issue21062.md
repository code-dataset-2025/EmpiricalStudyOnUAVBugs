**Environment where the bug occurred:**

- **Hardware environment:** Not explicitly mentioned
- **Software environment:** Not explicitly mentioned
- **Report Time:** Feb 4, 2023
- **PX4 Autopilot commit version:** Not mentioned
- **last commit before the reporting time:**e153d1d

**Steps for bug reproduction:**

- **Step 1:** Right-click in the VSCode terminal.
- **Step 2:** Text from the clipboard is pasted.

**Observed behavior by the user:**

- **Behavior after step 1:** The context menu intended by the user doesn't open.<font color='red'>实际上不是项目的bug，这个提交里面没有这个设置，但存在vscode的设置文件</font>
- **Behavior after step 2:** Text from the clipboard is pasted into the terminal instead.

**Expected behavior:**

- **Expected behavior 1:** By default, a context menu should open when right-clicking.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Described the specific cause by referring to the setting `"terminal.integrated.rightClickBehavior": "paste"` in `.vscode/settings.json`.
- **URL of the flight log provided by the user:** Not applicable.

**Communication between developers or other personnel and the user:**

- No specific communication details provided.
