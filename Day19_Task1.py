"""
here we are done abstraction , encapsulation , constructor
"""

'''
#Abstraction
from abc import ABC, abstractmethod

class GradeCalculation(ABC):
    @abstractmethod
    def totalmark():
        pass
    @abstractmethod
    def grademark():
      pass
    
class SSLCStd(GradeCalculation):
    def __init__(self,*marks):
        self.marks = marks
        self.total = 0
        self.grade = None
    def totalmark(self):
        total = 0
        for i in self.marks:
            total+=i
        self.total = total
        print("Total : ",self.total)
    def grademark(self):
        grade = ''
        avg = self.total//5
        if avg>= 76 and avg<=100:
            grade = 'A'
        elif avg>=51 and avg<=75:
            grade = 'B'
        elif avg>=26 and avg<=50:
            grade = 'C'
        elif avg>=0 and avg<=25:
            grade = 'D'
        else:
            grade = 'invalid marks'
        self.grade = grade
        print("Grade : ",self.grade)

t1 = SSLCStd(20,30,40,50,60)
t1.totalmark()
t1.grademark()

class HSCStd(GradeCalculation):
    def __init__(self,*marks):
        self.marks = marks
        self.total = 0
    def totalmark(self):
        total = 0
        for i in self.marks:
            total+=i
        self.total = total
        print("Total : ",self.total)
    def grademark(self):
        grade = ''
        avg = self.total//6
        if avg>= 76 and avg<=100:
            grade = 'A'
        elif avg>=51 and avg<=75:
            grade = 'B'
        elif avg>=26 and avg<=50:
            grade = 'C'
        elif avg>=0 and avg<=25:
            grade = 'D'
        else:
            grade = 'invalid marks'
        print("Grade : ",grade)
            

t2 = HSCStd(20,30,40,50,60,39)
t2.totalmark()
t2.grademark()

#Encapsulation

class account:
    def __init__(self,name,pin):
        self.name = name
        self.pin = pin   
a = account("Mounika",2369)
print(a.name)
print(a.pin)

class account1:
    def __init__(self,name,pin):
        self.__name = name
        self.__pin = pin
    def getter(self):
        print("Name : ",self.__name)
        print("Pin : ",self.__pin)
        
a1 = account1("Mounika",2369)
#print(a.name) -> Give error
#print(a.pin) -> Give error
a1.getter()

class account2:
    def __init__(self):
        self.__name = ''
        self.__pin = 0
        
    def getter(self):
        print("Name : ",self.__name)
        print("Pin : ",self.__pin)

    def setter(self,name,pin):
        self.__name = name
        self.__pin = pin
        
a2 = account2()
#print(a.name) -> Give error
#print(a.pin) -> Give error
a=input("Enter Your Name : ")
b=int(input("Enter Your Pin :"))
a2.setter(a,b)
a2.getter()

#Cosntructor chaining

class A:
    def __init__(self):
        print("Hi from Parent")

class B(A):
    def __init__(self):
        print("Start from child")
        super().__init__()
        print("End from child")
b = B()
'''

#__doc__ string -> Using to get the documentation
print(__doc__)











