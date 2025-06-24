# Basic Information:
### Title:  make tests fails after first time #9025 
### Issue status: Closed
### Author: julianoes
### Issue open time: Mar 5, 2018
# Report
### Report author: julianoes
### Report Time: Mar 5, 2018
### Report Content:   
The tests which can be run in docker seem to pass the very first time but fail afterwards.  
This can be reproduced by doing:  
    
```bash     
 ./Tools/docker_run.sh "make tests"        
```  
The first time, the tests pass but the second time something fails together with a printf from mavlink:  
    
```bash     
 ./Tools/docker_run.sh "make tests"        
guessing PX4_DOCKER_REPO based on input        
PX4_DOCKER_REPO: px4io/px4-dev-simulation:2017-12-30        
Starting with UID : 1000        
[1/1] Running tests in sitl        
Site: 4d76d755de95        
Build name: Linux-c++        
Test project /home/julianoes/src/Firmware/build/posix_sitl_default        
Start 1: autodeclination        
1/31 Test \\\\#1: autodeclination .................. Passed 0.48 sec        
Start 2: bson        
2/31 Test \\\\#2: bson ............................. Passed 0.49 sec        
Start 3: commander        
3/31 Test \\\\#3: commander ........................ Passed 0.44 sec        
Start 4: controllib        
4/31 Test \\\\#4: controllib .......................***Failed Error regular expression found in output. Regex=[controllib FAILED] 0.46 sec        
args: /home/julianoes/src/Firmware/build/posix_sitl_default/px4 posix-configs/SITL/init/test none none tests_controllib_generated /home/julianoes/src/Firmware /home/julianoes/src/Firmware/build/posix_sitl_default        
SITL ARGS        
sitl_bin: /home/julianoes/src/Firmware/build/posix_sitl_default/px4        
rcS_dir: posix-configs/SITL/init/test        
debugger: none        
program: none        
model: tests_controllib_generated        
src_path: /home/julianoes/src/Firmware        
build_path: /home/julianoes/src/Firmware/build/posix_sitl_default        
SITL COMMAND: /home/julianoes/src/Firmware/build/posix_sitl_default/px4 /home/julianoes/src/Firmware /home/julianoes/src/Firmware/posix-configs/SITL/init/test/tests_controllib_generated        
data path: /home/julianoes/src/Firmware        
commands file: /home/julianoes/src/Firmware/posix-configs/SITL/init/test/tests_controllib_generated        
161 WARNING: setRealtimeSched failed (not run as root?)        
______ __ __ ___        
| ___ \ \ \ / / / |        
| |_/ / \ V / / /| |        
| __/ / \ / /_| |        
| | / /^\ \ \___ |        
\_| \/ \/ |_/        
px4 starting.        
INFO [pwm_out_sim] MODE_16PWM        
HW arch: SITL        
FW git-hash: 03b8cd78b3e32be581f5e9ecf22358da03b3fe91        
FW version: 1.7.3 0 (17236736)        
OS: Linux        
OS version: Release 4.15.6 (68093695)        
Build datetime: Mar 5 2018 17:28:42        
Build uri: localhost        
Toolchain: GNU GCC, 5.4.0 20160609        
MFGUID: SIMULATIONID        
UNKNOWN MCU        
UID: SIMULATIONID        
INFO [platforms__posix__px4_layer] Active Tasks:        
INFO [platforms__posix__px4_layer] hpwork 139763141170944        
INFO [platforms__posix__px4_layer] lpwork 139763132778240        
INFO [platforms__posix__px4_layer] wkr_hrt 139763124385536        
INFO [platforms__posix__px4_layer] dataman 139763115992832        
INFO [platforms__posix__px4_layer] gps 139763099207424        
INFO [platforms__posix__px4_layer] pwmsim 139763090814720        
INFO [drivers__device] PX4 Devices:        
INFO [drivers__device] /dev/airspeed0        
INFO [drivers__device] /dev/ms4525        
INFO [drivers__device] /dev/pwm_output0        
INFO [drivers__device] DF Devices:        
INFO [drivers__device] /dev/led0        
INFO [drivers__device] (null)        
INFO [drivers__device] /dev/accel0        
INFO [drivers__device] /dev/gyro0        
INFO [drivers__device] /dev/accel1        
INFO [drivers__device] /dev/mag0        
INFO [drivers__device] /dev/baro0        
INFO [drivers__device] /dev/adc0        
INFO [drivers__device] (null)        
INFO [drivers__device] Devices:        
INFO [drivers__device] /obj/_obj_        
INFO [drivers__device] /obj/actuator_armed0        
INFO [drivers__device] /obj/actuator_outputs0        
INFO [drivers__device] /obj/differential_pressure0        
INFO [drivers__device] /obj/log_message0        
INFO [drivers__device] /obj/parameter_update0        
INFO [drivers__device] /obj/sensor_accel0        
INFO [drivers__device] /obj/sensor_accel1        
INFO [drivers__device] /obj/sensor_baro0        
INFO [drivers__device] /obj/sensor_gyro0        
INFO [drivers__device] /obj/sensor_mag0        
INFO [drivers__device] Files:        
INFO [mavlink] mode: Normal, data rate: 2000000 B/s on udp port 14556 remote port 14550        
Test BlockLimit : not equal ->        
a: 1.00000000        
b: 1015.21783447        
FAIL        
controllib FAILED        
Command 'tests' failed, returned -1        
INFO [dataman] Writes 0        
INFO [dataman] Reads 3        
INFO [dataman] Clears 0        
INFO [dataman] Restarts 0        
INFO [dataman] Max Q lengths work 1, free 8        
Shutting down        
Restoring terminal        
Start 5: conv        
5/31 Test \\\\#5: conv ............................. Passed 0.39 sec        
Start 6: dataman        
^CThe futex facility returned an unexpected error code.ninja: build stopped: interrupted by user.        
Makefile:147: recipe for target 'posix_sitl_default' failed        
make[1]: *** [posix_sitl_default] Interrupt        
Makefile:285: recipe for target 'tests' failed        
make: *** [tests] Interrupt        
make: *** wait: No child processes. Stop.        
```  
Depending on timing different tests can fail.  

