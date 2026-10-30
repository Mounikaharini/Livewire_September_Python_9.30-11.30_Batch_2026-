'''
def add():
    a = 10
    b = 20
    print(a+b)
add()

def add1(a,b):#parameter
    print(a+b)
add1(12,23)#argument

def add2(a,b):
    return a+b
x = add2(123,866)
print(x)
print(add2(12,26))

def sub(a,b):
    c = a-b
    return c
a = sub(5,3)
print(a)
'''
#without parameter without return
def fun1():
    print("hi from fun1")
fun1()

#without parameter with return
def fun2():
    return "hi from fun2"
data = fun2()
print(data)

#with parameter without return
def fun3(x,y):
    print(x<y)
m = 10
n = 20
fun3(m,n)

#with parameter with return
def login(username,password):
    if username=="admin" and password==1234:
        return "Login Successful"
    else:
        return "Invalid Username or Password"
n = int(input("Enter the no.of.login : "))
for i in range(n):
    username = input("Enter the Username : ")
    password = int(input("Enter the Password : "))
    print(login(username,password))
