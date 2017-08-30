import binascii 

i=0
pos = raw_input()
posend = raw_input() 
foo = open("binout.bin", "wb")
  
with open ( "binbin", "r" ) as myfile:       
    while True:
        if (int(pos, 16) > i):
            i=i+1
            myfile.seek(i)
            # print 'inner'+str(i)
            continue
        c0 = myfile.read(1)
        c1 = myfile.read(1)
        if not c1: break
        if (int(posend, 16) <= i):break
        str = '0x'+(binascii.hexlify( c0 )) + b'\x2c' + '0x' + (binascii.hexlify( c1 )) + b'\x2c'
        print(str)        
        foo.write(str)
        # print (binascii.hexlify( c1 ))
        # print b'\x2c'
        # print (binascii.hexlify( c0 ))
        # print b'\x2c'
        i=i+2
        

        