# Basic Information:
### Title:  Streaming identical messages #9841 
### Issue status: Closed
### Author: superware
### Issue open time: Jul 5, 2018
### Fixed by: #9903
# Report
### Report author: superware
### Report Time: Jul 5, 2018
### Report Content:   
Describe the bug    
Some messages are not streamed if nothing has changed in their data.  
To Reproduce    
Steps to reproduce the behavior:  
1.Monitor the sending of POSITION_TARGET_GLOBAL_INT, see only a single packet per change.  
Expected behavior    
Most scenarios use unreliable wireless communication, it's unacceptable to expect a single packet to always arrive to the GCS.  
See this commit, @dagar  

# Comment
## Comment1
### Comment author: dagar
### Comment Time: Jul 13, 2018
### Comment Content:   
In most cases this is a good mechanism for limiting irrelevant data from being published over a limited data link. We don't want mavlink publishing POSITION_TARGET_GLOBAL_INT if you're not in a mode that has one.  
Here we could combine it with another publication to get the behaviour you want.  

## Comment2
### Comment author: superware
### Comment Time: Jul 17, 2018
### Comment Content:   
@dagar,  
1."a good mechanism for limiting irrelevant data from being published over a limited data link", but still, that limited data link MUST have enough bandwidth to continuously transport ALL streams at their defined rates. How will limiting a low-rate stream message change that?  
2.These limited data links are often wireless and unreliable, it might be catastrophic if the GCS will not know the current global targets just because the link failed to transport a single packet??  
Thanks.  

## Comment3
### Comment author: dagar
### Comment Time: Jul 17, 2018
### Comment Content:   
1.    
There definitely isn't enough bandwidth to continuously transport ALL streams at their defined rates in most cases. Check mavlink status. On most serial links the transmit rates are automatically scaled back.    
2.    
I would reevaluate areas of the mavlink spec where you consider missing messages to be catastrophic. We have acknowledgements and retry logic that could be applied.    
