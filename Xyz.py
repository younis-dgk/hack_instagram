import os,re,sys,platform
os.system('git pull')
bit = platform.architecture()[0]
if bit == '64bit':
    import Xyz
    
elif bit == '32bit':
    print(f"\03[1;91m Sorry 32Bit Not Supported .... ");exit() 
 
