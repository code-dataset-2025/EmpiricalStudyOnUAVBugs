# Basic Information:
### Title:  PX4 allows arming while the control is not fully initialized. (TARGET_LOCAL_NED not yet published) (workaround proposed) #9200 
### Issue status: Closed
### Author: AlexisTM
### Issue open time: Mar 30, 2018
# Report
### Report author: AlexisTM
### Report Time: Mar 30, 2018
### Report Content:   
Bug Report    
We were experiencing from time to time something that looked like a "random rotation towards North" at the takeoff of our copters. Today, we successfully reproduced it in a Gazebo simulation. It seems that we are capable of arming and taking off in offboard mode without any position (GPS or PX4Flow). Therefore, our commands (vx, vy, vz yaw_rate)  are ignored except vz.  
The takeoff procedure is the following:  
- OFFBOARD  
- ARM  
- (Vx=0, Vy=0, Vz=3.0, yaw_rate=0) until a certain altitude.  
When the simulation is started from a certain time, it works perfectly (well straight takeoff) but when the simulation is just started, we can still go in offboard, arm and takeoff but additionally to the expected drift, the copter rotates to north (the gazebo simulation starts pointing east)  
-     
Log: https://logs.px4.io/plot_app?log=5477f120-408d-4ce5-82e1-3b3d695a3a03    
-     
Expected behaviour:    
- The copter does not arm until GPS fix or PX4Flow fix    
- If the copter arms, it should drift as the position is not fixed    
-     
Behaviour:    
- The copter arms    
- The copter drifts    
- The copter rotates around the yaw angle    
-     
Steps to reproduce the problem:    
- Start Mavros over UDP link      
- roslaunch mavros px4.launch fcu_url:="udp://:14540@127.0.0.1:14557"`      
- Prepare your OFFBOARD control method    
- Start the simulation      
- make -j8 posix_sitl_default gazebo      
- Run your OFFBOARD control method    
-     
Results:    
- The copter arms, but rotates from East to North and drifts until we see in the console of the simulator: "EKF GPS checks passed (WGS-84 origin set)" and "EKF commencing GPS fusion".    
- The rest of the mission works fine.    
-     
Simulation console information:    
    
```bash     
 INFO  [mavlink] partner IP: 127.0.0.1        
WARN  [mavlink] [timesync] Hard setting offset.        
INFO  [lib__ecl] EKF aligned, (pressure height, IMU buf: 15, OBS buf: 14)        
INFO  [tone_alarm] positive        
INFO  [tone_alarm] positive        
INFO  [tone_alarm] arming        
INFO  [commander] Takeoff detected        
INFO  [tone_alarm] positive        
INFO  [lib__ecl] EKF GPS checks passed (WGS-84 origin set)        
INFO  [lib__ecl] EKF commencing GPS fusion        
```  
-     
Hardware in simulation: IRIS+    
-     
Firmware:    
- PX4 1.6.5    
- PX4 1.7.3    
-     
CURRENT WORKAROUND:    
- Subscribe to ~setpoint_raw/local topic (handle_position_target_local_ned Mavlink Handler) and do not approve takeoff before the topic is published.    
- Once published, an additional (optional?) step is to verify that the position (x,y,z,yaw) in the TARGET_LOCAL message is very close to the current LOCAL_POSITION.    
- Takeoff safely    

# Comment
## Comment1
### Comment author: dagar
### Comment Time: Apr 2, 2018
### Comment Content:   
Thanks for the detailed report. I'm hoping we can do a much better job locking this stuff down. This PR is just the start \\\#9193.  

## Comment2
### Comment author: AlexisTM
### Comment Time: Apr 6, 2018
### Comment Content:   
@dagar The same behaviour is observed with PX4Flow only.  
Mask used - 0b0000011111000111 which is: vx, vy, vz, yawrate  
Observed: The yaw setpoint is still 0 at the takeoff while we are sending "yawrate = 0" setpoints.    
Expected: yaw_sp = current_yaw if yawrate = 0.  
    
```bash     
 NFO  [lib__ecl] EKF aligned, (pressure height, IMU buf: 15, OBS buf: 14)        
INFO  [tone_alarm] positive        
INFO  [tone_alarm] positive        
INFO  [commander] Takeoff detected           
INFO  [tone_alarm] positive         
```  
NOTE: The typemask seems to be wrongly saved in target_local on the PX4 Firmware  

## Comment3
### Comment author: AlexisTM
### Comment Time: Apr 6, 2018
### Comment Content:   
@dagar  
To know when to takeoff, we have to wait for the topic setpoint_raw/target_local to be published. If we start before it is published, it starts to be published with a yaw angle default to 0 instead to default to the current copter yaw position (probably the same problem for X,Y position as well but less visible as the copter starts in (0,0).). setpoint_raw/target_local  is the ROS publisher for the MAVLink handler:  
    
```bash     
 handle_position_target_local_ned(const mavlink::mavlink_message_t *msg, mavlink::common::msg::POSITION_TARGET_LOCAL_NED &tgt)    
