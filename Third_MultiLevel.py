#In the below code the base class can inherit the data from the super class, i.e. it is an example of multilevel class where the third class
#inherits the data from the second class which in turn inherits the data from first class. Hence the third class is having access to member functions
# of first class.
class ClassOne():
    value1 = "First"
    value2 = "Second"

class ClassTwo(ClassOne):
    value3 = "Third"
    value4 = "Fourth"

class ClassThree(ClassTwo):
    value5 = "Fifth"
    value6 = "Sixth"

myClassOne = ClassOne()
myClassTwo = ClassTwo()
myClassThree = ClassThree()

print(myClassThree.value1)