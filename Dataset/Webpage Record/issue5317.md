# Basic Information:
### Title:  FMU v2 no longer connecting over USB / radio telemetry  #5317 
### Issue status: Closed
### Author: sanderux
### Issue open time: Aug 14, 2016
# Report
### Report author: sanderux
### Report Time: Aug 14, 2016
### Report Content:   
Somewhere after 9f4a91a master fails to connect to QGC  

# Comment
## Comment1
### Comment author: LorenzMeier
### Comment Time: Aug 15, 2016
### Comment Content:   
Reverting this change doesn't fix it. The issue is actually a hard fault triggered in the MAVLink app:  
    
```bash     
 INFO  [mavlink] mode: Config, data rate: 8000Assertion failed at file:armv7-m/up_hardfault.c line: 184 task: mavlink_if1        
sp:     20002528        
IRQ stack:        
  base: 2000256c        
  size: 000002e8        
20002520: 2001ef28 080795ef 080a628b 000000b8 080830dd 00000010 200025b0 00000003        
20002540: 00000000 08080efd 08080ee9 08080ed5 00000000 00000000 2001eb60 2001ff70        
20002560: 00000000 080797fd 2001ea4c 00000000 10000010 00000001 00000000 00000000        
sp:     2001eb20        
User stack:        
  base: 2001ef28        
  size: 00000aec        
2001eb20: 00000000 00000000 2001ff30 00000000 0020f10c 0803c0dd 00000000 00000000        
2001eb40: 00000000 00000000 2000a3d0 2001df4c 0000260a 2001ebc8 08058615 0807a3db        
2001eb60: 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000        
2001eb80: 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000        
2001eba0: 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000        
2001ebc0: 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000        
2001ebe0: 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000        
2001ec00: 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000        
2001ec20: 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000        
2001ec40: 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000        
2001ec60: 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000        
2001ec80: 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000        
2001eca0: 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000        
2001ecc0: 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000        
2001ece0: 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000        
2001ed00: 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000        
2001ed20: 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000        
2001ed40: 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000        
2001ed60: 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000        
2001ed80: 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000        
2001eda0: 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000        
2001edc0: 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000        
2001ede0: 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000        
2001ee00: 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000        
2001ee20: 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000        
2001ee40: 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000        
2001ee60: 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000        
2001ee80: 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000        
2001eea0: 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000        
2001eec0: 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000        
2001eee0: 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000        
2001ef00: 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000        
2001ef20: 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000        
R0: 2001eb60 00000000 7323eba8 20020001 00000000 2001eb60 2001ff70 00000000        
R8: 0020f10c 00000000 2001f680 2001ecf0 08057f97 2001eb20 080395f7 080778ce        
xPSR: 81000000 BASEPRI: 00000000 CONTROL: 00000000        
EXC_RETURN: ffffffe9        
```  

## Comment2
### Comment author: LorenzMeier
### Comment Time: Aug 15, 2016
### Comment Content:   
Happening somewhere around here:  
    
```bash     
 (gdb) info line *0x080778ce        
Line 184 of "string/lib_memset.c" starts at address 0x80778ca <memset+4> and ends at 0x80778d4 <memset+14>.        
(gdb) info line *0x080395f7        
Line 93 of "../src/modules/mavlink/mavlink_orb_subscription.cpp"        
   starts at address 0x80395f6 <MavlinkOrbSubscription::update(unsigned long long*, void*)+52>        
   and ends at 0x80395fa <MavlinkOrbSubscription::update(unsigned long long*, void*)+56>.        
(gdb) info line *0x08057f97        
Line 173 of "../src/modules/uORB/uORBDevices_nuttx.cpp"        
   starts at address 0x8057f96 <uORB::DeviceNode::read(file*, char*, unsigned int)>        
   and ends at 0x8057f98 <uORB::DeviceNode::read(file*, char*, unsigned int)+2>.        
```  

## Comment3
### Comment author: LorenzMeier
### Comment Time: Aug 15, 2016
### Comment Content:   
Originating specifically here:  
    
