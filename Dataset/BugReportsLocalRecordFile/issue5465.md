# Basic Information:
### Title:  SITL gazebo: Tools/sitl_gazebo/models/iris/iris.sdf not updated #5465 
### Issue status: Closed
### Author: julianoes
### Issue open time: Sep 7, 2016
# Report
### Report author: julianoes
### Report Time: Sep 7, 2016
### Report Content:   
The simulation in gazebo seems broken on master.  
Steps to reproduce:  
    
```bash     
 make posix gazebo        
```  
Then try to takeoff using:  
    
```bash     
 pxh> commander takeoff        
```  

# Comment
## Comment1
### Comment author: julianoes
### Comment Time: Sep 7, 2016
### Comment Content:   
Bisect points to 010c9e9  

## Comment2
### Comment author: jgoppert
### Comment Time: Sep 7, 2016
### Comment Content:   
This is odd, how did the SITL CI pass?  

## Comment3
### Comment author: bkueng
### Comment Time: Sep 7, 2016
### Comment Content:   
This works fine for me, I use gazebo 6.5.1.  

## Comment4
### Comment author: julianoes
### Comment Time: Sep 7, 2016
### Comment Content:   
It seems to be only my my Ubuntu 16.04 with gazebo7. Mac with gazebo7 is ok.  

## Comment5
### Comment author: jgoppert
### Comment Time: Sep 7, 2016
### Comment Content:   
It works fine on my ubuntu 16.04.  

## Comment6
### Comment author: LorenzMeier
### Comment Time: Sep 7, 2016
### Comment Content:   
Works fine on Mac here as well after all clean actions (make and git). I'm on stack_abstraction which is a branch addressing a few OS-specific stack size issues. It might be worthwhile for you to try as well.  

## Comment7
### Comment author: julianoes
### Comment Time: Sep 8, 2016
### Comment Content:   
Did a fresh checkout of Firmware and all is good again 😕.  

## Comment8
### Comment author: julianoes
### Comment Time: Sep 8, 2016
### Comment Content:   
The file Tools/sitl_gazebo/models/iris/iris.sdf was not re-generated/updated.  
The following resolved the problem:  
    
```bash     
 cd Tools/sitl_gazebo        
git clean -d -f -x        
```  

## Comment9
### Comment author: dagar
### Comment Time: Sep 8, 2016
### Comment Content:   
@julianoes Try make distclean next time. I use it when jumping between branches with big changes, especially when submodules have been added/deleted/url changed.  

## Comment10
### Comment author: julianoes
### Comment Time: Oct 22, 2016
### Comment Content:   
This should be fixed by PX4/PX4-SITL_gazebo-classic\\\#57, see PX4/PX4-SITL_gazebo-classic@d9b9f5b.  