```  
NOTE: I don't know where the message is published in the PX4 stack.  

## Comment4
### Comment author: dagar
### Comment Time: Apr 6, 2018
### Comment Content:   
How do we roll that into PX4? One part of commander is cleanly collecting the validity of all these things. The other piece that's missing in many cases is defining if it should be required or not and at which times (arming, state transitions, active mode).  
Can you answer these questions for the cases you care about?  

## Comment5
### Comment author: AlexisTM
### Comment Time: Apr 7, 2018
### Comment Content:   
Observation: When the target_local_ned is published, the offboard mode is operational (no yaw rotation on takeoff)  
As it is filled with the position/velocity/acceleration setpoints, I guess it is published only if the mc_pos_control module is ready and the default setpoint initialized, which can be done only if we have a position/velocity input for the EKF2 filter.  
Problem: The offboard mode can be used without any position (RollPitchYawThrust setpoints) and position setpoints, which requires the position control to be started and the setpoints to be initialized (defaulted to current position and yaw).  
Solution 1: Add to one of the status message the current control capabilities of the system.  
- POSITION  
- VELOCITY  
- ACCELERATION  
- FORCE  
- ANGULAR_THRUST  
- ANGULAR_RATES_THRUST  
This would allow the offboard software to know what is feasible.  
Solution 2: Add a new modes: OFFBOARD_POSITION and OFFBOARD_RAW that allow to control the copter with different sets of setpoints. Disallow the OFFBOARD_POSITION mode if everything (expressed above) is not ready. The OFFBOARD_POSITION would allow all setpoints, while the second would only allow "raw" setpoints that uses the mc_att_control. Note that an application might want to start in a GPS denialed place and then switch to offboard position mode. In that case, the capabilities would be required (to avoid to "try to switch to see if it is available" instead of switching when it is possible.  

## Comment6
### Comment author: AlexisTM
### Comment Time: Apr 10, 2018
### Comment Content:   
@dagar    
It seems the fix of looking at the ~setpoint_raw/target_local topic (loopback of the executed command onto the Pixhawk) is not working with the PX4Flow.  
In GPS mode: The topic is published once we have the GPS fix and the yaw is correct.    
In OpticalFlow mode: The topic is not published (probably because the PX4Flow quality is 0 as we are on the ground) but when we switch to OFFBOARD mode, the topic is published but the yaw of the target is not equal to the yaw of the position. Once we take off, the PX4Flow goes valid but the target yaw was 0. Thus, the copter rotates towards North (yaw = 0 in NED).  
UPDATE: The ~setpoint_raw/target_local is published in mavlink_messages.cpp\\\#L2666-L2740 and come from the uOrb topic: vehicle_local_position_setpoint  
The only place this is published is by the mc_pos_control_main.cpp.  
    
```bash     
 $ grep -nr "orb_publish(ORB_ID(vehicle_local_position_setpoint)" .         
./src/modules/mc_pos_control/mc_pos_control_main.cpp:2362:  orb_publish(ORB_ID(vehicle_local_position_setpoint), _local_pos_sp_pub, &_local_pos_sp);        
```  
The MAVLink message set_position_target_local_ned is handled and published through offboard messages.  
In the mc_pos_control, the uOrb topic is published if any position control is used. (That's why it's sent when we switch to OFFBOARD mode).  
https://github.com/PX4/Firmware/blob/f160743df40b9dcc9558f3df1c6eeaf56646a758/src/modules/mc_pos_control/mc_pos_control_main.cpp\\\#L2342-L2366  
The yaw (which is the issue) comes from the attitude setpoint. _att_sp.yaw_body. It is filled by the offboard setpoint and by integrating the yawrate setpoint.  
https://github.com/PX4/Firmware/blob/f160743df40b9dcc9558f3df1c6eeaf56646a758/src/modules/mc_pos_control/mc_pos_control_main.cpp\\\#L1245-L1250  
Yet, _att_sp.yaw_body is defaulted to 0 while we send only yawrate=0 commands. Therefore, the copter rotates. The _att_sp.yaw_body defaults to the current yaw angle on GPS fix.  

## Comment7
### Comment author: AlexisTM
### Comment Time: Apr 10, 2018
### Comment Content:   
A fix would be to reinitialize the attitude setpoint (_att_sp) (thus the position setpoint yaw (_local_pos_sp)) on arming?  

## Comment8
### Comment author: stale
### Comment Time: Jan 26, 2019
### Comment Content:   
This issue has been automatically marked as stale because it has not had recent activity. It will be closed if no further activity occurs. Thank you for your contributions.  

## Comment9
### Comment author: stale
### Comment Time: Jun 24, 2019
### Comment Content:   
This issue has been automatically marked as stale because it has not had recent activity. It will be closed if no further activity occurs. Thank you for your contributions.  

## Comment10
### Comment author: stale
### Comment Time: Jul 8, 2019
### Comment Content:   
Closing as stale.  

## Comment11
### Comment author: julianoes
### Comment Time: Jul 9, 2019
### Comment Content:   
@AlexisTM is there still work to do here?  

## Comment12
### Comment author: AlexisTM
### Comment Time: Jul 9, 2019
### Comment Content:   
I implemented a safety check and changed the default setpoints in the application software and did not experience it ever since.  
The safety check is sending a zero velocity setpoint until local_position/pose and setpoint_raw/target_local are close to eachother before arming.  
On top of that, the default velocity setpoints sent are including the local_position/pose yaw ensuring a proper initialisation of the yaw. (It only failed if we were only sending yaw velocities)  
The safety check never triggered after ensuring that the few first setpoints contains a raw yaw.  
