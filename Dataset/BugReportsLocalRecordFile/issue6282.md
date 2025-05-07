# Basic Information:
### Title:  EKF2 flow integration_timespan check is invalid #6282 
### Issue status: Closed
### Author: svpcom
### Issue open time: Jan 9, 2017
# Report
### Report author: svpcom
### Report Time: Jan 9, 2017
### Report Content:   
I've debug why ekf2 refuses flow measurements (using gazebo sitl) and found that we have:  
in LPE: src/modules/local_position_estimator/sensors/flow.cpp  
    
```bash     
  float dt_flow = _sub_flow.get().integration_timespan / 1.0e6f;        
        if (dt_flow > 0.5f || dt_flow < 1.0e-6f) {        
                return -1;        
        }        
```  
in EKF2: src/lib/ecl/EKF/estimator_interface.cpp  
    
```bash     
       float delta_time = 1e-6f * (float)flow->dt;        
      bool delta_time_good = (delta_time >= 0.05f);        
```  
I think the check condition should be inverted in case of EKF2  

# Comment
## Comment1
### Comment author: ChristophTobler
### Comment Time: Jan 10, 2017
### Comment Content:   
@svpcom That's correct. I already asked @priseborough about that. The real PX4Flow sends flow messages at ~20fps, but the simulations runs at 100Hz. Not sure why the ekf limits the rate  

## Comment2
### Comment author: priseborough
### Comment Time: Jan 10, 2017
### Comment Content:   
The EKF limits the rate for a number of reasons:  
1.The data buffers used to time align data can only reliably handle data at rates of 20Hz or lower. We can increase the buffer size to handle higher rates, but  that causes problems with some processors that are low on RAM.  
2.Optical flow fusion is a more expensive operation than GPS fusion and reducing the fusion rate helps lower power processors.  
3.Due to the integration between samples, reducing the rate to 20Hz does not hurt performance for the yaw rates typical of optical flow operation.  

## Comment3
### Comment author: jgoppert
### Comment Time: Jan 11, 2017
### Comment Content:   
With the modified px4flow firmware in my PR I stabilize the flow output rate using a param to 10 hz. It is helpful for this.  
@ChristophTobler if you get a chance, take a look at the PR. I'd like to get this merged. I've had many users confirm as well as via my own testing that it is more robust indoors and outdoors.  
PX4/PX4-Flow\\\#86  
https://github.com/PX4/Flow/pull/86/files\\\#diff-7624ab7c53eb9962990d9668d74d8608R198  

## Comment4
### Comment author: ChristophTobler
### Comment Time: Jan 11, 2017
### Comment Content:   
@priseborough Ok, that makes sense. So I will adapt the way the optical flow messages get published. It will still use full fps but integrate over several frames and only publish at arount 10-20Hz.  
@jgoppert I will take a look at it. But I need to build a new PX4Flow quad setup first.  

## Comment5
### Comment author: svpcom
### Comment Time: Jan 11, 2017
### Comment Content:   
@priseborough But now if we submit flow measurements with rate > 20Hz (for example 20.001Hz) we don't got any errors or warnings but instead all measurements will be silently ignored. I think we need to add some error reporting and add some guard interval to prevent occasional message drop due to flow rate fluctuations.  

## Comment6
### Comment author: svpcom
### Comment Time: Jan 11, 2017
### Comment Content:   
@jgoppert Also with EKF2 + flow and without gps copter unable to takeoff (due to unfocused sensor). I think we need add the same workaround as LPE does.  

## Comment7
### Comment author: priseborough
### Comment Time: Jan 11, 2017
### Comment Content:   
It won't ignore all messages, just the ones arriving sooner than the minimum allowed interval.  

## Comment8
### Comment author: svpcom
### Comment Time: Jan 11, 2017
### Comment Content:   
In case of SITL (100Hz flow), all flow messages was silently ignored. Because flow->dt is optical_flow.integration_timespan which is a constant  

## Comment9
### Comment author: ChristophTobler
### Comment Time: Jan 11, 2017
### Comment Content:   
@svpcom it is not able to takeoff in the simulation or in real life? Because in the simulation it is  

