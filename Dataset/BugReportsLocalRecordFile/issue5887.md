# Basic Information:
### Title:  RPi3: high cpu utilisation when auto start #5887 
### Issue status: Closed
### Author: lhc610github
### Issue open time: Nov 21, 2016
# Report
### Report author: lhc610github
### Report Time: Nov 21, 2016
### Report Content:   
Hi I have successfully running PX4 with Navio2 on RPi3.    
Now i have issues with auto starting this program as soon as the RPi3 has booted.:    
added the binary execution to rc.local    
cd /home/pi && ./px4 px4.config > startup.log    
It can successfully start the px4 program, but cpu utilisation is much higher than just start this program from shell or ssh. I couldn’t figure out . Could this be a linux distro problem (emlid RT kernel raspbian) or anything didn’t taken care of in PX4 code.    
Thanks in advance.    
fig 1 is auto start PX4 by rc.local    
this fig is start PX4 from shell or ssh  

# Comment
## Comment1
### Comment author: bkueng
### Comment Time: Nov 24, 2016
### Comment Content:   
I was able to reproduce, use the following line to fix it:  
    
```bash     
 cd /home/pi && ./px4 -d px4.config > px4.log        
```  
Note the -d which starts px4 in daemon mode.  
I added instructions to the DevGuide in PX4/PX4-Devguide\\\#68  
