class Fibs:
    def __init__(self):
        self.i = 0
        self.j = 1
     
    def __str__(self):
        return str(self.i)
     
    def __iter__(self):
        print("der")
        return self
     
    def __next__(self):
         self.i, self.j = self.j, self.i + self.j
         print("iinnnn  "+str(self.i))
         return self.i
 
fibs = Fibs()
print("ok")
for f in fibs:
    #print(f)
    if f > 10:
        break
