# Basic Information:
### Title:  Motor spinning on USB power reset #7457 
### Issue status: Closed
### Author: lericson
### Issue open time: Jun 22, 2017
# Report
### Report author: lericson
### Report Time: Jun 22, 2017
### Report Content:   
Despite the fixes in \\\#7123, we still get motors spinning on unplugging the USB cable.  
Steps to reproduce:  
1.Plug in battery, USB cable  
2.Start QGroundControl  
3.Unplug USB cable  
It only happens if QGroundControl has been talking to the PX4, as this triggers USB telemetry boolean that actually makes the PX4 reset after USB has been unplugged.  
I have looked at the PWM signal with an oscilloscope and have pictures of it, but they aren't very telling.  
Workaround:    
In src/modules/commander/commander.cpp, find the usleep() just before the reboot and put board_on_reset(0); before the sleep. This sets all PWMs to zero.  
A better long term fix would be to add a sleep to the board_on_reset.  

# Comment
## Comment1
### Comment author: lericson
### Comment Time: Jun 22, 2017
### Comment Content:   
We have the PixRacer hardware version 4, by the way.  

## Comment2
### Comment author: davids5
### Comment Time: Jun 22, 2017
### Comment Content:   
@lericson - Thank you for reporting this. Please test \\\#7459  
For a faster test cycle time: A reboot command on the debug port will also trigger the spin.    
It is tricky to catch. The asynchronous reset has to occur when the PWM pins are high. So more testing is better, testing with a logic analyzer with analog, is the best way to see the fix is solid.  
On the HW I tested the discharge rate was fast enough. I had assumed that is not the same on all HW and had the hook in place just incase. The PR use it.  

## Comment3
### Comment author: lericson
### Comment Time: Jun 22, 2017
### Comment Content:   
It happens very consistently for us. Will try the PR on Monday, thanks! I had tried usleep at the same location but it didn't work -- might've been to short an interval too.  

## Comment4
### Comment author: davids5
### Comment Time: Jun 22, 2017
### Comment Content:   
@lericson    
Thank you! Please let me know how the testing goes. I may also need more details the proposed fix you have and the HW attached.  

## Comment5
### Comment author: ndepal
### Comment Time: Jun 27, 2017
### Comment Content:   
Just happened to me as well with a PixRacer on master ca480ff.  

## Comment6
### Comment author: davids5
### Comment Time: Jun 27, 2017
### Comment Content:   
@ndepal Would you please test \\\#7459 and see if it stops the issue.  

## Comment7
### Comment author: ndepal
### Comment Time: Jun 27, 2017
### Comment Content:   
Just tested \\\#7459, it does not fix the issue.  

## Comment8
### Comment author: davids5
### Comment Time: Jun 27, 2017
### Comment Content:   
@ndepal would you be able to do a few more tests?  
1.Comment out the usleep found here  
Does the motors still spin?  
2.Add the sleep back in as usleep(10000)  
Does the motors still spin?  
These are just tests to try to understand where the PWM is getting stretched.  

## Comment9
### Comment author: ndepal
### Comment Time: Jun 28, 2017
### Comment Content:   
Tested as requested.  
1.motors still spin  
2.motors still spin  

## Comment10
### Comment author: davids5
### Comment Time: Jun 28, 2017
### Comment Content:   
@ndepal Thank you for testing.  
Would you mind one more test?  
Do as @lericson suggested place the  board_on_reset(0); call prior to this line  
I will need to duplicate your setup. Please list what you have connected to the PixRacer and on what connector. Part number or links would be appreciated.  

## Comment11
### Comment author: ndepal
### Comment Time: Jun 29, 2017
### Comment Content:   
board_on_reset(0); fixes the problem for me, but only with a long enough sleep afterwards. I did not get spinning motors with usleep(300000); or above, but I did with usleep(200000); and below.  
My setup:    
Pixracer from auav.co    
ESCs: Favourite Little Bee 30A    
Motors: Emax cooling MT2206 II 1900KV    
nothing else attached for these tests.  

## Comment12
### Comment author: davids5
### Comment Time: Jun 29, 2017
### Comment Content:   
@ndepal Thank you that is super helpful. I think I understand what is happening. See 0484ee3 for the details. I have updated \\\#7459. would you please fetch it again and test it with no other modification.  

## Comment13
### Comment author: ndepal
### Comment Time: Jun 29, 2017
### Comment Content:   
Pulled and re-tested \\\#7459, the issue is fixed for me.  

## Comment14
### Comment author: davids5
### Comment Time: Jun 29, 2017
### Comment Content:   
@ndepal - thank you!  
@lericson  I have updated \\\#7459. would you please fetch it again and test it with no other modification.  

## Comment15
### Comment author: LorenzMeier
### Comment Time: Jul 9, 2017
### Comment Content:   
Should be fixed.  

## Comment16
### Comment author: lericson
### Comment Time: Jul 17, 2017
### Comment Content:   
Can confirm it no longer happens. On a related note, we got the living crap scared out of us when our hexacopter started running its rotors full speed due to this. It even took off from the desk where it was seated, and not on USB reset either -- just a reboot command.  