```bash     
 (gdb) info line *0x0803c0dd        
Line 3110 of "../src/modules/mavlink/mavlink_messages.cpp"        
   starts at address 0x803c0dc <MavlinkStreamAltitude::send(unsigned long long)+48>        
   and ends at 0x803c0e2 <MavlinkStreamAltitude::send(unsigned long long)+54>.        
```  

## Comment4
### Comment author: LorenzMeier
### Comment Time: Aug 15, 2016
### Comment Content:   
Another assert:  
    
```bash     
 INFO  [mavlink] mode: Config, data rate: 800Assertion failed at file:armv7-m/up_hardfault.c line: 184 task: mavlink_if1        
sp:     20002528        
IRQ stack:        
  base: 2000256c        
  size: 000002e8        
20002520: 2001e6a8 080795ff 080a629b 000000b8 080830ed 00000010 200025b0 00000003        
20002540: 00000000 08080f0d 08080ef9 08080ee5 00000000 00000000 2001e358 2001ff80        
20002560: 00000000 0807980d 2001e264 00000000 10000010 00000001 00000000 00000000        
sp:     2001e338        
User stack:        
  base: 2001e6a8        
  size: 00000aec        
2001e320: 00000000 41845fb3 40800000 00004e20 80000010 080395e7 00000000 00000000        
2001e340: 2001ff50 00001bff 00216295 0803b907 00000000 00000000 00000000 00000000        
2001e360: 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000        
2001e380: 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000        
2001e3a0: 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000        
2001e3c0: 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000        
2001e3e0: 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000        
2001e400: 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000        
2001e420: 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000        
2001e440: 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000        
2001e460: 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000        
2001e480: 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000        
2001e4a0: 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000        
2001e4c0: 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000        
2001e4e0: 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000        
2001e500: 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000        
2001e520: 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000        
2001e540: 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000        
2001e560: 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000        
2001e580: 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000        
2001e5a0: 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000        
2001e5c0: 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000        
2001e5e0: 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000        
2001e600: 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000        
2001e620: 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000        
2001e640: 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000        
2001e660: 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000        
2001e680: 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000        
2001e6a0: 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000        
R0: 2001e358 00000000 7323e3a0 20020001 00000000 2001e358 2001ff80 00000000        
R8: 002172b4 00000000 2001fa70 2001e470 08057fa7 2001e338 080395f7 080778de        
xPSR: 81000000 BASEPRI: 00000000 CONTROL: 00000000        
EXC_RETURN: ffffffe9        
```  

## Comment5
### Comment author: LorenzMeier
### Comment Time: Aug 15, 2016
### Comment Content:   
Now it happens here:  
    
```bash     
 (gdb) info line *0x0803b907        
Line 750 of "../src/modules/mavlink/mavlink_messages.cpp"        
   starts at address 0x803b906 <MavlinkStreamHighresIMU::send(unsigned long long)+144>        
   and ends at 0x803b90e <MavlinkStreamHighresIMU::send(unsigned long long)+152>.        
```  
@bkueng This looks like a potential regression of the uORB changes. Could you please drop everything and immediately look into this, starting with an address sanitizer SITL run as described on http://dev.px4.io?  

## Comment6
### Comment author: LorenzMeier
### Comment Time: Aug 15, 2016
### Comment Content:   
One more:  
    
```bash     
 R0: b802760b 20014330 20010980 08076321 b802760b 20014334 20010980 00000000        
R8: 00000000 10004af0 00000000 00000000 00000000 20014c58 0807632f 0807dd84        
```  

## Comment7
### Comment author: LorenzMeier
### Comment Time: Aug 15, 2016
### Comment Content:   
More data:  
    
