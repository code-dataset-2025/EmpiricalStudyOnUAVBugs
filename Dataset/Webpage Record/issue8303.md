# Basic Information:
### Title:  FMU Input Capture crashes board #8303 
### Issue status: Closed
### Author: mhkabir
### Issue open time: Nov 17, 2017
# Report
### Report author: mhkabir
### Report Time: Nov 17, 2017
### Report Content:   
As a part of completing support for camera hardware feedback (\\\#8247), I've been resurrecting the FMU's input capture modes (mode pwm2cap2 and mode pwm3cap1). Initial testing reveals that the baseline command fmu test to verify the functionality fails, and the board crashes.  
To reproduce :  
1.Connect a digital signal to AUX4  
2.Set fmu to capture mode (fmu mode_pwm3cap1)  
3.Run fmu test  
4.Board freezes and/or reboots.  
Interestingly, nothing bad happens if there is no signal connected to the pin.  
It seems to have broken somewhere between Release v1.5.5 and v1.6.5. @davids5 Some help here would be appreciated, since I have not used the input capture functionality before and am not aware of any caveats and/or how it could have been broken.  
FYI @dagar @JonReacher  

# Comment
## Comment1
### Comment author: davids5
### Comment Time: Sep 27, 2018
### Comment Content:   
@mhkabir - what HW is this on?  
    
Connect a digital signal to AUX4    
Any frequency, a 1 or 0 or pulse width?  

## Comment2
### Comment author: mhkabir
### Comment Time: Sep 27, 2018
### Comment Content:   
This was on Pixhawk 2.1, and this was happening for "any" signal, including the 30ms active high pulses which I was testing with.  

## Comment3
### Comment author: davids5
### Comment Time: Sep 28, 2018
### Comment Content:   
@mhkabir - I Tested today's master on Pixhawk 2.1 CUBE with fmu-v3 build.  
    
```bash     
 nsh> fmu status        
INFO  [fmu] Running on work queue        
INFO  [fmu] Max update rate: 50 Hz        
INFO  [fmu] PWM Mode: pwm4cap1        
nsh> ver all        
HW arch: PX4FMU_V2        
HW type: V30        
HW version: 0x0009000E        
HW revision: 0x00000000        
FW git-hash: 066ca50ddff7d0552437ad9909b4ae04e5b0a5d9        
FW version: 1.8.0 0 (17301504)        
OS: NuttX        
OS version: Release 7.22.0 (118882559)        
OS git-hash: 7e3c8e10cd92351b905bc8d0e34e69bccd00dfea        
Build datetime: Sep 28 2018 10:37:38        
Build uri: localhost        
Toolchain: GNU GCC, 7.2.1 20170904 (release) [ARM/embedded-7-branch revision 255204]        
MFGUID: 343136303136510d002a0035        
MCU: STM32F42x, rev. 3        
UID: 2A0035:3136510D:34313630        
nsh        
```  
Not sure what your test setup was and how well you grounding was.  
But kicking it's at 400 Khz input - it runs fine. at 100 % load  
    
```bash     
  PID COMMAND                   CPU(ms) CPU(%)  USED/STACK PRIO(BASE) STATE FD        
   0 Idle Task                  280851  0.000   548/  748   0 (  0)  READY  3        
   1 hpwork                      10953  0.000   696/ 1780 249 (249)  READY  7        
   2 lpwork                       1521  0.000   872/ 1780  50 ( 50)  READY 10        
   3 init                        73360  0.000  1656/ 2484 100 (100)  w:sem  3        
 242 top                          8358 20.015  1320/ 1684 255 (255)  RUN    3        
  12 dataman                         1  0.000   792/ 1180  90 ( 90)  w:sem  4        
  86 sensors                     51199 31.339  1288/ 1964 249 (249)  READY 22        
  88 commander                    4375  0.000  1256/ 3212 140 (140)  READY 31        
  89 commander_low_prio             10  0.000   552/ 2996  50 ( 50)  READY 31        
  95 mavlink_if0                   202  0.000  1280/ 2532 100 (100)  READY  4        
 173 gps                          1063  0.000  1136/ 1548 220 (220)  READY  5        
 180 mavlink_if0                 22846  0.000  1744/ 2484 100 (100)  READY 28        
 181 mavlink_rcv_if0              1890  0.000  1576/ 2836 175 (175)  READY 28        
 200 ekf2                        82389 48.644  4528/ 6572 250 (250)  w:sem 22        
 202 navigator                     546  0.000   912/ 1764 105 (105)  READY 16        
 220 logger                       6231  0.000  1256/ 3540 245 (245)  READY 24        
 229 log_writer_file                 0  0.000   360/ 1148  60 ( 60)  w:sem 24        
Processes: 17 total, 13 running, 4 sleeping, max FDs: 54        
CPU usage: 100.00% tasks, 0.00% sched, 0.00% idle        
DMA Memory: 5120 total, 1024 used 1024 peak        
Uptime: 476.753s total, 280.851s idle        
ERROR [sensors] Accel \\\\#0 fail:  TIMEOUT! IMU bias        
ERROR [sensors] Sensor Accel \\\\#0 failed. Reconfiguring sensor priorities.        
WARN  [sensors] Remaining sensors after failover event 0: Accel \\\\#0 priority: 1        
WARN  [sensors] Remaining sensors after failover event 0: Accel \\\\#1 priority: 1        
WARN  [sensors] Remaining sensors after failover event 0: Accel \\\\#2 priority: 1        
WARN  [ecl/EKF] EKF stopping navigation failover event 0: Accel \\\\#1 priority: 1        
WARN  [sensors] Remaining sensors after failover event 0: Accel \\\\#2 priority: 1        
WARN  [ekf2] accel id changed, resetting IMU bias        
ERROR [sensors] Baro \\\\#0 fail:  TIMEOUT!reset to baro        
ERROR [sensors] Sensor Baro \\\\#0 failed. Reconfiguring sensor priorities.        
WARN  [sensors] Remaining sensors after failover event 0: Baro \\\\#0 priority: 1        
WARN  [sensors] Remaining sensors after failover event 0: Baro \\\\#1 priority: 1        
WARN  [sensors] Remaining sensors after failover event 1: Baro \\\\#1 priority: 1        
```  
A more realistic 40 Khz.  
    
```bash     
  PID COMMAND                   CPU(ms) CPU(%)  USED/STACK PRIO(BASE) STATE FD        
   0 Idle Task                  298849 61.155   548/  748   0 (  0)  READY  3        
   1 hpwork                      12014  2.969   696/ 1780 249 (249)  READY  7        
   2 lpwork                       1668  0.481   872/ 1780  50 ( 50)  w:sig 10        
   3 init                        73363  0.000  1656/ 2484 100 (100)  w:sem  3        
 243 top                           102  4.093  1312/ 1684 255 (255)  RUN    3        
  12 dataman                         1  0.000   792/ 1180  90 ( 90)  w:sem  4        
  86 sensors                     73568  7.383  1288/ 1964 249 (249)  w:sem 22        
  88 commander                    4824  1.364  1256/ 3212 140 (140)  w:sig 31        
  89 commander_low_prio             12  0.000   552/ 2996  50 ( 50)  w:sem 31        
  95 mavlink_if0                   225  0.080  1280/ 2532 100 (100)  w:sig  4        
 173 gps                          1162  0.321  1168/ 1548 220 (220)  w:sem  5        
 180 mavlink_if0                 23865  3.210  1760/ 2484 100 (100)  w:sig 28        
 181 mavlink_rcv_if0              2088  0.642  1576/ 2836 175 (175)  w:sem 28        
 200 ekf2                       117884 14.767  4528/ 6572 250 (250)  w:sem 22        
 202 navigator                     605  0.240   912/ 1764 105 (105)  w:sem 16        
 220 logger                       6910  2.407  1256/ 3540 245 (245)  w:sem 24        
 229 log_writer_file                 0  0.000   360/ 1148  60 ( 60)  w:sem 24        
Processes: 17 total, 3 running, 14 sleeping, max FDs: 54        
CPU usage: 37.96% tasks, 0.88% sched, 61.16% idle        
DMA Memory: 5120 total, 1024 used 1024 peak        
Uptime: 570.482s total, 298.849s idle        
```  
I would suggest you check your code and insure your not running long threads off the ISR.  
