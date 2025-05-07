# Basic Information:
### Title:  Bug: Firmware does not build if submodule #8255 
### Issue status: Closed
### Author: jlecoeur
### Issue open time: Nov 8, 2017
# Report
### Report author: jlecoeur
### Report Time: Nov 8, 2017
### Report Content:   
Bug Report  
If PX4/Firmware is cloned as a submodule, it does not build.    
I also had the problem when upgrading an existing Firmware submodule.  
Steps to reproduce:  
    
```bash     
 $ mkdir -p tmp/repo      
$ cd tmp/repo      
$ git init      
$ git submodule add https://github.com/PX4/Firmware      
$ git commit -am "Added submodule"      
$ cd Firmware      
$ git submodule update --init --recursive      
$ make    
```  
    
```bash     
 -- Build Type: RelWithDebInfo      
-- PX4 VERSION: v1.6.5-1632-gcf7140526      
-- CONFIG: posix_sitl_default      
-- The CXX compiler identification is GNU 7.2.0      
-- The C compiler identification is GNU 7.2.0      
-- The ASM compiler identification is GNU      
-- Found assembler: /usr/bin/cc      
-- Check for working CXX compiler: /usr/bin/c++      
-- Check for working CXX compiler: /usr/bin/c++ -- works      
-- Detecting CXX compiler ABI info      
-- Detecting CXX compiler ABI info - done      
-- Detecting CXX compile features      
-- Detecting CXX compile features - done      
-- Check for working C compiler: /usr/bin/cc      
-- Check for working C compiler: /usr/bin/cc -- works      
-- Detecting C compiler ABI info      
-- Detecting C compiler ABI info - done      
-- Detecting C compile features      
-- Detecting C compile features - done      
-- Found PythonInterp: /usr/bin/python (found version "3.6.3")       
-- Found PY_jinja2: /usr/lib/python3.6/site-packages/jinja2        
-- C compiler: cc (GCC) 7.2.0      
-- C++ compiler: c++ (GCC) 7.2.0      
CMake Error at src/lib/version/CMakeLists.txt:50 (message):      
  /home/jlecoeur/tmp/repo/Firmware/src/lib/.git/modules/Firmware is not a      
  directory      
-- Configuring incomplete, errors occurred!      
See also "/home/jlecoeur/tmp/repo/Firmware/build/posix_sitl_default/CMakeFiles/CMakeOutput.log".      
/bin/sh: line 0: cd: /home/jlecoeur/tmp/repo/Firmware/build/posix_sitl_default: No such file or directory      
make: *** [Makefile:147: posix_sitl_default] Error 1    
```  
When cloned separately, it works as expected:  
    
```bash     
 $ mkdir tmp      
$ git clone https://github.com/PX4/Firmware      
$ cd Firmware      
$ git submodule update --init --recursive      
$ make    
```  

# Comment
## Comment1
### Comment author: dagar
### Comment Time: Nov 9, 2017
### Comment Content:   
Thanks for reporting, we keep breaking this. Once we get it working again let's add something to CI.  

## Comment2
### Comment author: dagar
### Comment Time: Nov 22, 2017
### Comment Content:   
Fixed in \\\#8334  