# Comment
## Comment1
### Comment author: julianoes
### Comment Time: Mar 5, 2018
### Comment Content:   
Running make clean in-between test runs resolves the issue.  

## Comment2
### Comment author: dagar
### Comment Time: Mar 5, 2018
### Comment Content:   
On SITL the parameters test sets all parameters. https://github.com/PX4/Firmware/blob/master/src/systemcmds/tests/test_parameters.cpp\\\#L310  
After the test it's supposed to restore them to the previous state. Apparently that's not working?  

## Comment3
### Comment author: dagar
### Comment Time: Mar 5, 2018
### Comment Content:   
I'll dig into this and find the core problem.  

## Comment4
### Comment author: julianoes
### Comment Time: Mar 6, 2018
### Comment Content:   
@dagar this resolves the issue:  
    
```bash     
 rm -rf build/posix_sitl_default/tmp        
mkdir build/posix_sitl_default/tmp        
```  
Where would this need to happen in docker, make, cmake?  

## Comment5
### Comment author: julianoes
### Comment Time: Dec 12, 2018
### Comment Content:   
This is not just a docker issue but happens in general.  

## Comment6
### Comment author: dagar
### Comment Time: Dec 12, 2018
### Comment Content:   
Previously this was failing due to the parameters test not restoring the original parameters when finished. I fixed that a few months ago (ad321c8\\\#diff-2b2e4dae7339cf761a31d79df78dee31).  
What failure are you seeing now?  

## Comment7
### Comment author: julianoes
### Comment Time: Dec 12, 2018
### Comment Content:   
You're right, this might have been just a fluke on Windows. Thanks for following up.  
