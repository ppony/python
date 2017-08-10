
from strategy import *
from nu_openocd import *
from ctypes import *


class ICP(Strategy):

    def connect_func(self):
        mydll = cdll.LoadLibrary('FlashInfo.dll')

        def show(*args):
            print(*args, end="\n\n")
        with OpenOcd(True) as ocd:
            addr = 0x40000000
            value = ocd.readVariable(addr)
            show("variable @ %s: %s" % (hexify(addr), hexify(value)))
            uPID = c_uint(value)
            # uPID = c_uint(0x00945330)
            uConfig0 = c_uint(0xfffffffe)
            uConfig1 = c_uint(0x10000)
            puLDROM_Addr = c_uint(0)
            puAPROM_Addr = c_uint(0)
            puNVM_Addr = c_uint(0)
            ia = c_uint * 3
            auSPROM_Addr = ia(0, 0, 0)
            puKPROM_Addr = c_uint(0)
            puLDROM_Size = c_uint(0)
            puAPROM_Size = c_uint(0)
            puNVM_Size = c_uint(0)
            ia = c_uint * 3
            auSPROM_Size = ia(0, 0, 0)
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

            # print(hex(puAPROM_Size.value))
            # print(hex(puNVM_Addr.value))
            # print(hex(puNVM_Size.value))

    def erase_func(self):
        print('icp erase')

    def prog_func(self):
        print('icp prog')

        def show(*args):
            print(*args, end="\n\n")
        with OpenOcd(True) as ocd:
            ocd.send("reset")

            show(ocd.send("ocd_echo \"echo says hi!\"")[:-1])
            show(ocd.send("capture \"ocd_halt\"")[:-1])
            addr = 0x20001000
            value = ocd.readVariable(addr)
            show("variable @ %s: %s" % (hexify(addr), hexify(value)))

            ocd.writeVariable(addr, 0xdeadc0de)
            show("variable @ %s: %s" %
                 (hexify(addr), hexify(ocd.readVariable(addr))))

            data = [1, 0, 0xaaaaaaaa, 0x23, 0x42, 0xffff]
            wordlen = 32
            n = len(data)

            read = ocd.readMemory(wordlen, addr, n)
            show("memory (before):", list(map(hexify, read)))

            ocd.writeMemory(wordlen, addr, n, data)

            read = ocd.readMemory(wordlen, addr, n)
            show("memory  (after):", list(map(hexify, read)))

            compareData(read, data)

            show(ocd.send("reg r13 0x20001000")[:-1])
            show(ocd.send("flash write_image erase C:\LDROM.bin 0x0")[:-1])
            # show(ocd.send("flash write_image erase " + self.userinput + " 0x0")[:-1])


# class ISP(Strategy):
#	def erase_func(self):
#		print('isp erase')
#	def prog_func(self):
#		print('isp prog')

if __name__ == "__main__":
        #_isp = ISP()
    _icp = ICP()
    con = Context(_icp)
    con.call_func()
    # con=Context(_isp)
    # con.call_func()
    con = Context(_icp)
    con.call_func()
