# Basic Information:
### Title:  GLOBAL_POSITION_INT heading (hdg) overflow #9867 
### Issue status: Closed
### Author: superware
### Issue open time: Jul 9, 2018
### Fixed by: #9905
# Report
### Report author: superware
### Report Time: Jul 9, 2018
### Report Content:   
Describe the bug    
The heading (hdg) field in message GLOBAL_POSITION_INT is not in the protocol defined range of 0..35999 (degrees * 100).  
To Reproduce    
Steps to reproduce the behavior:  
1.Monitor message GLOBAL_POSITION_INT.  
2.Rotate vehicle 360 degrees.  
3.See GLOBAL_POSITION_INT.hdg overflowing.  
Expected behavior    
To see values in the range of 0..35999, UINT16_MAX for unknown.  
Additional context    
See here. My guess is that line should also wrap yaw between zero and 360 degrees, like it used to in previous versions.  

# Comment