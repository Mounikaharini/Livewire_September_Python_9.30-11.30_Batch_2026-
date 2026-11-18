'''
a=5
assert a==50
print(a)


a = 110
if a!=10:
    raise NameError("HI A IS NOT 10")
else:
    print(a)

class Animal:
    def Dog():
        print("Dog is here ... !")
    def Cat():
        print("Cat is here ... !")
    def Mouse(name="Mouse"):
        print(name,"is here ... !")
object1 = Animal
object1.Dog()
object1.Cat()
object1.Mouse("Micky")

#Single Inheritance
class calc:
    def add(a=0,b=0):
        print(a+b)
    def sub(a=0,b=0):
        print(a-b)
    def multiply(a=0,b=0):
        print(a*b)
    def div(a=0,b=0):
        print(int(a/b))

p1 = calc
p1.add(2,2)

p2 = calc
p2.sub(5,5)

p3 = calc
p3.multiply(2,8)

p4 = calc
p4.div(6,2)

class calc2(calc):
    def mod(a=0,b=0):
        print(a%b)
    def floor(a=0,b=0):
        print(a//b)
    def exp(a=0,b=0):
        print(a**b)
c1 = calc2
c1.add(2,2)
c1.sub(2,2)
c1.multiply(2,2)
c1.div(2,2)
c1.mod(2,2)
c1.floor(2,2)
c1.exp(2,2)

#multiple inheritance

#SDLC -> Software Development Lifecycle

1.BDA - Client (Gather the Requirements for the projects)
2.UI/UX - Creating a template by using the requirements
3.Development - Develop the project by using UI/UX template
4.Testing - Test the project workflow by using sample test case
5.Deployment - Deploy the project through cloud
6.Maintain - Maintain the Site

class BDA:
    def BDAWork():
        print("Client (Gather the Requirements for the projects)")
t1 = BDA
t1.BDAWork()

class UIUX:
    def UIUXWork():
        print("Creating a template by using the requirements")
t2 = UIUX
t2.UIUXWork()

class Development:
    def DevelopmentWork():
        print("Develop the project by using UI/UX template")
    def Frontend():
        print("Develop a frontend area using html,css,js,react")
    def Backend():
        print("Develop the backend part using any programming language")
    def Database():
        print("Store the Data from the frontend part through backend help")
t3 = Development
t3.DevelopmentWork()
t3.Frontend()
t3.Backend()
t3.Database()

class Testing:
    def TestingWork():
        print("Test the project workflow by using sample test case")
    def ManualTesting():
        print("Test Through Manual Checking")
    def AutomationTesting():
        print("Testing through Automation by using selenium / cucumber")
t4 = Testing
t4.TestingWork()
t4.ManualTesting()
t4.AutomationTesting()

class Deployment:
    def DeploymentWork():
        print("Deploy the project through cloud for public access")
t5 = Deployment
t5.DeploymentWork()

class Maintain:
    def MaintainWork():
        print("Maintain the Whole project and Solve the customer queries")
t6 = Maintain
t6.MaintainWork()

class Management(BDA,UIUX,Development,Testing,Deployment,Maintain):
    def ManagementTeam():
        print("Make people to work and monitor individual work")

t = Management
t.BDAWork()
t.UIUXWork()
t.DevelopmentWork()
t.Frontend()
t.Backend()
t.Database()
t.TestingWork()
t.ManualTesting()
t.AutomationTesting()
t.DeploymentWork()
t.MaintainWork()
t.ManagementTeam()

#Multi-level Inheritance
class Student:
    def StudentWork():
        print("Learn from Teachers, Obey the order from Teachers")

class Teachers(Student):
    def TeachersWork():
        print("Guide the students , Manage the Management Works too")

class HeadMaster(Teachers):
    def HeadMastersWork():
        print("Guide the students , teachers , Maintain the whole school")

s = Student
s.StudentWork()

t = Teachers
t.StudentWork()
t.TeachersWork()

h = HeadMaster
h.StudentWork()
h.TeachersWork()
h.HeadMastersWork()
'''
#Hierarchical Inheritance

class Python:
    def PythonWork():
        print("Console Based Project")

class Selenium(Python):
    def SeleniumWork():
        print("Used for s/w testing")

class AlAgorithms(Python):
    def AlAgorithmsWorks():
        print("Create an AI Model")

p = Python
p.PythonWork()

s = Selenium
s.PythonWork()
s.SeleniumWork()

a = AlAgorithms
a.PythonWork()
a.AlAgorithmsWorks()


