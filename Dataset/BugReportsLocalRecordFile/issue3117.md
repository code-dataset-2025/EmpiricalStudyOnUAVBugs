# Basic Information:
### Title:  Random IO mixer load error #3117 
### Issue status: Closed
### Author: AndreasAntener
### Issue open time: Nov 2, 2015
# Report
### Report author: AndreasAntener
### Report Time: Nov 2, 2015
### Report Content:   
@LorenzMeier as discussed.  This is happening on the runway_takeoff_before branch, with a mixer that has 8 channels assigned (yes we use them all ;))  
We get random mixer load errors like the following:  
    
```bash     
 gps: module found: UBX        
mixer: fmu sent: "000 0 -10000 10000        
S: 0 2 10000 10000 0 -10000 10000        
M: 1        
O00;"        
px4io mixer send error -1        
mixer: error loading mixers from /etc/mixers/AAERTWF.main.mix        
mixer: failed to load mixer        
[i] Error loading mixer: /etc/mixers/AAERTWF.main.mix         
telem> settings autosaved        
pwm: failed get disarmed values        
```  
Here's the px4io status output:  
    
```bash     
 nsh> px4io status        
px4io: loaded        
protocol 2147483648 hardware 2147483648 bootloader 2147483648 buffer 2147483648B crc 0x8000000080000000        
2147483648 controls 2147483648 actuators 2147483648 R/C inputs 2147483648 analog inputs 2147483648 relays        
2147483648 bytes free        
status 0x0000 SAFETY_SAFE RC_FAIL FMU_FAIL MIXER_FAIL ARM_NO_SYNC INIT_FAIL        
alarms 0x0000        
vservo 2147483648 mV vservo scale 2147483648        
vrssi 2147483648        
actuators 0 0 0 0 0 0 0 0        
servos 2147483648 2147483648 2147483648 2147483648 2147483648 2147483648 2147483648 2147483648        
reversed outputs: [________] trims: r:   0.0000 p:   0.0000 y:   0.0000        
0 raw R/C inputs        
R/C flags: 0x0000        
mapped R/C inputs 0x0000        
ADC inputs        
features 0x0000        
arming 0x0000 FMU_DISARMED IO_ARM_DENIED        
rates 0x80000000 default 2147483648 alt 2147483648        
debuglevel 2147483648        
controls 0: 0 0 0 0 0 0 0 0        
controls 1: 0 0 0 0 0 0 0 0        
controls 2: 0 0 0 0 0 0 0 0        
controls 3: 0 0 0 0 0 0 0 0        
input 0 min 2147483648 center 2147483648 max 2147483648 deadzone 2147483648 assigned 2147483648 options 0x0000        
input 1 min 2147483648 center 2147483648 max 2147483648 deadzone 2147483648 assigned 2147483648 options 0x0000        
input 2 min 2147483648 center 2147483648 max 2147483648 deadzone 2147483648 assigned 2147483648 options 0x0000        
input 3 min 2147483648 center 2147483648 max 2147483648 deadzone 2147483648 assigned 2147483648 options 0x0000        
input 4 min 2147483648 center 2147483648 max 2147483648 deadzone 2147483648 assigned 2147483648 options 0x0000        
input 5 min 2147483648 center 2147483648 max 2147483648 deadzone 2147483648 assigned 2147483648 options 0x0000        
input 6 min 2147483648 center 2147483648 max 2147483648 deadzone 2147483648 assigned 2147483648 options 0x0000        
input 7 min 2147483648 center 2147483648 max 2147483648 deadzone 2147483648 assigned 2147483648 options 0x0000        
input 8 min 2147483648 center 2147483648 max 2147483648 deadzone 2147483648 assigned 2147483648 options 0x0000        
input 9 min 2147483648 center 2147483648 max 2147483648 deadzone 2147483648 assigned 2147483648 options 0x0000        
input 10 min 2147483648 center 2147483648 max 2147483648 deadzone 2147483648 assigned 2147483648 options 0x0000        
input 11 min 2147483648 center 2147483648 max 2147483648 deadzone 2147483648 assigned 2147483648 options 0x0000        
input 12 min 2147483648 center 2147483648 max 2147483648 deadzone 2147483648 assigned 2147483648 options 0x0000        
input 13 min 2147483648 center 2147483648 max 2147483648 deadzone 2147483648 assigned 2147483648 options 0x0000        
input 14 min 2147483648 center 2147483648 max 2147483648 deadzone 2147483648 assigned 2147483648 options 0x0000        
input 15 min 2147483648 center 2147483648 max 2147483648 deadzone 2147483648 assigned 2147483648 options 0x0000        
input 16 min 2147483648 center 2147483648 max 2147483648 deadzone 2147483648 assigned 2147483648 options 0x0000        
input 17 min 2147483648 center 2147483648 max 2147483648 deadzone 2147483648 assigned 2147483648 options 0x0000        
failsafe 2147483648 2147483648 2147483648 2147483648 2147483648 2147483648 2147483648 2147483648        
disarmed values 2147483648 2147483648 2147483648 2147483648 2147483648 2147483648 2147483648 2147483648        
```  

