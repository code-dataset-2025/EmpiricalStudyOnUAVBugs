# Basic Information:
### Title:  catkin build fails -- Fails to find headers from ecl/ #9554 
### Issue status: Closed
### Author: ana-GT
### Issue open time: May 28, 2018
# Report
### Report author: ana-GT
### Report Time: May 28, 2018
### Report Content:   
Describe the bug    
Compiling Firmware as a ROS package using catkin build fails, due to catkin not finding headers located in the src/lib/ecl/ folder.  
Firmware itself builds fine when I use standard: mkdir build && cd build && cmake .. && make. I used this approach when first trying out the PX4/Firmware software, but now I was going to proceed to use ROS, so I wanted to build the PX4/Firmware as a ROS package.  
To Reproduce    
Steps to reproduce the behavior:    
0. Clone Firmware inside your ros_workspace/src folder (master branch)  
1.Build the package: cd ros_workspace/src && catkin build px4  
2.Build fails with messages of the type: "Cannot find ecl.h, not such file or directory"  
PS.- FYI, I just tried building (catkin build) the Firmware version v1.7.3 and that works fine (I still have to test some launch files, but at least the ROS package compiling finished successfully). I'll report if this version works fine, since that might mean that the compilation error might have been introduced between then and the current master.  

# Comment
## Comment1
### Comment author: dagar
### Comment Time: May 29, 2018
### Comment Content:   
@TSC21 could you add a basic catkin build to Jenkins?  
Anything we want to keep working needs to be included in CI.  
@lamping7 FYI  

## Comment2
### Comment author: TSC21
### Comment Time: May 29, 2018
### Comment Content:   
@dagar I will but I can't promise to have it ready this week.  

## Comment3
### Comment author: lamping7
### Comment Time: Jun 7, 2018
### Comment Content:   
Now that we're working toward a package to use for ROS sim/testing, do we want to support this additional build system? The idea is to make this more user friendly in the long run and only require building for dev purposes.  

## Comment4
### Comment author: ziggBee30
### Comment Time: Jul 17, 2018
### Comment Content:   
Any conclusion on this issue, its still failing for me with same error while catkin build : "Cannot find ecl.h, not such file or directory"    
Any comments ?  

## Comment5
### Comment author: mickey13
### Comment Time: Jul 17, 2018
### Comment Content:   
I've been using "v1.7.3" until this is fixed.  I'm not sure why this is closed.  

## Comment6
### Comment author: ziggBee30
### Comment Time: Jul 17, 2018
### Comment Content:   
Exactly, i am not at all able to catkin build, px4 not prepared to use catkin environment  

## Comment7
### Comment author: dagar
### Comment Time: Jul 30, 2018
### Comment Content:   
@mickey13 this isn't closed.  

## Comment8
### Comment author: dagar
### Comment Time: Jul 30, 2018
### Comment Content:   
@TSC21 @lamping7 @jgoppert has anyone looked into fixing catkin?  

## Comment9
### Comment author: dagar
### Comment Time: Jul 30, 2018
### Comment Content:   
Possible fix in \\\#9679. Could someone please test it to see if your issue is fully resolved?  

## Comment10
### Comment author: varunvp
### Comment Time: Sep 16, 2018
### Comment Content:   
How do you downgrade to Firmware v1.7.3?  

## Comment11
### Comment author: jannsta1
### Comment Time: Sep 17, 2018
### Comment Content:   
In the firmware directory you can use: $ git checkout v1.7.3.  
Hoping the issue is resolved soon as I have other incompatibilities with v1.7.3.  

## Comment12
### Comment author: mickey13
### Comment Time: Sep 17, 2018
### Comment Content:   
I ended up building a ROS node in my simulation (Gazebo) package for starting instances of the latest PX4 firmware (so that I could use the latest version in my SITL setup):  
    
