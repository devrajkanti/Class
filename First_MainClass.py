class Person:
    def setFullName(dvrj,FName,LName):
        dvrj.FName = FName
        dvrj.LName = LName

    def printFullName(dvrj):
        print(dvrj.FName,"",dvrj.LName)

myPerson = Person()
myPerson.setFullName("Devraj","Kanti")
myPerson.printFullName()
