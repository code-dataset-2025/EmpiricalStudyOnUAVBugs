# Basic Information:
### Title:  EKF2 Indoor Mag Mode not functional #9716 
### Issue status: Closed
### Author: mhkabir
### Issue open time: Jun 19, 2018
# Report
### Report author: mhkabir
### Report Time: Jun 19, 2018
### Report Content:   
Describe the bug    
The EKF2 Indoor Mag fusion mode (EKF2_MAG_TYPE = 4) does not function on master and v1.8 release.  
To Reproduce    
Set EKF2_MAG_TYPE=4 and reboot vehicle, or restart ekf2 in SITL (gazebo_iris_opt_flow).  
Expected behavior    
The EKF should initialize and produce an attitude estimate.  
In this case, the EKF does not initialise or produce an attitude estimate.  
Log Files and Screenshots    
Log from SITL : https://logs.px4.io/plot_app?log=5c2e7e20-35de-4278-bee8-40ba1b92c242  
    
```bash     
 pxh> ekf2 status        
INFO  [ekf2] local position OK no        
INFO  [ekf2] global position OK no        
INFO  [ekf2] time slip: 0 us        
```  

# Comment
## Comment1
### Comment author: priseborough
### Comment Time: Jun 20, 2018
### Comment Content:   
This fixes it on replay: https://github.com/PX4/ecl/tree/pr-ekfBugFix.  
I also noticed the artificial sensor noise on the SITL simulation which is the same on-ground and in-flight is causing the _vehicle_at_rest check to fail, which turns off fusion of the last known yaw angle, allowing the yaw to drift when on ground. I do not see this on hardware.  
If you don't get a chance, I will test further tomorrow.  

## Comment2
### Comment author: mhkabir
### Comment Time: Jun 20, 2018
### Comment Content:   
Just tested, it seems that yaw angle drift is present on ground. It also drifts quite a lot in the air, which is not entirely unexpected, but I expected better given that I'm using a temperature calibrated gyro.  
Here is a replay log : https://review.px4.io/plot_app?log=c3632182-1b19-4c9c-9a19-a2816d6b982c  

## Comment3
### Comment author: priseborough
### Comment Time: Jun 22, 2018
### Comment Content:   
I need data logging from boot to be able to debug on replay.  

## Comment4
### Comment author: mhkabir
### Comment Time: Jun 22, 2018
### Comment Content:   
Whoops, I thought I had logging from boot enabled. Sorry, will redo.  

## Comment5
### Comment author: priseborough
### Comment Time: Aug 24, 2018
### Comment Content:   
@mhkabir ping  

## Comment6
### Comment author: stale
### Comment Time: Jan 21, 2019
### Comment Content:   
This issue has been automatically marked as stale because it has not had recent activity. It will be closed if no further activity occurs. Thank you for your contributions.  

## Comment7
### Comment author: stale
### Comment Time: Feb 4, 2019
### Comment Content:   
Closing as stale.  
