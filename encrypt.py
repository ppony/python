import random
 
class Encrypt:
    def __init__(self):
        self.code = [chr(i) for i in range(97, 123)]
        random.shuffle(self.code)
        self.alph = [chr(i) for i in range(97, 123)]
     
    def __str__(self):
        return "code: " + "".join(self.code) +"\nalph: "+ "".join(self.alph)
     
    def setCode(self, data):
        self.code = list(data)
 
    def getCode(self):
        return "".join(self.code)
    
    def toEncode(self, s):
        result = ""
        for i in s:
            if i in self.code:
                j = self.alph.index(i)
                result += self.code[j]
            else:
                result += i
     
        return result
     
    def toDecode(self, s):
        result = ""
        for i in s:
            if i in self.code:
                j = self.code.index(i)
                result += self.alph[j]
            else:
                result += i
     
        return result    
 
if __name__ == '__main__':
    o = object()
    print(o)
    e = Encrypt()
    print(e)
    s1 = "There is no spoon."
    print("input: " + s1)
    s2 = e.toEncode(s1)
    print("encode: " + s2)
    s3 = e.toDecode(s2)
    print("decode: " + s3)
    print()
