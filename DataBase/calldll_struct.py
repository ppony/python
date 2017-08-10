
from ctypes import *

class SimpStruct(Structure):  
    _fields_ = [ ("nNo", c_int),  
              ("fVirus", c_float),
              ("szBuffer", c_char * 512)]  
  
dll = CDLL("test.dll")  
simple = SimpStruct();  
simple.nNo = 16  
simple.fVirus = 3.1415926  

dll.PrintStruct(byref(simple))
print (dll.PrintStruct(byref(simple)))

print(simple.nNo)
print(simple.szBuffer)