## Comment10
### Comment author: svpcom
### Comment Time: Jan 11, 2017
### Comment Content:   
In simulation (EKF2). With EKF2_AID_MASK 2 (flow on, gps off) it unable to takeoff.  

## Comment11
### Comment author: ChristophTobler
### Comment Time: Jan 11, 2017
### Comment Content:   
@svpcom yes that's the default setting for the ekf2 flow simulation and commander takeoff works just fine for me (with the rate adaption in the ekf flow update)  

## Comment12
### Comment author: svpcom
### Comment Time: Jan 11, 2017
### Comment Content:   
@ChristophTobler    
px4 master (48e7c78)  
make posix_sitl_ekf2 gazebo_iris_opt_flow  
    
```bash     
 Number of good matches: 2, desired: 30        
INFO  [simulator] Got initial simuation data, running sim..        
INFO  [pwm_out_sim] MODE_8PWM        
Sleeping for 1 s; (1000000 us).        
INFO  [lib__ecl] EKF IMU buffer length = 21        
INFO  [lib__ecl] EKF observation buffer length = 16        
INFO  [mavlink] mode: Normal, data rate: 4000000 B/s on udp port 14556 remote port 14550        
INFO  [mavlink] mode: Onboard, data rate: 4000000 B/s on udp port 14557 remote port 14540        
INFO  [mavlink] MAVLink only on localhost (set param MAV_BROADCAST = 1 to enable network)        
pxh> INFO  [logger] logger started (mode=all)        
INFO  [logger] Start file log        
INFO  [logger] Opened log file: rootfs/fs/microsd/log/2017-01-11/16_10_33.ulg        
INFO  [tone_alarm] startup        
INFO  [lib__ecl] EKF using range finder height - commencing alignment        
INFO  [lib__ecl] EKF alignment complete        
pxh>         
pxh>         
pxh> commander takeoff        
WARN  [commander] rejecting takeoff, no position lock yet. Please retry..        
pxh> [Wrn] [Publisher.cc:141] Queue limit reached for topic /gazebo/default/pose/local/info, deleting message. This warning        
pxh> param show EKF2_AID_MASK        
Symbols: x = used, + = saved, * = unsaved        
x + EKF2_AID_MASK [125,154] : 2        
 928 parameters total, 494 used.        
```  

## Comment13
### Comment author: priseborough
### Comment Time: Jan 11, 2017
### Comment Content:   
The rate at which the ekf2 can accept observations, which sets the size of the buffers, is controlled by the EKF2_MIN_OBS_DT parameter. From memory it is defaulted to 20msec (50Hz) in master.  

## Comment14
### Comment author: ChristophTobler
### Comment Time: Jan 11, 2017
### Comment Content:   
@svpcom Just to make sure: You have changed the lines you mentioned in your issue? But once you takeoff manually position control works?  

## Comment15
### Comment author: svpcom
### Comment Time: Jan 11, 2017
### Comment Content:   
@ChristophTobler Yes. I've removed check for 20Hz in EstimatorInterface::setOpticalFlowData and POSCTL became works after manual takeoff.  

## Comment16
### Comment author: svpcom
### Comment Time: Jan 11, 2017
### Comment Content:   
@priseborough EKF2_MIN_OBS_DT is used only for magnetometer and altimeter. In case of flow data it supplied to EKF2 anyway and rejected in  EstimatorInterface::setOpticalFlowData by hardcoded delta_time < 0.05 check  

## Comment17
### Comment author: priseborough
### Comment Time: Jan 11, 2017
### Comment Content:   
@svpcom That is incorrect.  
The optical flow max acceptance rate is set by _min_obs_interval_us.  
_min_obs_interval_us is set by _obs_buffer_length.  
_obs_buffer_length is set by EKF2_MIN_OBS_DT and the maximum of the various observation time delay parameters.  

## Comment18
### Comment author: svpcom
### Comment Time: Jan 11, 2017
### Comment Content:   
@priseborough There are a second check which hardcode 20Hz (see code below)  
EstimatorInterface::setOpticalFlowData  
    
