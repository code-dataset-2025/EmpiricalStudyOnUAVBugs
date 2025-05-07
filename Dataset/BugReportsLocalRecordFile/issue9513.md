# Basic Information:
### Title:  The Optical Flow Gazebo simulation is prohibitively slow on v1.8.0beta #9513 
### Issue status: Closed
### Author: AlexisTM
### Issue open time: May 23, 2018
# Report
### Report author: AlexisTM
### Report Time: May 23, 2018
### Report Content:   
Bug Report  
Explaination  
The gazebo optical flow simulation is incredibly slow using 1.8.0b branch but fast using 1.7.3 branch.  
Doing the simulation without PX4Flow works at full speed.  
Observations  
On 1.8.0.beta with PX4Flow:  
- When the copter moves, the real-time factor starts to drop as low as 0.02.  
- When the copter is hovering, the copter has a real-time factor of 1.0.  
On 1.8.0.beta without PX4Flow:  
- The real-time factor stays at 1.0 during the whole offboard mission.  
On 1.7.3 with PX4Flow:  
- The real-time factor stays at 1.0 during the whole offboard mission.  
Reproduce the problem:  
v1.8.0b PX4Flow  
    
```bash     
 git clone --recursive http://github.com/PX4/Firmware -b v1.8.0-beta1 PX4.1.8.0b      
cd PX4.1.8.0b      
make -j8 posix gazebo_iris_opt_flow       
roslaunch mavros px4.launch fcu_url:="udp://:14540@127.0.0.1:14557"      
\\\\\# Run a mission: goto(3,0,0), goto(6,0,0), goto(0,0,0)     
```  
v1.8.0b without PX4Flow  
    
```bash     
 git clone --recursive http://github.com/PX4/Firmware -b v1.8.0-beta1 PX4.1.8.0b      
cd PX4.1.8.0b      
make -j8 posix gazebo_iris      
roslaunch mavros px4.launch fcu_url:="udp://:14540@127.0.0.1:14557"      
\\\\\# Run a mission: goto(3,0,0), goto(6,0,0), goto(0,0,0)     
```  
v1.7.3 PX4Flow  
    
```bash     
 git clone --recursive http://github.com/PX4/Firmware -b v1.7.3 PX4.1.7.3      
cd PX4.1.7.3      
make -j8 posix gazebo_iris_opt_flow       
roslaunch mavros px4.launch fcu_url:="udp://:14540@127.0.0.1:14557"      
\\\\\# Run a mission: goto(3,0,0), goto(6,0,0), goto(0,0,0)     
```  
Running under Linux Ubuntu 16.04.  

# Comment
## Comment1
### Comment author: dagar
### Comment Time: May 23, 2018
### Comment Content:   
Thanks for the detailed report, I've actually just started looking at getting optical flow into our CI system.  
Would you be able to do any profiling (http://www.brendangregg.com/flamegraphs.html)? As a start you could simply run top or htop with all threads listed.  
@TSC21 any initial thoughts here?  

## Comment2
### Comment author: AlexisTM
### Comment Time: May 23, 2018
### Comment Content:   
Flamegraph seems awesome! I will try to use it tomorrow :)  

## Comment3
### Comment author: TSC21
### Comment Time: May 23, 2018
### Comment Content:   
We should change the world to use the asphalt_plane instead  

## Comment4
### Comment author: AlexisTM
### Comment Time: May 23, 2018
### Comment Content:   
The two branches v1.7 3 and 1.8.0beta are using the same world; do it should not come from the world texture.  

## Comment5
### Comment author: mhkabir
### Comment Time: May 23, 2018
### Comment Content:   
I only see this issue on the uneven_ground world. In the asphalt_plane world, 1.8 functions as normal.  

## Comment6
### Comment author: LorenzMeier
### Comment Time: May 28, 2018
### Comment Content:   
@mhkabir Do you want to send a PR to fix?  

## Comment7
### Comment author: mhkabir
### Comment Time: May 28, 2018
### Comment Content:   
It's not a fix, it's rather a workaround. Something is broken in 1.8 which needs fixing. I can send in the workaround, but do not recommend it for the release instead of fixing whatever is wrong.  

## Comment8
### Comment author: LorenzMeier
### Comment Time: May 28, 2018
### Comment Content:   
Not necessarily. For setups that were borderline in terms of CPU a more complex terrain model might be all it takes to break them.  

## Comment9
### Comment author: mhkabir
### Comment Time: May 28, 2018
### Comment Content:   
It's not borderline as far as I can see. The complex terrain model works perfectly on v1.7.3 across the full range of vehicle dynamics on the same computer without any drop in framerate compared to the vanilla simulation.  
See @AlexisTM's detailed report in the issue.  

## Comment10
### Comment author: Oceasdeep
### Comment Time: Jul 22, 2018
### Comment Content:   
@LorenzMeier Hello,Now I have a problem with 1.8.0 my px4flow didn't localization indoor,but using 1.6.3locallization very well,I don't know why ,did I set something wrong?waiting for your answer,thanks in advance.  

## Comment11
### Comment author: AlexisTM
### Comment Time: Jul 22, 2018
### Comment Content:   
@Oceasdeep This issue is only on simulation. It works wonderfully for our setup with the PX4Flow and PX4 1.8.0  

## Comment12
### Comment author: TSC21
### Comment Time: Dec 10, 2018
### Comment Content:   
@AlexisTM still an issue?  

## Comment13
### Comment author: AlexisTM
### Comment Time: Dec 10, 2018
### Comment Content:   
I did not run it for quite some time but can only test it next week.  

## Comment14
### Comment author: AlexisTM
### Comment Time: Dec 20, 2018
### Comment Content:   
@TSC21 The world is now the even ground and I seem to have no drop. Can be closed for me.  