# Comment
## Comment1
### Comment author: AndreasAntener
### Comment Time: Nov 2, 2015
### Comment Content:   
Heres the mixer btw: https://github.com/PX4/Firmware/blob/b16ae5a94992f2c840de7f30b849a05121bb1ebb/ROMFS/px4fmu_common/mixers/AAVVTWFF.main.mix  

## Comment2
### Comment author: AndreasAntener
### Comment Time: Nov 2, 2015
### Comment Content:   
I took the last 2 lines (flaps) out of the mixer now, still the same issue.  

## Comment3
### Comment author: AndreasAntener
### Comment Time: Nov 2, 2015
### Comment Content:   
Reduced the mixer to the first two outputs only now, same problem.  

## Comment4
### Comment author: LorenzMeier
### Comment Time: Nov 2, 2015
### Comment Content:   
Can you boot with the safety switch held down once to force an upgrade?  

## Comment5
### Comment author: AndreasAntener
### Comment Time: Nov 2, 2015
### Comment Content:   
Tried that in the beginning, it didn't help  

## Comment6
### Comment author: AndreasAntener
### Comment Time: Nov 2, 2015
### Comment Content:   
With nothing on the pins I had 20 successful boots. As soon as I have the receiver (no bec) plugged in it happens again after a few tries  

## Comment7
### Comment author: LorenzMeier
### Comment Time: Nov 2, 2015
### Comment Content:   
So the receiver has nothing connected to it, right?  

## Comment8
### Comment author: AndreasAntener
### Comment Time: Nov 2, 2015
### Comment Content:   
No  

## Comment9
### Comment author: LorenzMeier
### Comment Time: Nov 2, 2015
### Comment Content:   
Odd. It would be great if you could take a servo extension and cut the signal wire to see if that does anything.  

## Comment10
### Comment author: AndreasAntener
### Comment Time: Nov 2, 2015
### Comment Content:   
Hm, doesn't seem to happen anymore without the signal pin. It is an FrSky, sbus  

## Comment11
### Comment author: AndreasAntener
### Comment Time: Nov 2, 2015
### Comment Content:   
Ok, it just failed as well with a Graupner receiver, PPM.  

## Comment12
### Comment author: AndreasAntener
### Comment Time: Nov 2, 2015
### Comment Content:   
I'm on the full mixer again, everything wired up again (graupner ppm). It happens still but it seems less frequent. We also have one dead servo now, although that could have been a mechanical issue too.  

## Comment13
### Comment author: LorenzMeier
### Comment Time: Nov 2, 2015
### Comment Content:   
I would advise against flying that setup. There is something fundamentally wrong with the setup or you hit a completely unknown corner case.  

## Comment14
### Comment author: AndreasAntener
### Comment Time: Nov 2, 2015
### Comment Content:   
Here's an IO status when it's working btw  
    