```bash     
       // limit data rate to prevent data being lost        
        if (time_usec - _time_last_optflow > _min_obs_interval_us) {        
                // check if enough integration time        
                float delta_time = 1e-6f * (float)flow->dt;        
                bool delta_time_good = (delta_time >= 0.05f);        
...        
           if (delta_time_good && flow_magnitude_good && flow_quality_good) {        
...        
              _flow_buffer.push(optflow_sample_new);        
...        
           }        
        }        
```  

## Comment19
### Comment author: ChristophTobler
### Comment Time: Jan 12, 2017
### Comment Content:   
@svpcom Yes there are two hard coded checks. You mentioned two files in the in the issue so en figured you had them both, my fault... So now that you changed these two checks, I guess commander takeoffworks?  

## Comment20
### Comment author: ChristophTobler
### Comment Time: Jan 12, 2017
### Comment Content:   
@svpcom I checked the simulation again and if you change https://github.com/PX4/ecl/blob/master/EKF/control.cpp\\\#L249 as well commander takeoff will work (I had both of them changed from the beginning).  
@priseborough Maybe it would be good to use parameters instead of hard coded 0.05f in https://github.com/PX4/ecl/blob/master/EKF/estimator_interface.cpp\\\#L283 and https://github.com/PX4/ecl/blob/master/EKF/control.cpp\\\#L249?  
For the flow calculation in the simulation: I'm adding a parameter to set the ouput rate of the flow. I guess a range between 5Hz and 20Hz would be good?  

## Comment21
### Comment author: LorenzMeier
### Comment Time: Jan 12, 2017
### Comment Content:   
I think the discussion is conclusive, can we move on to a proper and complete fix?  

## Comment22
### Comment author: ChristophTobler
### Comment Time: Jan 12, 2017
### Comment Content:   
As I suggested:  
- set flow ouput rate: update submodule and adaptions for it PX4-SITL_gazebo-classic\\\\\#79 will lower the ouput rate of the flow so it will work with the ekf2 and hard coded limits  
- Still I don't think that these limits should be hard coded and if so, it should be clearly stated in the dev guide  
- We might have to come up with a solution for taking off in flow mode  

## Comment23
### Comment author: svpcom
### Comment Time: Jan 13, 2017
### Comment Content:   
@ChristophTobler @priseborough  With commit 967197a flow became works, but only to first flow focus lost (for example flight out of asphalt texture). When I came back to textured field I'm unable to switch to POSCTL mode.  Flow data is good:  
    
```bash     
 delta_time 0.053213 is good: 1, flow mag: 0.025434 is good: 1, flow qual: 153.000000 is good: 1        
delta_time 0.052794 is good: 1, flow mag: 0.025106 is good: 1, flow qual: 185.000000 is good: 1        
delta_time 0.060996 is good: 1, flow mag: 0.022210 is good: 1, flow qual: 159.000000 is good: 1        
delta_time 0.051348 is good: 1, flow mag: 0.025605 is good: 1, flow qual: 185.000000 is good: 1        
delta_time 0.074743 is good: 1, flow mag: 0.024073 is good: 1, flow qual: 170.000000 is good: 1        
delta_time 0.056513 is good: 1, flow mag: 0.023177 is good: 1, flow qual: 185.000000 is good: 1        
```  
so it seems that something is broken in EKF2.  
How to reproduce:  
1.make posix_sitl_ekf2 gazebo_iris_opt_flow  
2.Switch to ALTCTL  
3.ARM and takeoff to 3m using joystick.  
4.Switch to POSCTL.  
5.move outside asphalt texture. Mode will failback to ALTCTL.  
6.Move back to textured zone.  
7.Try to switch to POSCTL -> unable to switch.  

## Comment24
### Comment author: ChristophTobler
### Comment Time: Jan 16, 2017
### Comment Content:   
I think we can close this since the actual issue is fixed. Overview on exsting issues in \\\#6347 (comment)  

## Comment25
### Comment author: LorenzMeier
### Comment Time: Jan 17, 2017
### Comment Content:   
@priseborough For sierra, try this:  
\\\#6360  
    
```bash     
 brew uninstall gazebo7        
brew untap osrf/simulation        
brew tap px4/simulation        
brew install gazebo7        
```  
