# Basic Information:
### Title:  CMake build error corner case #8828 
### Issue status: Closed
### Author: RomanBapst
### Issue open time: Feb 5, 2018
### Fixed by: #8829
# Report
### Report author: RomanBapst
### Report Time: Feb 5, 2018
### Report Content:   
@dagar FYI    
How to reproduce:  
1.Try to build PX4 without having the arm compiler installed  
2.Install arm compiler  
3.Try to build PX4 (without doing a 'make distclean')  
If no 'make distclean' after the compiler installation is executed you get the following error.  
Console output:  
    
```bash     
 make px4fmu-v5_default upload        
-- Build Type: MinSizeRel        
-- PX4 VERSION: v1.7.3-296-g26f9e56        
-- CONFIG: nuttx_px4fmu-v5_default        
-- Build Type: MinSizeRel        
-- The ASM compiler identification is GNU        
-- Found assembler: /home/roman/gcc-arm-none-eabi-5_4-2016q2/bin/arm-none-eabi-gcc        
-- Found PythonInterp: /usr/bin/python (found version "2.7.12")         
-- Found PY_jinja2: /usr/local/lib/python2.7/dist-packages/jinja2          
-- C compiler: arm-none-eabi-gcc (GNU Tools for ARM Embedded Processors) 5.4.1 20160609 (release) [ARM/embedded-5-branch revision 237715]        
-- C++ compiler: arm-none-eabi-g++ (GNU Tools for ARM Embedded Processors) 5.4.1 20160609 (release) [ARM/embedded-5-branch revision 237715]        
-- Building and including px4io-v2        
-- Using C++03        
-- Release build type: MinSizeRel        
-- Adding UAVCAN STM32 platform driver        
-- NuttX: px4fmu-v5 nsh cortex-m7        
-- ROMFS: px4fmu_common        
-- Configuring done        
-- Generating done        
-- Build files have been written to: /home/roman/drones/Firmware/build/px4fmu-v5_default        
[5/906] Building px4io-v2        
-- Build Type: MinSizeRel        
-- PX4 VERSION: v1.7.3-296-g26f9e56        
-- CONFIG: nuttx_px4io-v2_default        
-- Build Type: MinSizeRel        
-- The ASM compiler identification is GNU        
-- Found assembler: /home/roman/gcc-arm-none-eabi-5_4-2016q2/bin/arm-none-eabi-gcc        
-- Found PythonInterp: /usr/bin/python (found version "2.7.12")         
-- Found PY_jinja2: /usr/local/lib/python2.7/dist-packages/jinja2          
-- C compiler: arm-none-eabi-gcc (GNU Tools for ARM Embedded Processors) 5.4.1 20160609 (release) [ARM/embedded-5-branch revision 237715]        
-- C++ compiler: arm-none-eabi-g++ (GNU Tools for ARM Embedded Processors) 5.4.1 20160609 (release) [ARM/embedded-5-branch revision 237715]        
-- NuttX: px4io-v2 nsh cortex-m3        
-- Configuring done        
-- Generating done        
-- Build files have been written to: /home/roman/drones/Firmware/build/px4io-v2_default        
[157/157] Linking CXX executable nuttx_px4io-v2_default.elf        
[11/906] Running dsdl compiler        
FAILED: cd /home/roman/drones/Firmware/src/modules/uavcan/libuavcan/libuavcan && /usr/bin/python /home/roman/drones/Firmware/src/modules/uavcan/libuavcan/libuavcan/dsdl_compiler/libuavcan_dsdlc test/dsdl_test/root_ns_a test/dsdl_test/root_ns_b /home/roman/drones/Firmware/src/modules/uavcan/libuavcan/libuavcan/../dsdl/uavcan -Oinclude/dsdlc_generated && /usr/bin/cmake -E touch /home/roman/drones/Firmware/build/px4fmu-v5_default/libuavcan_dsdlc_run.stamp        
Traceback (most recent call last):        
  File "/home/roman/drones/Firmware/src/modules/uavcan/libuavcan/libuavcan/dsdl_compiler/libuavcan_dsdlc", line 59, in <module>        
    from libuavcan_dsdl_compiler import run as dsdlc_run        
  File "/home/roman/drones/Firmware/src/modules/uavcan/libuavcan/libuavcan/dsdl_compiler/libuavcan_dsdl_compiler/__init__.py", line 17, in <module>        
    from uavcan import dsdl        
ImportError: No module named uavcan        
[11/906] Generating parameters.xml        
ninja: build stopped: subcommand failed.        
Makefile:153: recipe for target 'px4fmu-v5_default' failed        
make: *** [px4fmu-v5_default] Error 1        
```  

# Comment
## Comment1
### Comment author: dagar
### Comment Time: Feb 5, 2018
### Comment Content:   
It looks like we're missing a few dependencies at the UAVCAN level.  