```bash     
 INFO  [mavlink] mode: Config, data rate: 800000 B/s on /Assertion failed at file:armv7-m/up_hardfault.c line: 184 task: mavlink_if1        
sp:     20002548        
IRQ stack:        
  base: 2000258c        
  size: 000002e8        
20002540: 2001ddc0 0807dadf 080aad1f 000000b8 080875cd 00000010 200025d0 00000003        
20002560: 00000000 080853ed 080853d9 080853c5 00000000 00000000 2001d990 2001ffc0        
20002580: 00000000 0807dced 2001d894 00000000 10000010 00000001 00000000 00000000        
sp:     2001d968        
User stack:        
  base: 2001ddc0        
  size: 00000894        
2001d960: 60000011 080395df 00000000 00000000 2001ff80 00000000 00229cd5 0803cc01        
2001d980: 00000000 2001fe20 0001e848 00229cd5 00000000 00000000 00000000 00000000        
2001d9a0: 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000        
2001d9c0: 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000        
2001d9e0: 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000        
2001da00: 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000        
2001da20: 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000        
2001da40: 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000        
2001da60: 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000        
2001da80: 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000        
2001daa0: 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000        
2001dac0: 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000        
2001dae0: 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000        
2001db00: 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000        
2001db20: 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000        
2001db40: 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000        
2001db60: 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000        
2001db80: 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000        
2001dba0: 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000        
2001dbc0: 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000        
2001dbe0: 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000        
2001dc00: 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000        
2001dc20: 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000        
2001dc40: 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000        
2001dc60: 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000        
2001dc80: 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000        
2001dca0: 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000        
2001dcc0: 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000        
2001dce0: 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000        
2001dd00: 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000        
2001dd20: 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000        
2001dd40: 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000        
2001dd60: 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000        
2001dd80: 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000        
2001dda0: 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000        
R0: 2001d990 00000000 7323d9d8 20020001 00000000 2001d990 2001ffc0 00000000        
R8: 00229cd5 00000000 2001a330 2001db88 0805bc47 2001d968 080395ef 0807bdba        
xPSR: 81000000 BASEPRI: 00000000 CONTROL: 00000000        
EXC_RETURN: ffffffe9        
```  
    
```bash     
 Line 93 of "../src/modules/mavlink/mavlink_orb_subscription.cpp"        
   starts at address 0x80395ee <MavlinkOrbSubscription::update(unsigned long long*, void*)+52>        
   and ends at 0x80395f2 <MavlinkOrbSubscription::update(unsigned long long*, void*)+56>.        
(gdb) info line *0x0805bc47        
Line 173 of "../src/modules/uORB/uORBDevices_nuttx.cpp"        
   starts at address 0x805bc46 <uORB::DeviceNode::read(file*, char*, unsigned int)>        
   and ends at 0x805bc48 <uORB::DeviceNode::read(file*, char*, unsigned int)+2>.        
```  

## Comment8
### Comment author: LorenzMeier
### Comment Time: Aug 15, 2016
### Comment Content:   
Now crashed in ekf2:  
    
