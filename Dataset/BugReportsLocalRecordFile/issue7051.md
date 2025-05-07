# Basic Information:
### Title:  Oscillations on actuators with full thrust and roll ~ 45 degree #7051 
### Issue status: Closed
### Author: svpcom
### Issue open time: Apr 14, 2017
# Report
### Report author: svpcom
### Report Time: Apr 14, 2017
### Report Content:   
HW: pixhawk (fmu-v2) + quadcopter x6    
FW: px4 stable in EKF2 mode  
I've found that on full thrust there are actuators oscillations with roll ~45 degree.    
To ensure that is not related to frame vibration i've disconnect all engines and made a test again.    
So it is easy to reproduce:  
1.disconnect engines from fmu  
2.arm throttle (manual mode without gps available)  
3.set max throttle  
4.Slowly roll copter ~45 degree left and see actuators oscillations (from min to max)  
http://logs.uaventure.com/view/FbSe3zE7oB3WVCMqqbNF2e  

# Comment
## Comment1
### Comment author: MaEtUgR
### Comment Time: Apr 18, 2017
### Comment Content:   
Thanks for your report, I see your point there in the log!    
I suppose your drone flies normaly with hover thrust here. First I thought you may have vibrations or other effects like steeper motor input to thrust curve with higher throttle that leads to control loop oscillations.    
But your log seems to reveal some weird mixer limiting bug on full throttle... We need to track this down.    
What do you think @Stifael ?  

## Comment2
### Comment author: svpcom
### Comment Time: Apr 18, 2017
### Comment Content:   
@MaEtUgR Yes, i'm not flying with 45deg roll, but i'm doing a test "in hands" before flying. I've upgraded my copter with ESC that have active braking feature (opposite to ordinary esc which reduce rpm via removing power and air braking) and found that engines became "clicks" when I do aggressive stick movements on full throttle. I've repeat a test without control actions and found that there is a frame orientation where there are continuous oscillations in engine control signal. My first guess was a frame resonance with engines. I've disconnect all motors but engine control oscillations  continued.  

## Comment3
### Comment author: MaEtUgR
### Comment Time: Apr 18, 2017
### Comment Content:   
@svpcom ok, got it. Looking at the log I can see the sudden motor output dropouts with always full throttle. Currently I think it is a corner case in the multicopter mixer: https://github.com/PX4/Firmware/blob/master/src/modules/systemlib/mixer/mixer_multirotor.cpp\\\#L215    
In principle like it's implemented now it should not drop the throttle no matter what rotation input you give. But when you tilt the vehicle like in your hand held test, the attitude and rate controllers go to full rotation torque output to counteract and I bet the mixer runs into some full throttle full rotation combination of limits that is not handeled correctly.  

## Comment4
### Comment author: LorenzMeier
### Comment Time: Apr 27, 2017
### Comment Content:   
@MaEtUgR Any news?  

## Comment5
### Comment author: LorenzMeier
### Comment Time: May 4, 2017
### Comment Content:   
I've inspected this. What is happening is that the system (correctly) detects an actuator saturation and engages a recovery mixing strategy to maximize torque along the roll and pitch axes to recover the attitude. You can consider this a safety envelope that should never be reached by the top-level controller and kicks in here as the controller is making demands that are not feasible in an under-actuated system.  
We could try to make the transition between normal operation and failsafe less discontinuous, but that would come at the price of either starting to interfere with the attitude controller sooner (which would deteriorate performance) or to react slower when we enter the under-actuated limit zone, which could make the system flip more easily.  
That said, it will take some thought and time to do this with very likely very limited returns. If you try to do acrobatic flying the best we can do is probably to disable the mixer protection as an option. But for the normal use cases that's not what you want.  

## Comment6
### Comment author: svpcom
### Comment Time: May 4, 2017
### Comment Content:   
Ok, i got it. My main idea was that in case of electrodynamic braking discontinuous switch between min thrust and max thrust caused engine overheat. Can mixer saturation happens when flying on high wind condition (or braking from max horizontal speed) or it is hard to achieve in real flights ?  

## Comment7
### Comment author: MaEtUgR
### Comment Time: May 8, 2017
### Comment Content:   
@svpcom if you hit the limits and in which cases heavily depends on your entire setup including vehicle size, actuation and also controller tuning. But while developing I would always expect to hit the limit because it will happen especially when you tune for high performance.  
@LorenzMeier I don't see why such discontinuities would make sense if the input to the mixer is pretty smooth. The mixer should apart from the values where you hit the limit continue to distribute actuation in a different combination and not generate any steps because of limit switching with smooth input.    
I suspect it is an error that was found here.  

## Comment8
### Comment author: MaEtUgR
### Comment Time: May 9, 2017
### Comment Content:   
@svpcom I tried to reproduce the problem on current stable and master without success. I used a pixracer and defualt parameters (which you also had in your log for the attitude controller). I managed to get it into the limits but with a rather smooth input I could not get any extreme discontinuities like you had.  
I could not find out what version you used from the log because the commit hash af8fbbf is not in the main history so you probably used some custom branch that forked somewhere.  
There were some fixes related to the mixer for example: 084e714    
But again you have to check on which version you were.  
Can you please try to reproduce this exact issue on the current master? If the error is still in there I would love to find it.  

