'''
#Hybrid Inheritance
class ButtonPhone:
    def ButtonPhoneFeature():
        print("--  Button Phone Features --")
        print("Used To Talk \nText Messages Availability \nUse Camera")
class SmartPhone(ButtonPhone):
    def SmartPhoneFeature():
        print("-- Smart Phone Feature --")
        print("Touch Screen \nInternet upto 4G \nSocial Media Usage") 
class Tab:
    def TabFeature():
        print("-- Tab Feature --")
        print("Wider Screen \nMultiple Screen Access \nWe can use as phone and lap")
class FoldablePhone(SmartPhone, Tab):
    def FoldablePhoneFeature():
        print("Multi Screen\nWE can use as tab and phone\nEasy to Carry \nN/w Speed Increase")

b = ButtonPhone
b.ButtonPhoneFeature()
print()
s = SmartPhone
s.ButtonPhoneFeature()
s.SmartPhoneFeature()
print()
t = Tab
t.TabFeature()
print()
f = FoldablePhone
f.ButtonPhoneFeature()
f.SmartPhoneFeature()
f.TabFeature()
f.FoldablePhoneFeature()

#Polymorphism
#Function Overloading
#Not possible to do directly , achieve by using variable length argument
class Calculator:
    def add(*data):
        output = 0
        for i in data:
            output = output + i
        return output
c = Calculator
print(c.add(1,2,3,4,5,6))
n = c.add(1,2,3,4,5,6)
print(n)

#Operator Overloading
# = act as for addition and concatenation
print(10+20)
print("hi"+" "+"bye")

#Function Overriding
class Briyani:
    def BriyaniIngredient():
        print("-- Briyani Ingredient --")
        biryani_ingredients_detailed = [
        {"item": "Basmati rice", "quantity": "500g"},
        {"item": "Plain yogurt", "quantity": "1/2 cup"},
        {"item": "Onions", "quantity": "2 large"},
        {"item": "Tomatoes", "quantity": "2 medium"},
        {"item": "Ginger-garlic paste", "quantity": "2 tbsp"},
        {"item": "Green chilies", "quantity": "3"},
        {"item": "Mint leaves", "quantity": "1/4 cup"},
        {"item": "Coriander leaves", "quantity": "1/4 cup"},
        {"item": "Ghee", "quantity": "3 tbsp"},
        {"item": "Cooking oil", "quantity": "2 tbsp"},
        {"item": "Whole spices (bay leaves, cardamom, cinnamon, cloves, star anise)", "quantity": "1 mix"},
        {"item": "Turmeric powder", "quantity": "1/2 tsp"},
        {"item": "Red chili powder", "quantity": "1 tsp"},
        {"item": "Biryani masala", "quantity": "2 tsp"},
        {"item": "Saffron", "quantity": "1 pinch"},
        {"item": "Warm milk", "quantity": "2 tbsp"},
        {"item": "Lemon juice", "quantity": "1 tbsp"},
        {"item": "Salt", "quantity": "to taste"},
        {"item": "Water", "quantity": "4 cups"}]
        
        for i in biryani_ingredients_detailed:
            print("=> ",i)
    def AddOn():
        addon = {"item": "ItemName", "quantity": "500g"}
        print("Add On : ",addon)
b = Briyani
b.BriyaniIngredient()
b.AddOn()

class VegBriyani(Briyani):
    def AddOn():
        addon = {"item": "Vegetables", "quantity": "500g"}
        print("Add On : ",addon)
v = VegBriyani
v.BriyaniIngredient()
v.AddOn()

class ChickenBriyani(Briyani):
    def AddOn():
        addon = {"item": "Chicken", "quantity": "500g"}
        print("Add On : ",addon)
c = ChickenBriyani
c.BriyaniIngredient()
c.AddOn()

'''
#Abstraction
from abc import ABC, abstractmethod

class GradeCalculation(ABC):
    @abstractmethod
    def total():
        pass
    @abstractmethod
    def grade():
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
    def gradeMark(self):
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
t1.totalMark()
t1.gradeMark()
'''
class HSCStd(GradeCalculation):
    def __init__(self,*marks):
        self.marks = marks
        self.total = 0
    def total(self):
        total = 0
        for i in self.marks:
            total+=i
        self.total = total
        print("Total : ",self.total)
    def grade(self):
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

'''











