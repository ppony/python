import binascii
import pdb
import os
import re

mylist = [r'./init', r'./ProgramPage', r'./EraseSector', r'./Verify']
idx = 0
pre_s0 = ""
# pos = raw_input('start from ')
# bp_pos = raw_input('replace this position with bkpt assembly code ')
# posend = raw_input('to end - not include this line ')


for idx, name in enumerate(mylist):
    """
    to search last 16bit of function before veneer,
    have this position we know where to replace 16bit bkpt instruction to it.
    there is two possible $d and $t when see veneer
    """
    with open(name + r'.txt', "rb") as f:
        for i, s0 in enumerate(f):
            if re.search(r'\s\$t\s|\s\$d', str(s0)) is not None:
                s1 = pre_s0.split(b':')
                bp_pos = hex(int(s1[0], 16))
                print(bp_pos)
                break
            if not s0:
                break
            pre_s0 = s0
    f.close()

    i = 0
    foo = open(name + r'/' + name + r'.txt', "w")
    with open(name + r'/PrgCode', "rb") as myfile:
        # i = int(pos, 16)
        # myfile.seek(i)
        while True:
            c0 = myfile.read(1)
            c1 = myfile.read(1)

            if not c1:
                break
            # if (int(posend, 16) <= i):
            #     break
            if (int(bp_pos, 16) == i):
                mystr = '0x00' + ',' + '0xbe' + ','
            else:
                mystr = '0x' + str(binascii.hexlify(c0)) + ',' + \
                    '0x' + str(binascii.hexlify(c1)) + ','
            # print(mystr)
            foo.write(mystr)
            i = i + 2
    foo.close()
