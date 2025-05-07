# Basic Information:
### Title:  Crash in certain modes when using vmount #6783 
### Issue status: Closed
### Author: gcWorld
### Issue open time: Mar 11, 2017
# Report
### Report author: gcWorld
### Report Time: Mar 11, 2017
### Report Content:   
See http://discuss.px4.io/t/pixracer-1-5-5-fly-away/2507/7 for full discussion regarding this issue.  
When using the vmount driver and switching to any of the non-manual modes (Auto Hold, Offboard, Follow me) the system stops responding to any RC input, QGC looses the connection, logging stops, and all fail-safes are ignored.    
Notable is that during the initial fly-away the stabilisation was working and the drone kept its position (not the altitude though) until the battery ran out.  
Steps to reproduce:    
Equipment:  
- PixRacer, no props, tested indoors  
- PX4 1.5.5 stable via Qgroundcontrol  
- extras.txt with:  
    
```bash     
 \\\\#start mount driver        
vmount start        
set MNT_MODE_IN 2        
set MNT_MODE_OUT 0        
set MNT_MAN_CONTROL 1        
set MNT_MAN_PITCH 2        
```  
- Telemetry link to Linux machine with Uart example code (https://github.com/mavlink/c_uart_interface_example)  
After Take-off in manual mode launch uart example program. As soon as the program switches the flight mode to OFFBOARD the system stops responding.  
It was reported by another user that this behaviour also happens on a Pixhawk 2.4.5 using the PX4 current master.  

# Comment
## Comment1
### Comment author: LorenzMeier
### Comment Time: Mar 11, 2017
### Comment Content:   
@gcWorld Would you be able to increase this to 1700 and re-test?    
https://github.com/PX4/Firmware/blob/master/src/drivers/vmount/vmount.cpp\\\#L383  

## Comment2
### Comment author: gcWorld
### Comment Time: Mar 11, 2017
### Comment Content:   
No visible change in behaviour for me.  

## Comment3
### Comment author: PX4BuildBot
### Comment Time: Feb 21, 2018
### Comment Content:   
Hey, this issue has been closed because the label status/STALE is set and there were no updates for 30 days. Feel free to reopen this issue if you deem it appropriate.  
(This is an automated comment from GitMate.io.)  
