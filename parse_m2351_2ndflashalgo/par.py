def printme( str ):
   "This prints a passed string into this function"
   print (str)
   return;

foo = open("binout.bin", "wb")
with open("binbin",'rb') as f:
    while True:
        c0=f.read(1)
        c1=f.read(1)
        str = c0 + b'\x2c' + c1 + b'\x2c'
        print(str)        
        foo.write(str)
        if not c0: break
        
#printme('heleleeo')
#fo = open("binbin", "rb")
#print('haha', c0, c1)
#str = c0 + b'\x2c' + c1
#print(str)
foo.write(str)
f.close()
foo.close()
