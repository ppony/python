from tkinter import *
from encrypt import Encrypt
from nu_openocd import *
import os
 
class EncryptGUI(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.createWidgets()
        self.e = None
        self.userinput = ""
        self.result = ""
 
    def createWidgets(self):
        self.inputText = Label(self)
        self.inputText["text"] = "Input:"
        self.inputText.grid(row=0, column=0)
        self.inputField = Entry(self)
        self.inputField["width"] = 50
        self.inputField.grid(row=0, column=1, columnspan=6)
 
        self.outputText = Label(self)
        self.outputText["text"] = "Output:"
        self.outputText.grid(row=1, column=0)
        self.outputField = Entry(self)
        self.outputField["width"] = 50
        self.outputField.grid(row=1, column=1, columnspan=6)
         
        self.new = Button(self)
        self.new["text"] = "New"
        self.new.grid(row=2, column=0)
        self.new["command"] =  self.newMethod
        self.load = Button(self)
        self.load["text"] = "Load"
        self.load.grid(row=2, column=1)
        self.load["command"] =  self.loadMethod
        self.save = Button(self)
        self.save["text"] = "Save"
        self.save.grid(row=2, column=2)
        self.save["command"] =  self.saveMethod
        self.encode = Button(self)
        self.encode["text"] = "Encode"
        self.encode.grid(row=2, column=3)
        self.encode["command"] =  self.encodeMethod
        self.decode = Button(self)
        self.decode["text"] = "Decode"
        self.decode.grid(row=2, column=4)
        self.decode["command"] =  self.decodeMethod
        self.clear = Button(self)
        self.clear["text"] = "Clear"
        self.clear.grid(row=2, column=5)
        self.clear["command"] =  self.clearMethod
        self.copy = Button(self)
        self.copy["text"] = "Copy"
        self.copy.grid(row=2, column=6)
        self.copy["command"] =  self.copyMethod
 
        self.displayText = Label(self)
        self.displayText["text"] = "something happened"
        self.displayText.grid(row=3, column=0, columnspan=7)
     
    def newMethod(self):
        self.e = Encrypt() 
        self.displayText["text"] = self.e
 
    def loadMethod(self):
        if os.path.exists("./code.txt"):
            f = open('./code.txt', 'r')
            code = f.readline()
            self.e = Encrypt()
            self.e.setCode(code)
            self.displayText["text"] = "code: " + self.e.getCode()
        else:
            self.displayText["text"] = "Load denied!!"
 
    def saveMethod(self):
        if self.e == None:
            self.displayText["text"] = "No Encrypt object can save!!"
        else:
            f = open('./code.txt', 'w')
            f.write(self.e.getCode())
            f.closed
            self.displayText["text"] = "The code is saved."
 
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
        if self.result == "":
            self.displayText["text"] = "Copy denied!!"
        else:
            self.clipboard_clear()
            self.clipboard_append(self.result)
            self.displayText["text"] = "It is already copied to the clipboard."
 
if __name__ == '__main__':
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
 

    root = Tk()
    app = EncryptGUI(master=root)
    app.mainloop()
