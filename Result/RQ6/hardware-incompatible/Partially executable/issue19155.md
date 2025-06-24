**Environment where the bug occurred:**

- **Hardware environment:** Matek H743 Slim board
- **Software environment:** PX4 Autopilot, Host OS: Ubuntu 20.04, x86_64
- **Report Time:** Feb 9, 2022
- **PX4 Autopilot commit version:** commit 33ce1b9

**Steps for bug reproduction:**

- **Step 1:** Build the bootloader target for the Slim using `make matek_h743-slim_bootloader`.<font color='red'>pixhawk 4(fmu_v5)没有对应的Bootloader target可以编译</font>
- **Step 2:** Put the chip in DFU mode and connect it to the host machine over USB.
- **Step 3:** Use STM32CubeProgrammer to completely erase all flash sectors of the chip.
- **Step 4:** Flash the Matek h743 Slim Bootloader to address 0x08000000.
- **Step 5:** Disconnect the USB cable.
- **Step 6:** Build the firmware target for the Slim using `make matek_h743-slim_default`.
- **Step 7:** Connect the FMU directly to the host machine via USB.
- **Step 8:** Use `Tools/px_uploader.py --port /dev/ttyACM0 build/matek_h743-slim_default/matek_h743-slim_default.px4` to flash the firmware.
- **Step 9:** Disconnect the USB cable from the FMU.
- **Step 10:** Format a fresh SD card and insert it into the FMU.
- **Step 11:** Connect the USART1 interface on the FMU to the host machine via USB FTDI adapter.
- **Step 12:** Reconnect the USB cable from the host to the FMU to power on.

**Observed behavior by the user:**

- **Behavior after step 1-11:** The firmware can write files to the SD card but cannot read files. Errors occur during the startup, such as invalid arguments when trying to read.
- **Behavior after step 12:** Commands like `cat` on SD card files result in I/O errors, whereas performing `cat` on ROMFS files works correctly.

**Expected behavior:**

- **Expected behavior 1:** Operations like `cat` should work on SD card files in `nsh`.
- **Expected behavior 2:** There should be no read/write-related errors with the SD card during boot.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Reformatted the SD card, enabled `mkfatfs` in the NSH lib config, attempted to bootstrap various clock divider configurations.
- **Communication:** Spiderkeys adjusted the SDIO clock frequency divider to stabilize performance, and performed additional testing with multiple SD cards and boards.

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** Test whether the issue is reproducible on multiple units.
- **Result of the operation after the user adopted suggestion 1:** Spiderkeys confirmed the reproducibility of the issue across multiple boards and cards.
- **Suggestion 2 provided by developers or other personnel:** Investigate a potential clock configuration issue.
- **Result of the operation after the user adopted suggestion 2:** Reducing clock speed improved performance and resolved the issue.
- **Suggestion 3 provided by developers or other personnel:** Consider creating a pull request if the change brings stability.
- **Result of the operation after the user adopted suggestion 3:** A pull request was made and merged, and the issue was resolved.

A prior incident was referenced by @spiderkeys concerning Ardupilot, reflecting similar problems in clock configuration. Subsequent testing affirmed stability post-modification.
