#Below is the code of multiple inheritance where the base class inherits the data from two classes.

class FirstClass():
    val1 = "First"
    val2 = "Second"

class SecondClass():
    val3 = "Three"
    val4 = "Four"

class ThirdClass(FirstClass,SecondClass):
    val5 = "Five"
    val6 = "Six"

myFirstClass = FirstClass()
mySecondClass = SecondClass()
myThirdClass = ThirdClass()

print(myThirdClass.val1)
print(myThirdClass.val3)