```bash     
 Assertion failed at file:armv7-m/up_hardfault.c line: 184 task: ekf2                                                                 
sp:     20002548                                                                                                                     
IRQ stack:                                                                                                                           
  base: 2000258c                                                                                                                     
  size: 000002e8                                                                                                                     
20002540: 20015000 0807daf7 080aad57 000000b8 080875ed 00000010 200025d0 00000003                                                    
20002560: 00000000 0808540d 080853f9 080853e5 00000000 20011a50 20011b50 20014d40                                                    
20002580: 20014c98 0807dd05 200148f4 00000000 10000010 00000001 00000000 00000000                                                    
sp:     200149c8                                                                                                                     
User stack:        
  base: 20015000        
  size: 00000bb4        
200149c0: 8000001b 08045493 20014c48 00000000 0000174d 00000000 20014a08 20014a14                                            200149e0: 003a5c3a 00000000 ffffffff 000000ff 00000000 ffffffff ffffffff ffffffff                                            20014a00: ffffffff ffffffff 360417c4 b7091c33 372d71ee ba673f40 39179ac3 bd719078                                            20014a20: ffffffff ffffffff ffffffff ffffffff ffffffff ffffffff ffffffff ffffffff                                            20014a40: ffffffff ffffffff ffffffff ffffffff ffffffff ffffffff ffffffff ffffffff                                            20014a60: ffffffff ffffffff 0021bcf7 00000000 00000001 00000000 ffffffff ffffffff                                            20014a80: ffffffff ffffffff ffffffff ffffffff ffffffff ffffffff ffffffff ffffffff                                            20014aa0: ffffffff ffffffff ffffffff ffffffff ffffffff ffffffff ffffffff ffffffff                                            20014ac0: ffffffff ffffffff ffffffff ffffffff ffffffff ffffffff ffffffff ffffffff                                            20014ae0: ffffffff ffffffff ffffffff ffffffff 00000000 00000000 00000000 00000000                                            20014b00: 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000                                            20014b20: 00000000 00000000 00000000 00000000 00000003 00000000 00000101 20010a9c                                            20014b40: 00000006 00000000 00000001 20010acc ffffffff ffffffff ffffffff ffffffff                                            20014b60: ffffffff ffffffff ffffffff ffffffff ffffffff ffffffff 00000000 00000000                                            20014b80: 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000                                            20014ba0: 00000000 00000000 003859f6 00000000 00000001 00000001 00000000 00000000                                            20014bc0: 00000000 00000100 0000010d 01000100 00000000 00000000 ffffffff ffffffff                                            20014be0: ffffffff ffffffff ffffffff ffffffff ffffffff ffffffff ffffffff ffffffff                                            20014c00: ffffffff ffffffff 003a5ba9 00000000 39ad014d bab3938d 3ae32a3f 3bc3760c                                            20014c20: 00000000 be176f52 3cc68f5d c11e30f4 3bc3760c ffffe1a6 be4a258b 3e16ffff                                            20014c40: 3ea9aa9c ffffa690 43b62b06 421e9999 00000000 00000000 00000000 00000000                                            20014c60: 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000                                            20014c80: 00000000 00000000 00000000 00000000 00000000 00000000 003a5e23 00000000                                            20014ca0: 00000000 00000000 00000000 00000000 ffffffff ffffffff ffffffff ffffffff                                            20014cc0: ffffffff ffffffff ffffffff ffffffff ffffffff ffffffff ffffffff ffffffff                                            20014ce0: 0039417b 00000000 e9b1d53b 00053a18 1c3b558b 05133bac 0006a23a 00000000                                            20014d00: 41aee76d 40490fda 483434fa 47fed9e2 42c7fae1 42c7fae1 0000005f 00000010                                            20014d20: 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000                                            20014d40: 003a5e29 00000000 36513ca7 b272f9cb b718c9d6 20012478 3abd0c09 3a2f3803                                            20014d60: a8a5f328 b7a7bcd2 a480d70d 3b0570d3 b5931878 36154b12 3a2f3803 b49bb897                                            20014d80: b718c9d6 b601e496 b4badf7a a62fbb1c 32b801c9 288a15df a5f2ce6f 3293db22                                            20014da0: b55fe0b8 36a4a2c8 326cb416 b49bb897 36a4a2c8 aa9a558e ffffffff ffffffff                                            20014dc0: ffffffff ffffffff ffffffff ffffffff ffffffff ffffffff ffffffff ffffffff                                            20014de0: ffffffff ffffffff ffffffff ffffffff ffffffff ffffffff ffffffff ffffffff                                            20014e00: ffffffff ffffffff ffffffff ffffffff ffffffff ffffffff ffffffff ffffffff                                            20014e20: ffffffff ffffffff ffffffff ffffffff ffffffff ffffffff ffffffff ffffffff                                            20014e40: ffffffff ffffffff ffffffff ffffffff ffffffff ffffffff ffffffff ffffffff                                            20014e60: ffffffff ffffffff ffffffff ffffffff ffffffff ffffffff ffffffff ffffffff                                            20014e80: ffffffff ffffffff ffffffff ffffffff ffffffff ffffffff ffffffff ffffffff        
```  

## Comment9
### Comment author: LorenzMeier
### Comment Time: Aug 15, 2016
### Comment Content:   
    
```bash     
 R0: 00000000 00000000 00005e2d 2140a445 20011a50 20011b50 20014d40 20014c98                                                          
R8: 00000000 00000000 00000000 00000000 00000000 200149c8 0805be81 0804549a        
```  

## Comment10
### Comment author: LorenzMeier
### Comment Time: Aug 15, 2016
### Comment Content:   
    
```bash     
 (gdb) info line *0x0805be81        
Line 393 of "../src/modules/uORB/uORBDevices_nuttx.cpp"        
   starts at address 0x805be80 <uORB::DeviceNode::publish(orb_metadata const*, void*, void const*)+60>        
   and ends at 0x805be82 <uORB::DeviceNode::publish(orb_metadata const*, void*, void const*)+62>.        
```  

