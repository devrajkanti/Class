class Person:
    def __init__(self,id):
        self.id =id
        print(id,"Our Class is Created")
    def __del__(self):
        print("Destructor Called")
    def setName(self,FName,LName):
        self.FName = FName
        self.LName = LName
    def printName(self):
        print(self.FName,"",self.LName)

class Anjali:
    def setData(self,x,y):
        self.x=x
        self.y=y

    def add(self):
        print(self.x+self.y)

myPerson = Person(10)
myPerson.setName("Devraj","Kanti")
myPerson.printName()

myAnjali = Anjali()
myAnjali.setData(10,20)
myAnjali.add()