## Comment9
### Comment author: svpcom
### Comment Time: May 9, 2017
### Comment Content:   
@MaEtUgR  My version is a current stable branch with small fixes related to mavlink stream (https://github.com/svpcom/Firmware/tree/eval_stable). I'll retest this issue with current master today.  

## Comment10
### Comment author: MaEtUgR
### Comment Time: May 9, 2017
### Comment Content:   
Ok, thanks 👍  

## Comment11
### Comment author: MaEtUgR
### Comment Time: May 9, 2017
### Comment Content:   
@svpcom Ah maybe I found it. On the current stable when I rotated in roll like you did there is a spike and when I go back again there is one in the opposite direction. Is this the same? Did you intentionally switch back and forth between the two states for your log to get these numerous steps?    

## Comment12
### Comment author: svpcom
### Comment Time: May 9, 2017
### Comment Content:   
@MaEtUgR In my case these were continuous oscillations (from min to max) when i hold a copter with roll ~45deg left. My setup was pixhawk v2.4.6 (EKF2 mode) + SF11/c lidar.  

## Comment13
### Comment author: svpcom
### Comment Time: May 9, 2017
### Comment Content:   
@MaEtUgR Got oscillations with latest master too:    
http://review.px4.io/plot_app?log=1c12f28d-7e82-4747-8196-c66e77ff2db0    
log got with motors enabled  

## Comment14
### Comment author: svpcom
### Comment Time: May 10, 2017
### Comment Content:   
@MaEtUgR any ideas?  

## Comment15
### Comment author: MaEtUgR
### Comment Time: May 16, 2017
### Comment Content:   
I think I even reproduced this issue on a different platform that I'm currently using... sorry but I didn't find the time to get to the root cause yet 😞 It's on my list and we have to fix the mixer which I'm still blaming right now.  

## Comment16
### Comment author: diegoeck
### Comment Time: May 17, 2017
### Comment Content:   
Hi, i'm new to the community but i think i can help. It may be a controller problem, maybe wind-up. Does the problem occur if the roll rate integral term is null (MC_ROLLRATE_I=0)? I can't see in your log the controller output (the output from the controller that goes to the mixer). I believe the problem is before the mixer.  

## Comment17
### Comment author: dagar
### Comment Time: May 17, 2017
### Comment Content:   
@diegoeck  
The controller output is actuator_controls per axis [-1, 1]. ATTC.Roll, ATTC.Pitch, ATTC.Yaw    
http://logs.uaventure.com/view/FbSe3zE7oB3WVCMqqbNF2e  
Here's the same plot with the integrators (x10 for visualization). MACS = multicopter attitude control status  

## Comment18
### Comment author: diegoeck
### Comment Time: May 17, 2017
### Comment Content:   
Well, then it seems it is something related to the mixer. When the output ATTC.Roll crosses the value 0.5 the mixer seems to be summing something. Definetly it something related with the saturation, but i can't exatly find the problem. It is also strange that MACS.RRint seems to be constant while the problem occurs.  

## Comment19
### Comment author: svpcom
### Comment Time: May 30, 2017
### Comment Content:   
@MaEtUgR \\\#7310 doesn't help  

## Comment20
### Comment author: mhkabir
### Comment Time: May 30, 2017
### Comment Content:   
I just saw this in flight a few days back. I can't match up the logs, but I was flying master as of that day. I was flying really aggressively in stabilize mode. It would oscillate heavily when I commanded completely opposite responses when rolling pitching to ~45 degrees in the other direction.  
Will send logs when I find them.  

## Comment21
### Comment author: svpcom
### Comment Time: May 30, 2017
### Comment Content:   
@mhkabir  my logs: http://review.px4.io/plot_app?log=ba03e0b6-9146-4e42-aac7-50d2ba333b2a    
Was tested without props in hands in ALT_CTL mode  

## Comment22
### Comment author: svpcom
### Comment Time: May 30, 2017
### Comment Content:   
@MaEtUgR @mhkabir It seems something bad happens with mixer if pitch control is near 0.5 (see at 34:20 - 34:40). May be float precision lost somewhere in mixer code when substracting 0.5 ?  

## Comment23
### Comment author: svpcom
### Comment Time: Jun 19, 2017
### Comment Content:   
@MaEtUgR any updates?  

## Comment24
### Comment author: MaEtUgR
### Comment Time: Jul 3, 2017
### Comment Content:   
No, I'm sorry I did not find the time 😞 I know it's important.  

## Comment25
### Comment author: LorenzMeier
### Comment Time: Oct 5, 2017
### Comment Content:   
We revised the controller and I'm closing this as stale. Please re-open if it persists on master.  
