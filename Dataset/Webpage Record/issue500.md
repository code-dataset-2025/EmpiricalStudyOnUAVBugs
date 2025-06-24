# Basic Information:
### Title:  px4_simple_app: crash when app returns #500 
### Issue status: Closed
### Author: julianoes
### Issue open time: Oct 29, 2013
# Report
### Report author: julianoes
### Report Time: Oct 29, 2013
### Report Content:   
This issue relates to this email thread:    
https://groups.google.com/d/msg/px4users/nRxxc2HrzO4/lF3tDS-_drEJ  
Basically, when the px4_simple_app returns after printing some values instead of looping forever, it sometimes crashes the FMU.  
The issue can be reproduced using this commit 6d17af3  
    
```bash     
 Program received signal SIGINT, Interrupt.        
0x0809650c in setbasepri (basepri=16) at /home/joes/src/Firmware/NuttX/nuttx/include/arch/armv7-m/irq.h:227        
227   __asm__ __volatile__        
(gdb) info line        
Line 227 of "/home/joes/src/Firmware/NuttX/nuttx/include/arch/armv7-m/irq.h"        
   starts at address 0x8096506 <_up_assert+22> and ends at 0x809650e <_up_assert+30>.        
(gdb) info line        
Line 227 of "/home/joes/src/Firmware/NuttX/nuttx/include/arch/armv7-m/irq.h"        
   starts at address 0x8096506 <_up_assert+22> and ends at 0x809650e <_up_assert+30>.        
(gdb) bt        
\\\\#0  0x0809650c in setbasepri (basepri=16) at /home/joes/src/Firmware/NuttX/nuttx/include/arch/armv7-m/irq.h:227        
\\\\#1  irqsave () at /home/joes/src/Firmware/NuttX/nuttx/include/arch/armv7-m/irq.h:255        
\\\\#2  _up_assert (errorcode=<optimized out>) at armv7-m/up_assert.c:289        
\\\\#3  0x080968b6 in up_assert (filename=0x80d5278 "armv7-m/up_hardfault.c", lineno=16) at armv7-m/up_assert.c:331        
\\\\#4  0x08096ad0 in up_hardfault (irq=<optimized out>, context=<optimized out>) at armv7-m/up_hardfault.c:184        
\\\\#5  0x080b3df4 in irq_dispatch (irq=16, context=0x200055dc) at irq_dispatch.c:103        
\\\\#6  0x080aefbc in up_doirq (irq=3, regs=0x200055dc) at armv7-m/up_doirq.c:102        
\\\\#7  0x08096a1c in exception_common () at armv7-m/up_exception.S:141        
/home/build/work/jenkins-daily-build/src/gdb/gdb/regcache.c:178: internal-error: register_size: Assertion `regnum >= 0 && regnum < (gdbarch_num_regs (gdbarch) + gdbarch_num_pseudo_regs (gdbarch))' failed.        
A problem internal to GDB has been detected,        
further debugging may prove unreliable.        
```  

# Comment
## Comment1
### Comment author: LorenzMeier
### Comment Time: Oct 29, 2013
### Comment Content:   
On which hardware version did you reproduce this?  

## Comment2
### Comment author: julianoes
### Comment Time: Oct 29, 2013
### Comment Content:   
FMUv1  

## Comment3
### Comment author: LorenzMeier
### Comment Time: Nov 3, 2013
### Comment Content:   
Fixed in \\\#509  
