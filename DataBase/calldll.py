
from ctypes import *

mydll = cdll.LoadLibrary('FlashInfo.dll')

# gg = c_uint(0)
# ggg = c_int * 2
# ia = ggg(0, 0)
# mydll.sum1(byref(gg), byref(ia))

# print (hex(gg.value))
# print ("%x" % gg.value)
# print (ia[0])
# print (hex(ia[1]))

uPID = c_uint(0x00945330)
uConfig0 = c_uint(0xfffffffe)
uConfig1 = c_uint(0x10000)
puLDROM_Addr = c_uint(0)
puAPROM_Addr= c_uint(0)
puNVM_Addr = c_uint(0)
ia = c_uint * 3
auSPROM_Addr = ia(0,0,0)
puKPROM_Addr = c_uint(0)
puLDROM_Size = c_uint(0)
puAPROM_Size = c_uint(0)
puNVM_Size = c_uint(0)
ia = c_uint * 3
auSPROM_Size = ia(0,0,0)
puKPROM_Size = c_uint(0)

mydll.GetInfo2(uPID,
             uConfig0,
             uConfig1,
             byref(puLDROM_Addr),
             byref(puAPROM_Addr),
             byref(puNVM_Addr),
             byref(auSPROM_Addr),
             byref(puKPROM_Addr),
             byref(puLDROM_Size),
             byref(puAPROM_Size),
             byref(puNVM_Size),
             byref(auSPROM_Size),
             byref(puKPROM_Size))

print(hex(puAPROM_Size.value))
print(hex(puNVM_Addr.value))
print(hex(puNVM_Size.value))

# class SimpStruct(Structure):  
    # _fields_ = [ ("nNo", c_int),  
              # ("fVirus", c_float),
              # ("szBuffer", c_char * 512)]  
  
# dll = CDLL("test.dll")  
# simple = SimpStruct();  
# simple.nNo = 16  
# simple.fVirus = 3.1415926  

# dll.PrintStruct(byref(simple))
# print (dll.PrintStruct(byref(simple)))

# print(simple.nNo)
# print(simple.szBuffer)