## Comment11
### Comment author: LorenzMeier
### Comment Time: Aug 15, 2016
### Comment Content:   
Looks like something is trashing the uORB data structs.  

## Comment12
### Comment author: bkueng
### Comment Time: Aug 15, 2016
### Comment Content:   
Havn't been able to reproduce this so far. address sanitizer shows nothing, valgrind shows something that could be an issue:  
    
```bash     
 ==20576== Syscall param socketcall.sendto(msg) points to uninitialised byte(s)        
==20576==    at 0x4E48363: ??? (in /usr/lib64/libpthread-2.23.so)        
==20576==    by 0x464EEB: Mavlink::send_packet() (mavlink_main.cpp:905)        
==20576==    by 0x46C951: _mav_finalize_message_chan_send (mavlink_helpers.h:347)        
==20576==    by 0x46CA3B: mavlink_msg_wind_cov_send_struct (mavlink_msg_wind_cov.h:250)        
==20576==    by 0x46CA3B: MavlinkStreamWind::send(unsigned long) (mavlink_messages.cpp:3216)        
==20576==    by 0x46F9AD: MavlinkStream::update(unsigned long) (mavlink_stream.cpp:83)        
==20576==    by 0x467229: Mavlink::task_main(int, char**) (mavlink_main.cpp:2156)        
==20576==    by 0x4676E9: Mavlink::start_helper(int, char**) (mavlink_main.cpp:2296)        
==20576==    by 0x43B58F: entry_adapter(void*) (px4_posix_tasks.cpp:108)        
==20576==    by 0x4E3F5C9: start_thread (in /usr/lib64/libpthread-2.23.so)        
==20576==    by 0x5C06EAC: clone (in /usr/lib64/libc-2.23.so)        
==20576==  Address 0x5f20c3a is 714 bytes inside a block of size 1,224 alloc'd        
==20576==    at 0x4C2C20C: operator new(unsigned long) (vg_replace_malloc.c:334)        
==20576==    by 0x4676CC: Mavlink::start_helper(int, char**) (mavlink_main.cpp:2284)        
==20576==    by 0x43B58F: entry_adapter(void*) (px4_posix_tasks.cpp:108)        
==20576==    by 0x4E3F5C9: start_thread (in /usr/lib64/libpthread-2.23.so)        
==20576==    by 0x5C06EAC: clone (in /usr/lib64/libc-2.23.so)        
```  

## Comment13
### Comment author: LorenzMeier
### Comment Time: Aug 15, 2016
### Comment Content:   
I think we also might want to run EKF2 with -Weffc++ and -Werror=uninitialized. But it'll take some work. I seem to have more crashes with a smaller EKF2 stack, although I do not see why that's related.  

## Comment14
### Comment author: LorenzMeier
### Comment Time: Aug 15, 2016
### Comment Content:   
We're hunting definitely an overflow:  
    
```bash     
 nsh> free        
             total       used       free    largest        
Mem:        180144-1241213499        800        688        
```  

## Comment15
### Comment author: bkueng
### Comment Time: Aug 15, 2016
### Comment Content:   
Did you do a git bisect?  

## Comment16
### Comment author: LorenzMeier
### Comment Time: Aug 15, 2016
### Comment Content:   
No, but I found it just now: The crashes were the result of the system running out of RAM for heap allocations. It got random memory pointers and kept using them. I'm working on a target with 50K less memory, so this is all handled. I'm adding a RAM monitor just now.  

## Comment17
### Comment author: bkueng
### Comment Time: Aug 15, 2016
### Comment Content:   
great!    
but why would it get random pointers?  

## Comment18
### Comment author: LorenzMeier
### Comment Time: Aug 15, 2016
### Comment Content:   
Because we have not solved the return value of new() yet, so the pointer will not get actually set to zero. You opened an issue a while back.  

## Comment19
### Comment author: bkueng
### Comment Time: Aug 15, 2016
### Comment Content:   
I thought the nuttx implementation just returns NULL on failure?    
You mean \\\#4493? That's something different and solved for GCC  

## Comment20
### Comment author: davids5
### Comment Time: Aug 15, 2016
### Comment Content:   
If you're getting back random values that would suggest the heap is corrupted.  