```bash     
 nsh> px4io status        
px4io: loaded        
protocol 4 hardware 2 bootloader 3 buffer 64B crc 0x18000dc1        
8 controls 8 actuators 18 R/C inputs 2 analog inputs 0 relays        
600 bytes free        
status 0x374d OUTPUTS_ARMED SAFETY_OFF RC_OK PPM FMU_OK MIXER_OK ARM_SYNC INIT_OK        
alarms 0x0030 FMU_LOST RC_LOST        
vservo 5177 mV vservo scale 10000        
vrssi 1695        
actuators 0 0 0 0 0 0 0 0        
servos 1500 1500 1500 1500 1000 1500 1500 1500        
reversed outputs: [________] trims: r:   0.0000 p:   0.0000 y:   0.0000        
12 raw R/C inputs 1098 1441 1487 1534 1105 1105 1105 1105 1105 1657 1506 1505        
R/C flags: 0x0018 MAPPING_OK        
RC data (PPM frame len) 30003 us        
mapped R/C inputs 0x004f 0:0 1:0 2:0 3:0 6:-10000        
ADC inputs 2133 2075        
features 0x0008 RSSI_ADC        
arming 0x0035 FMU_DISARMED IO_ARM_OK MANUAL_OVERRIDE_OK INAIR_RESTART_OK ALWAYS_PWM_ENABLE        
rates 0x0000 default 50 alt 200        
debuglevel 0        
controls 0: 0 0 0 0 0 0 0 0        
controls 1: 0 0 0 0 0 0 0 0        
controls 2: 0 0 0 0 0 0 0 0        
controls 3: 0 0 0 0 -10000 0 -10000 0        
input 0 min 1098 center 1098 max 1891 deadzone 10 assigned 3 options 0x0001 ENABLED        
input 1 min 1105 center 1441 max 1836 deadzone 10 assigned 0 options 0x0003 ENABLED REVERSED        
input 2 min 1105 center 1488 max 1886 deadzone 10 assigned 1 options 0x0001 ENABLED        
input 3 min 1142 center 1533 max 1905 deadzone 10 assigned 2 options 0x0003 ENABLED REVERSED        
input 4 min 1000 center 1500 max 2000 deadzone 10 assigned 100 options 0x0001 ENABLED        
input 5 min 1000 center 1500 max 2000 deadzone 10 assigned 255 options 0x0000        
input 6 min 1000 center 1500 max 2000 deadzone 10 assigned 255 options 0x0000        
input 7 min 1000 center 1500 max 2000 deadzone 10 assigned 255 options 0x0000        
input 8 min 1150 center 1501 max 1900 deadzone 0 assigned 6 options 0x0001 ENABLED        
input 9 min 1105 center 1505 max 1905 deadzone 0 assigned 255 options 0x0000        
input 10 min 1000 center 1500 max 2000 deadzone 0 assigned 255 options 0x0000        
input 11 min 1000 center 1500 max 2000 deadzone 0 assigned 255 options 0x0000        
input 12 min 1000 center 1500 max 2000 deadzone 0 assigned 255 options 0x0000        
input 13 min 1000 center 1500 max 2000 deadzone 0 assigned 255 options 0x0000        
input 14 min 1000 center 1500 max 2000 deadzone 0 assigned 255 options 0x0000        
input 15 min 1000 center 1500 max 2000 deadzone 0 assigned 255 options 0x0000        
input 16 min 1000 center 1500 max 2000 deadzone 0 assigned 255 options 0x0000        
input 17 min 1000 center 1500 max 2000 deadzone 0 assigned 255 options 0x0000        
failsafe 1500 1500 1500 1500 900 1500 1500 1500        
disarmed values 0 0 0 0 1000 0 0 0        
nsh>         
```  

## Comment15
### Comment author: LorenzMeier
### Comment Time: Nov 2, 2015
### Comment Content:   
I can't make sense of it yet. Can you make it go bad if you attach the RC receiver after boot? Or is it a weird on-boot condition?  

## Comment16
### Comment author: AndreasAntener
### Comment Time: Nov 2, 2015
### Comment Content:   
It's a weird on-boot condition. Although I haven't tried booting and then connecting the receiver  

## Comment17
### Comment author: LorenzMeier
### Comment Time: Nov 2, 2015
### Comment Content:   
I pulled my hair out on this one but I have no idea what this could be. If you could provide instructions and a photograph how to repro Roman and I will start to look at it.  

## Comment18
### Comment author: AndreasAntener
### Comment Time: Nov 3, 2015
### Comment Content:   
When I was pulling everything out to find the error, I was still able to reproduce it with a minimal setup:  
- pixhawk  
- buzzer  
- safety switch  
- power module (8S and 4S)  
- frsky accst receiver via sbus  
- gps  
- i2c with airspeed and external mag  
- empty sd card  
- NO servos, NO bec, NO telemetry radio  
Note: when I was trying to find the troublemaker I also unplugged GPS and I2C and it still occurred, so these are probably not the problem nor necessary to repro. But in the receiver only tests I had them on.  
Then:    
Flashed the runway branch with startup 2106 (pushed yesterday). Everything calibrated. Then I just re-plugged the battery many times. Sometimes I also disabled safety in between (to check if that had an effect, found no pattern). It took 10 to 20 reboots until it happened again.  
With everything on the pins connected (7 servos, one ESC) it seemed to happen more often but I'm not certain.  

## Comment19
### Comment author: LorenzMeier
### Comment Time: Nov 3, 2015
### Comment Content:   
What is the particular FrSky receiver type?  

## Comment20
### Comment author: AndreasAntener
### Comment Time: Nov 3, 2015
### Comment Content:   
Uh, the one that comes with the Taranis 9XD  

## Comment21
### Comment author: AndreasAntener
### Comment Time: Nov 3, 2015
### Comment Content:   
I think Frsky X8R-XP  

## Comment22
### Comment author: RomanBapst
### Comment Time: Nov 6, 2015
### Comment Content:   
Fixed in \\\#3126  
