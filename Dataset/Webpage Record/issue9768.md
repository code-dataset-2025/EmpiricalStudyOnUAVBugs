# Basic Information:
### Title:  Descending with MPC_LAND_SPEED instead of MPC_Z_VEL_MAX_DN #9768 
### Issue status: Closed
### Author: ivodre
### Issue open time: Jun 26, 2018
# Report
### Report author: ivodre
### Report Time: Jun 26, 2018
### Report Content:   
Describe the bug    
When descending during a mission in simulation the Deltaquad does the whole descend with MPC_LAND_SPEED instead of descending with MPC_Z_VEL_MAX_DN until MPC_LAND_ALT1, and than ramping down to MPC_LAND_SPEED.  
To Reproduce    
Steps to reproduce the behavior:  
1.Create "multicopter" mission with delta quad in gazebo (e.g. at 30m altitude)  
2.Make sure to set reasonable values for MPC_LAND_SPEED, MPC_Z_VEL_MAX_DN, MPC_LAND_ALT1, MPC_LAND_ALT2  
3.Start mission  
Expected behavior    
The vehicle climbs with MPC_Z_VEL_MAX_UP, flies at desired altitude and than descends with MPC_LAND_SPEED all the way to the ground.  
Log Files    
https://logs.px4.io/plot_app?log=70e15793-db80-4ec7-91d8-d1b6af522e70  
Drone (please complete the following information):  
- Gazebo Deltaquad  
Additional context    
We observed this also in real flights  
@lamping7  

# Comment
## Comment1
### Comment author: dagar
### Comment Time: Jun 26, 2018
### Comment Content:   
@sanderux @RomanBapst  

## Comment2
### Comment author: dagar
### Comment Time: Jun 26, 2018
### Comment Content:   
Likely an issue with the multicopter position controller rather than VTOL specific.  

## Comment3
### Comment author: dakejahl
### Comment Time: Jun 26, 2018
### Comment Content:   
Please see \\\#9772  

## Comment4
### Comment author: stale
### Comment Time: Jan 21, 2019
### Comment Content:   
This issue has been automatically marked as stale because it has not had recent activity. It will be closed if no further activity occurs. Thank you for your contributions.  

## Comment5
### Comment author: stale
### Comment Time: Feb 4, 2019
### Comment Content:   
Closing as stale.  