## Comment21
### Comment author: western-co-at
### Comment Time: Aug 24, 2016
### Comment Content:   
Hello    
My copter crashed with v1.4.1 during a mission flight in ekf2 today with following message:  
    
```bash     
 INFO  [commander] Takeoff detected        
WARN  [navigator] do_set_servo command        
WARN  [navigator] navigator: global position timeout        
WARN  [navigator] do_set_servo command        
WARN  [navigator]Assertion failed at file:armv7-m/up_hardfault.c line: 184 task: mavlink_if0        
sp:        
20005d20: 00000000 2000df20 00000025 00000025 00000000 080a4e0015848 000000f5 00000000 00000000 000000f5 0809f933        
20015160: 000000dc 20015718 00000000 0803f653 00000002 200152a8 080a9d45 318a318a        
20015180: 00000002 20015258 00000000 2000df20 00000025 000fa714 00000000 2000df20        
200151a0: 20011170 00000000 20011130 ffffffe9 000f837c 00000000 00000000 00000000        
200151c0: 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000        
200151e0: 00000000 00000000 00000000 00000000 20015278 00000000 2001529d 2001527d        
20015200: 200152f8 080414fb 080a143c 810000714        
20015240: 00000000 2000df20 20011170 00000000 20011130 080415d1 00000025 00000016        
20015260: 2ba904cd 00000000 3d4693d2 3d8d54e4 be85985e 3ea1716d 000b2d51 3e012d5d        
20015280: bdab1863 3c24f444 3f7d0a23 3d4693d2 3d8d54e4 be85985e 3ea273d4 00000000        
200152a0: 2ba90721 00000000 ba9c2a91 3e2c8871 4038cea9 00000000 bf74475b be808b71        
200152c0: be2683fd 3e7da4eb bf77ccde 3d27db94 be2bb7c2 ba99f46e 3f7c5fea 3e012d5e        
200152e0: bdab1864 3c24f446 3f7d0a22 00000000 00000000 00000000 00000000 3ea273d4        
20015300: 00000001 00000000 00000000 00000000 00000000 000f837c 00000000 00000000        
20015320: 00000000 00000000 00000000 2ba90904 00000000 08042bc5 00000000 00000000        
20015340: 2ba90904 00000000 2000df20 200155e0 20015390 0803c037 00000400 2000b860        
20015360: 0000e100 ffffffff 200112f0 20010fc0 ffffffff ffffffff ffff682065 0000656d 20025150 20024900 20025189 20064c10 00000000        
20015460: ffffffff ffffffff ffffffff ffffffff ffffffff ffffffff ffffffff ffffffff        
20015480: ffffffff ffffffff ffffffff ffffffff ffffffff ffffffff ffffffff ffffffff        
200154a0: ffffffff ffffffff ffffffff ffffffff ffffffff ffffffff ffffffff ffffffff        
200154c0: ffffffff ffffffff ffffffff ffffffff ffffffff ffffffff ffffffff ffffffff        
200154e0: ffffffff ffffffff ffffffff ffffffff ffffffff ffffffff ffffffff ffffffff        
20015500: ffffffff ffffffff ffffffff ffffffff ffffffff ffffffff ffffffff ffffffff        
20015520: ffffffff ffffffff ffffffff ffffffff ffffffff ffffffff 20003cc0 0809ffa9        
20015540:560: 80000050 080a2ca5 200166b0 200155e0 00000018 080a2fcd 200166b0 200155e0        
20015580: 00000000 080000000 0803c339 00000000 00000000 00000000 080a07a1        
200155c0: 00000000 00000000 ffffffff 026dbef1 3336c35d 6ff36bb7 0        
R8: 20015278 00000053 00000000 20011130 20015250 20015140 0803a41f 0803a406        
xPSR: 01        
```  
The mavlink was configured in /etc/extras.txt as follows:  
    
```bash     
 nsh> cat /fs/microsd/etc/extras.txt        
mavlink stop-all        
mavlink start -d /dev/ttyS1 -b 57600 -r 1024        
mavlink start -d /dev/ttyS2 -b 9600 -r 192         
```  
Is this problem also fixed in v1.5.0?  
