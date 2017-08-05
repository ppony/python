from tkinter import *
from encrypt import Encrypt
from nu_openocd import *
import os

from singleton import *


class EncryptGUI(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.createWidgets()
        self.e = None
        self.userinput = ""
        self.result = ""
        self.interface = self.interface_opt.get()
        prog = Programmer(self.interface)
        print("__init__")

    def createWidgets(self):
        self.inputText = Label(self)
        self.inputText["text"] = "APROM:"
        self.inputText.grid(row=0, column=0)
        self.inputField = Entry(self)
        self.inputField["width"] = 50
        self.inputField.grid(row=0, column=1, columnspan=6)
 
        self.outputText = Label(self)
        self.outputText["text"] = "interface:"
        self.outputText.grid(row=1, column=0)
        self.outputField = Entry(self)
        self.outputField["width"] = 50
        self.outputField.grid(row=1, column=1, columnspan=6)
         
        self.new = Button(self)
        self.new["text"] = "Connect"
        self.new.grid(row=2, column=0)
        self.new["command"] =  self.connectMethod
#        self.load = Button(self)
#        self.load["text"] = "Load"
#        self.load.grid(row=2, column=1)
#        self.load["command"] =  self.loadMethod
        self.save = Button(self)
        self.save["text"] = "start"
        self.save.grid(row=2, column=2)
        self.save["command"] =  self.startMethod

        self.interface_opt = StringVar(self.master)
        self.interface_opt.set("usb_swd") # default value

        self.interface = OptionMenu(self.master, self.interface_opt, "usb_swd", "usb", "uart")
        self.interface["text"] = "interface"
        self.interface.grid(row=2, column=3)
        
#        self.encode = Button(self)
#        self.encode["text"] = "Encode"
#        self.encode.grid(row=2, column=3)
#        self.encode["command"] =  self.encodeMethod
#        self.decode = Button(self)
#        self.decode["text"] = "Decode"
#        self.decode.grid(row=2, column=4)
#        self.decode["command"] =  self.decodeMethod
#        self.clear = Button(self)
#        self.clear["text"] = "Clear"
#        self.clear.grid(row=2, column=5)
#        self.clear["command"] =  self.clearMethod
        self.copy = Button(self)
        self.copy["text"] = ""
        self.copy.grid(row=2, column=6)
        self.copy["command"] =  self.copyMethod
 
        self.displayText = Label(self)
        self.displayText["text"] = "programming...."
        self.displayText.grid(row=3, column=0, columnspan=7)
     
    def connectMethod(self):
        prog.Connect()
        print("connectMethod")
        # logging.debug("connectMethod")

    def loadMethod(self):
        if os.path.exists("./code.txt"):
            f = open('./code.txt', 'r')
            code = f.readline()
            self.e = Encrypt()
            self.e.setCode(code)
            self.displayText["text"] = "code: " + self.e.getCode()
        else:
            self.displayText["text"] = "Load denied!!"

    def startMethod(self):
        self.userinput = self.inputField.get()
        # self.interface = self.interface_opt.get()
        print(self.userinput)
        # print(self.interface)
        # prog = Programmer("usb_swd")
        
        # prog = Programmer(self.interface)
        # prog1 = Programmer(_icp)
        
        # assert prog is prog1

        # print("same")
        # progisp = Programmer(_isp)
        
        # assert prog is progisp
        # prog.set_strategy(_isp)
        prog.start()

        print("start()")

        #prog.start()
        #if self.e == None:
        #    self.displayText["text"] = "No Encrypt object can save!!"
        #else:
        #    f = open('./code.txt', 'w')
        #    f.write(self.e.getCode())
        #    f.closed
        #    self.displayText["text"] = "The code is saved."

        ##1 direct testing
        # def show(*args):
        #     print(*args, end="\n\n")
 
        # with OpenOcd(True) as ocd:
            # ocd.send("reset")
 
            # show(ocd.send("ocd_echo \"echo says hi!\"")[:-1])
            # show(ocd.send("capture \"ocd_halt\"")[:-1])
            # addr = 0x20001000
            # value = ocd.readVariable(addr)
            # show("variable @ %s: %s" % (hexify(addr), hexify(value)))
 
            # ocd.writeVariable(addr, 0xdeadc0de)
            # show("variable @ %s: %s" % (hexify(addr), hexify(ocd.readVariable(addr))))
 
            # data = [1, 0, 0xaaaaaaaa, 0x23, 0x42, 0xffff]
            # wordlen = 32
            # n = len(data)
 
            # read = ocd.readMemory(wordlen, addr, n)
            # show("memory (before):", list(map(hexify, read)))
 
            # ocd.writeMemory(wordlen, addr, n, data)
 
            # read = ocd.readMemory(wordlen, addr, n)
            # show("memory  (after):", list(map(hexify, read)))
 
            # compareData(read, data)
            # print("jajadddddja")
            # self.userinput = self.inputField.get()
            # self.interface = self.outputField.get()

            # print(self.userinput)
            # print(self.interface)

            # show(ocd.send("reg r13 0x20001000")[:-1])
            # show(ocd.send(r"flash write_image erase C:\\LDROM.bin 0x0")[:-1])
            # show(ocd.send("flash write_image erase " + self.userinput + " 0x0")[:-1])

        ##2 real case
        # _icp = ICP()
        # _isp = ISP()
        # print("lala")
        # prog = Programmer(_icp)
        # prog.start()

 
    def encodeMethod(self):
        self.userinput = self.inputField.get()
         
        if self.userinput == "":
            self.displayText["text"] = "No input string!!"
        else:
            if self.e == None:
                self.displayText["text"] = "No encrypt object!!"
            else:
                self.result = self.e.toEncode(self.userinput)
                self.outputField.delete(0, 200)
                self.outputField.insert(0, self.result)
                self.displayText["text"] = "Encoding success!!"
         
 
    def decodeMethod(self):
        self.userinput = self.inputField.get()
         
        if self.userinput == "":
            self.displayText["text"] = "No input string!!"
        else:
            if self.e == None:
                self.displayText["text"] = "No encrypt object!!"
            else:
                self.result = self.e.toDecode(self.userinput)
                self.outputField.delete(0, 200)
                self.outputField.insert(0, self.result)
                self.displayText["text"] = "Decoding success!!"
 
    def clearMethod(self):
        self.e = None
        self.userinput = ""
        self.result = ""
        self.inputField.delete(0, 200)
        self.outputField.delete(0, 200)
 
        self.displayText["text"] = "It's done."
 
    def copyMethod(self):
        _icp = ICP()
        con = Context(_icp)
        con.call_func()
        if self.result == "":
            self.displayText["text"] = "Copy denied!!"
        else:
            self.clipboard_clear()
            self.clipboard_append(self.result)
            self.displayText["text"] = "It is already copied to the clipboard."
 
if __name__ == '__main__':
    root = Tk()
    app = EncryptGUI(master=root)
    app.mainloop()
