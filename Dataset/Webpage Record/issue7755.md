# Basic Information:
### Title:  vmount causes system freeze #7755 
### Issue status: Closed
### Author: ndepal
### Issue open time: Aug 9, 2017
# Report
### Report author: ndepal
### Report Time: Aug 9, 2017
### Report Content:   
I'm trying to use vmount with mavlink inputs (MNT_MODE_IN 3, i.e. MAVLINK_DO_MOUNT) and with mavlink output (MNT_MODE_OUT 1, i.e. MAV_CMD_DO_MOUNT_CONTROL).  
When I configure a PixRacer this way, vmount and in fact the whole system freezes: console via debug port no longer responsive, QGC loses connection, PixRacer stops flashing.  
Steps to reproduce  
- Flash current master  
- reset all parameters  
- on the console:  
    
```bash     
 param set MNT_MODE_IN 3        
param set MNT_MODE_OUT 1        
vmount start        
```  
I suspect the problem lies in the fact that in this configuration, the vmount input InputMavlinkCmdMount subscribes to vehicle_command and the output OutputMavlink publishes on it, causing a loop.  
I tried preventing InputMavlinkCmdMount from processing messages that were published by OutputMavlink by checking here that the system and component IDs don't match the one's that vmount itself is publishing, but it didn't help.  
@bkueng , any ideas?  

# Comment
## Comment1
### Comment author: bkueng
### Comment Time: Aug 10, 2017
### Comment Content:   
Yep, this is easily reproducible thanks to your precise steps. I'll look into it.  

## Comment2
### Comment author: LorenzMeier
### Comment Time: Aug 13, 2017
### Comment Content:   
Fixed.  
