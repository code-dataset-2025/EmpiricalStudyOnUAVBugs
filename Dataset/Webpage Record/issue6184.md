# Basic Information:
### Title:  Pixracer has incorrect gyro device ID on some sensor_gyro messages #6184 
### Issue status: Closed
### Author: priseborough
### Issue open time: Dec 27, 2016
# Report
### Report author: priseborough
### Report Time: Dec 27, 2016
### Report Content:   
Description  
Whilst testing a prototype IMU thermal compensation algorithm here: https://github.com/priseborough/Firmware/tree/sensor_correction-wip  
It was noticed that the sensor_correction message occasionally contained an invalid device ID value for the voted gyro when displayed over the nsh console using the listener app . Further investigation using both the sensor_correction-wip branch and origin/master at 3a17c07 showed that the sensor_gyro topic regularly displayed invalid values for device_id.  
Steps to reproduce  
1.build and load upstream master onto the pixracer:  
git fetch origin    
git checkout master    
git reset --hard origin/master    
make distclean    
make px4fmu-v4_default upload  
2.    
Connect the debug cable to the serial port and establish an nsh console connection using a serial terminal.    
3.    
Repeatedly enter 'listener sensor_gyro'    
Note the value of device_id. It should be the ID for the ICM-20608 or the MPU9250 gyro. Occasionally it returns a random integer.  

# Comment
## Comment1
### Comment author: LorenzMeier
### Comment Time: Dec 27, 2016
### Comment Content:   
@priseborough Its not really a bug but merely not implemented. We do not use that field on NuttX yet (but we plan to as part of the system evolution). I can add tomorrow code into the drivers to fill it. Please hack around it in the meanwhile.  

## Comment2
### Comment author: mhkabir
### Comment Time: Apr 3, 2017
### Comment Content:   
@LorenzMeier @priseborough Does this still affect us?  

## Comment3
### Comment author: priseborough
### Comment Time: Apr 3, 2017
### Comment Content:   
I've checked the sensor_gyro and sensor_accel topics on a pixracer using the nsh listenerand they now contain consistent sensor ID's.  