```bash     
 \\\\#include <ros/ros.h>        
\\\\#include <string>        
int main(int argc, char** argv) {        
  ros::init(argc, argv, "px4_node");        
  ros::NodeHandle rosNode;        
  ros::Rate rosRate(10.0);        
  std::string executable = "${CATKIN_WS}/src/px4_firmware/build/posix_sitl_default/bin/px4";        
  std::string argFmu = "${CATKIN_WS}/src/px4_firmware/ROMFS/px4fmu_common";        
  std::string argRcS = "${CATKIN_WS}/src/px4_firmware/ROMFS/px4fmu_common/init.d-posix/rcS";        
  int argId = 0;        
  rosNode.param(ros::this_node::getName() + "/rcs", argRcS, argRcS);        
  rosNode.param(ros::this_node::getName() + "/id", argId, argId);        
  std::string command = executable + " " + argFmu + " -s " + argRcS + " -i " + std::to_string(argId) + " -d";        
  system(command.c_str());        
  while (rosNode.ok()) {        
    ros::spinOnce();        
    rosRate.sleep();        
  }        
  return 0;        
}        
```  
Note you'll want to blacklist building this with catkin:  
    
```bash     
 cd $CATKIN_WS        
catkin config --blacklist px4        
cd $CATKIN_WS/src/px4_firmware        
make        
cd $CATKIN_WS        
```  
This is just a workaround that I'm using until this issue is resolved.  

## Comment13
### Comment author: lamping7
### Comment Time: Sep 17, 2018
### Comment Content:   
What is the motivation for tightly-coupling PX4 within your ROS environment? I don't see an advantage to do this. This build system isn't actively supported for this project. Use PX4 as an independent node, launch with roslaunch, and build with the supported system. Is there a problem with the standard approach?  

## Comment14
### Comment author: mickey13
### Comment Time: Sep 17, 2018
### Comment Content:   
My requirement (and I believe it's the same for others) is that I want to be able to run PX4 instances from my ROS workspace for each modeled UAV in my simulation environment.  I don't consider that requirement "tightly-coupling PX4 within your ROS environment", as I include other non-PX4 packages via wstool and build them with catkin.  
Since PX4 cannot be built with catkin any longer, nor is there a ROS package that can be downloaded, it's not obvious how to start PX4 processes in a standard simulation environment that uses ROS (i.e. you can't roscd into px4).  What the node I mentioned above does is starts up a PX4 process so you can connect to it via MAVROS for any UAVs in your simulation environment.  

## Comment15
### Comment author: lamping7
### Comment Time: Sep 17, 2018
### Comment Content:   
    
you can't roscd into px4    
You sure can!  
You just don't have your environment setup as described by the docs.  

## Comment16
### Comment author: lamping7
### Comment Time: Sep 17, 2018
### Comment Content:   
Thumb down because why? You haven't displayed a need for this and you're just wrong.  
See the image (v1.8.0 checkout):    
It's completely obvious how to start the firmware if you read the docs.  

## Comment17
### Comment author: TSC21
### Comment Time: Sep 30, 2018
### Comment Content:   
Fixed in \\\#10587.  

## Comment18
### Comment author: incebellipipo
### Comment Time: Nov 15, 2018
### Comment Content:   
Ladies and gentleman, i didn't want to upset you, but issue persist in version 1.8.1  
Ros version: Kinetic    
Linux Distro: Linux Mint 18.3 (Based on Ubuntu 16.04.5)    
gcc: (Ubuntu 5.4.0-6ubuntu1~16.04.10) 5.4.0 20160609  
To generate error:  
    
```bash     
 \\\\\# create tmp workspace      
mkdir -p ~/tmp_ws/src      
cd ~/tmp_ws/src      
\\\\\# clone px4 source      
git clone git clone https://github.com/PX4/Firmware.git      
cd ~/tmp_ws/src/Firmware      
\\\\\# check out to version 1.8.1      
git checkout v1.8.1      
\\\\\# rest should be familiar      
git submodule update --init --recursive      
cd ~/tmp_ws/      
catkin_make    
```  
Here you are, error output:    
Edit:    
I rollback to version v1.7.3 . Problem is gone.  

## Comment19
### Comment author: dagar
### Comment Time: Nov 15, 2018
### Comment Content:   
@incebellipipo the issue is fixed in PX4 master (what will be v1.9.0).  
