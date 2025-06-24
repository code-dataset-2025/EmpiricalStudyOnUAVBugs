# Basic Information:
### Title:  Mag timeout current master #7746 
### Issue status: Closed
### Author: sanderux
### Issue open time: Aug 7, 2017
# Report
### Report author: sanderux
### Report Time: Aug 7, 2017
### Report Content:   
@Stifael i am getting intermittent mag timeouts that coincide with the land detector.    
I did notice  on our last test flights the mag timeout every time it actually landed.    
On this vehicle it seems to give constant 'maybe landed' jumps that constantly coincide with mag timeouts.  
Maybe this is reversing cause and effect but this behavior is gone when i flash stable.  

# Comment
## Comment1
### Comment author: dagar
### Comment Time: Aug 7, 2017
### Comment Content:   
I suspect this is because both the land detector and the external mag (i2c) are running in the high priority work queue. The additional code in the land detector probably pushed it over the edge.  
I think we need some way to instrument the work queue and understand what's running in each and for how long.  
@davids5 FYI  

## Comment2
### Comment author: sanderux
### Comment Time: Aug 7, 2017
### Comment Content:   
Here's the full log of the bench test: https://logs.px4.io/plot_app?log=7308ecce-8078-4c20-a458-d8461a9fe6e5  

## Comment3
### Comment author: dagar
### Comment Time: Aug 8, 2017
### Comment Content:   
I want to instrument the work queues to understand what's happening, but I probably won't have time in the next day or two.  
Is this easy to reproduce on the bench? If so connect a console, run top, and note the HPWORK cpu usage. Then stop each of the following, noting HPWORK cpu usage after stopping each. This is a crude way of trying to understand what's happening in the high priority work queue.  
- fmu stop  
- land_detector stop  
- hmc5883 stop  
- ms5611 stop  
- using camera_trigger?  

## Comment4
### Comment author: bkueng
### Comment Time: Aug 8, 2017
### Comment Content:   
There was only very little code added to the land detector, I would not expect that to be the cause. However many tasks such as pos ctrl, sensors, estimator & att ctrl have higher prio than HPWORK, and if they use a bit more CPU due to a land detector state change, they can all be the cause of that.    
@sanderux can you try setting https://github.com/PX4/Firmware/blob/master/nuttx-configs/px4fmu-v2/nsh/defconfig\\\#L756 (make sure it's the build target that you use) to something like 253 and see if that helps (and do a clean build after changing it)?  

## Comment5
### Comment author: sanderux
### Comment Time: Aug 8, 2017
### Comment Content:   
@bkueng no change with prio 253    
(i did do a clean build)  

## Comment6
### Comment author: sanderux
### Comment Time: Aug 8, 2017
### Comment Content:   
Interestingly when i force no landing detected (by keeping throttle high) it doesn't timeout. it really only times out when if actually detects a landing (see messages above).  
I checked cpu usage with and without land detector. with everything running it's at +- 1.5%    
But: the LPWORK stays at a constant 35% cpu when i put throttle high. putting it low again returns the lpwork cpu to 0.07.  
repeating this test with land_detector stopped keeps lpwork at 0.07%  

## Comment7
### Comment author: sanderux
### Comment Time: Aug 8, 2017
### Comment Content:   
another interesting observation: this only happens on vtol in FW mode. in MC mode it's fine    
also in FW mode (as shown above) it constantly switches between landed and takeoff.  
Likely during FW mode the logic breaks down running the MC land detector  

## Comment8
### Comment author: Stifael
### Comment Time: Aug 8, 2017
### Comment Content:   
@sanderux, thats possible. I am looking at the log right now  

## Comment9
### Comment author: sanderux
### Comment Time: Aug 8, 2017
### Comment Content:   
I'm now testing with adding  
    
```bash     
 	// Only trigger in RW mode        
	if(!_vehicle_status.is_rotary_wing) {        
		return false;        
	}        
```  

## Comment10
### Comment author: Stifael
### Comment Time: Aug 8, 2017
### Comment Content:   
I mean it clearly breaks down. It has landdetected all over the place. interesting that it did not crash  

## Comment11
### Comment author: sanderux
### Comment Time: Aug 8, 2017
### Comment Content:   
it's a bench test. or did you mean the process?  

## Comment12
### Comment author: sanderux
### Comment Time: Aug 8, 2017
### Comment Content:   
I have a fix  

## Comment13
### Comment author: Stifael
### Comment Time: Aug 8, 2017
### Comment Content:   
why did the current changes have an effect on the FW mode?  
