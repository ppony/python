
from strategy import *
from nu_openocd import *

class ICP(Strategy):
    def connect_func(self):
        print('icp connect')
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
            show("variable @ %s: %s" % (hexify(addr), hexify(ocd.readVariable(addr))))

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
            #show(ocd.send("flash write_image erase " + self.userinput + " 0x0")[:-1])



#class ISP(Strategy):
#	def erase_func(self):
#		print('isp erase')
#	def prog_func(self):
#		print('isp prog')

if __name__=="__main__":
	#_isp = ISP()
	_icp = ICP()
	con=Context(_icp)
	con.call_func()
	#con=Context(_isp)
	#con.call_func()
	con=Context(_icp)
	con.call_func()
