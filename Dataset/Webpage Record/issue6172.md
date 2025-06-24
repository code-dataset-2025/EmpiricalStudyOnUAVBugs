# Basic Information:
### Title:  Build broken on Ubuntu16.04 #6172 
### Issue status: Closed
### Author: iZhangHui
### Issue open time: Dec 26, 2016
# Report
### Report author: iZhangHui
### Report Time: Dec 26, 2016
### Report Content:   
make px4fmu-v4_default    
-- nuttx-px4fmu-v4-default    
-- CMAKE_INSTALL_PREFIX:    
-- cmake module path: /home/henry/Dev/px4/cmake    
-- Nuttx build for px4fmu-v4 on m4 hardware, using nsh with ROMFS on px4fmu_common    
-- The ASM compiler identification is GNU    
-- Found assembler: /usr/bin/arm-none-eabi-gcc    
-- Found PythonInterp: /usr/bin/python (found version "2.7.12")    
-- NuttX patch: nuttx-patches/ctype_cctype_.patch    
-- NuttX patch: nuttx-patches/export_insitu.patch    
-- NuttX patch: nuttx-patches/nsh_parse.patch    
-- NuttX patch: nuttx-patches/fixStdint.patch    
-- NuttX patch: nuttx-patches/wip_inflight_to_upstream.patch    
-- NuttX patch: nuttx-patches/static_asset-fix.patch    
-- NuttX patch: nuttx-patches/math.h.patch    
-- NuttX patch: nuttx-patches/silence-jobserver-warnings.patch    
-- NuttX patch: nuttx-patches/serial_dma_hotfix.patch    
-- NuttX patch: nuttx-patches/Fixed-Shadow-wanings.patch    
-- NuttX patch: nuttx-patches/c++11.patch    
-- Using C++03    
-- Release build type: RelWithDebInfo    
-- Adding UAVCAN STM32 platform driver    
-- Adding ROMFS on px4fmu-v4    
-- Configuring done    
-- Generating done    
-- Build files have been written to: /home/henry/Dev/px4/build_px4fmu-v4_default    
PX4 CONFIG: /home/henry/Dev/px4/build_px4fmu-v4_default    
Scanning dependencies of target git_genmsg    
Scanning dependencies of target ver_gen    
Scanning dependencies of target git_nuttx    
Scanning dependencies of target git_gencpp    
[  0%] Generating git_init_Tools_genmsg.stamp    
[  0%] Generating git hash header    
[  1%] Generating git_init_NuttX.stamp    
[  1%] Generating git_init_Tools_gencpp.stamp    
[  1%] Built target git_genmsg    
[  1%] Built target git_nuttx    
[  1%] Built target git_gencpp    
Scanning dependencies of target git_matrix    
Scanning dependencies of target git_mavlink    
Scanning dependencies of target git_uavcan    
[  1%] Generating git_init_src_lib_matrix.stamp    
Updating header /home/henry/Dev/px4/build_px4fmu-v4_default/build_git_version.h    
[  1%] Built target git_matrix    
[  1%] Generating git_init_mavlink_include_mavlink_v1.0.stamp    
[  1%] Built target ver_gen    
[  2%] Generating git_init_src_modules_uavcan_libuavcan.stamp    
[  2%] Built target git_mavlink    
[  2%] Generating romfs.o    
[  2%] Built target git_uavcan    
Scanning dependencies of target libuavcan_dsdlc    
Scanning dependencies of target git_ecl    
Scanning dependencies of target xml_gen    
[  2%] Running dsdl compiler    
[  2%] Generating git_init_src_lib_ecl.stamp    
[  2%] Generating parameters.xml    
[  2%] Built target git_ecl    
[  3%] Generating airframes.xml    
Scanning dependencies of target mixer_gen    
[  4%] Generating mixer_multirotor.generated.h    
[  4%] Built target mixer_gen    
Traceback (most recent call last):    
File "/home/henry/Dev/px4/cmake/nuttx/bin_to_obj.py", line 56, in     
locals())    
File "/home/henry/Dev/px4/cmake/nuttx/bin_to_obj.py", line 47, in run_cmd    
raise RuntimeError(stderr)    
RuntimeError: /usr/bin/arm-none-eabi-ld: romfs.bin: not in ELF format  
src/firmware/nuttx/CMakeFiles/romfs.dir/build.make:192: recipe for target 'src/firmware/nuttx/romfs.o' failed    
make[3]: *** [src/firmware/nuttx/romfs.o] Error 1    
CMakeFiles/Makefile2:7407: recipe for target 'src/firmware/nuttx/CMakeFiles/romfs.dir/all' failed    
make[2]: *** [src/firmware/nuttx/CMakeFiles/romfs.dir/all] Error 2    
make[2]: *** Waiting for unfinished jobs....    
[  4%] Built target libuavcan_dsdlc    
Scanning dependencies of target nuttx_patch_fixStdint.patch-px4fmu-v4    
[  4%] Copying NuttX for px4fmu-v4 with nsh    
[  5%] Applying /home/henry/Dev/px4/nuttx-patches/fixStdint.patch    
[  5%] Built target nuttx_patch_fixStdint.patch-px4fmu-v4    
[  5%] Built target xml_gen    
Makefile:160: recipe for target 'all' failed    
make[1]: *** [all] Error 2    
Makefile:174: recipe for target 'px4fmu-v4_default' failed    
make: *** [px4fmu-v4_default] Error 2  

# Comment
## Comment1
### Comment author: LorenzMeier
### Comment Time: Dec 26, 2016
### Comment Content:   
@dagar Do you have time to have a look? We get lots of build issue reports  

## Comment2
### Comment author: jgoppert
### Comment Time: Dec 26, 2016
### Comment Content:   
I can reproduce, @davids5 any ideas?  
    
```bash     
 ~/git/px4/src/px4/build_px4fmu-v4_default/src/firmware/nuttx$ file romfs.bin romfs.bin: romfs filesystem, version 1 74912 bytes, named NSHInitVol.    
```  

## Comment3
### Comment author: LorenzMeier
### Comment Time: Dec 28, 2016
### Comment Content:   
Fixed.  

## Comment4
### Comment author: iZhangHui
### Comment Time: Dec 29, 2016
### Comment Content:   
Try to build the latest master, it still failed.    
Ubuntu 16.04 auto update GCC version to 6.x.  
arm-none-eabi-gcc --version    
arm-none-eabi-gcc (GNU Tools for ARM Embedded Processors) 6.2.1 20161205 (release) [ARM/embedded-6-branch revision 243739]    
Copyright (C) 2016 Free Software Foundation, Inc.    
This is free software; see the source for copying conditions.  There is NO    
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  

## Comment5
### Comment author: kd0aij
### Comment Time: Dec 29, 2016
## Comment6
### Comment author: iZhangHui
### Comment Time: Dec 29, 2016
### Comment Content:   
Follow the link below:    
http://dev.px4.io/starting-installing-linux.html  
