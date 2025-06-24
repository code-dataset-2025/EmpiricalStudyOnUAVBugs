# Basic Information:
### Title:  RTL mode state is not being reset to NONE #6669 
### Issue status: Closed
### Author: matanhavi
### Issue open time: Feb 25, 2017
### Fixed by: #6670
# Report
### Report author: matanhavi
### Report Time: Feb 25, 2017
### Report Content:   
When RTL mode is being deactivated, and then re-activate, the RTL mode is not always goes to RTL_STATE_NONE.    
On some case it is, if for example a mission is being triggered on between.    
It can be easily reproduced on the simulator (iris, ekf2)  
1.takeoff  
2.fly to another location (you must fly, another bug is that RTL is not started if triggered just after takeoff)  
3.start RTL  
4.the drone will climb (RTL_STATE_CLIMB)  
5.the drone will return home (RTL_STATE_RETURN)  
6.the drone will start descending (RTL_STATE_DESCEND)  
7.pause the drone  
8.fly to another location  
9.start RTL again  
10.(BUG here) instead of starting the RTL from beginning (step 4) it will continue from it last state (in this case descending)  
its much more critical if during RTL mode its goes as far to RTL_STATE_LAND mode.    
its seems that a call to set_can_loiter_at_sp(true) should be done on some places on the code (which I am not sure where)  

# Comment
## Comment1
### Comment author: dagar
### Comment Time: Feb 25, 2017
### Comment Content:   
Thanks for reporting. I'll take a look.  

## Comment2
### Comment author: LorenzMeier
### Comment Time: Feb 25, 2017
### Comment Content:   
I have a fix coming.  

## Comment3
### Comment author: LorenzMeier
### Comment Time: Feb 25, 2017
### Comment Content:   
Fix is here: \\\#6670  
