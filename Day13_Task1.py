'''
#positional Argument
#The values are passed in the same order*as
#the parameters are defined.

def smallestOfTwo(a,b):
    if a<b:
        print(a)
    else:
        print(b)
smallestOfTwo(12,23)

#Default Argument
#These have a default value.If no value is passed for
#that parameter, Python uses the default.


def addition(a=0,b=0,c=0):
    print(a+b+c)
addition(1)
addition(1,2)
addition(1,2,3)

#Keyword Argument
#Here, the parameters are specified by name while
#calling the function.
Order doesn’t matter when using keywords.


def userDetails(name="UserName Not Found",
                mailid="Mail Id Not Found",
                phone="Phone NumberNot Found"):
    print("Name :",name)
    print("Mail Id :",mailid)
    print("Phone Number :",phone)
userDetails(mailid="mounika@gmail.com",phone=9378521400)

#Variable Length Argument- Type1 (Data store in Tuple)
#Used when you don’t know how many positional arguments
#will be passed.
def linearSearch(*a):
    #print(type(a))
    key = 8
    flag = True
    for i in a:
        if i==key:
            flag = False
            return "Key Present"
    if flag:
        return "Key Not Present"
print(linearSearch(1,2,3,4,5,9,8,7,6))

#Variable Length Argument- Type 2 (Data store in Dictionary)
#Used when you don’t know how many keyword arguments
#will be passed.

def userDetails(**Details):
    print(Details)
    print("Name :",Details["name"])
    print("Mail Id :",Details["mailid"])
    print("Phone Number :",Details["phone"])
userDetails(name="Mounika",mailid="mounika@gmail.com",phone=9378521400)

#Recursion
#A recursive function is a function that calls
#itself in order to solve a problem.
def hi():
    print("HI")
    hi()
hi()

def login():
    name = input("Enter The Username : ")
    pwd  = int(input("Enter The Password : "))
    if name=="admin" and pwd==1234:
        print("Logged In Successfully")
    else:
        print("Invalid Username / Password")
        login()
login()

def factorial(n):
    if n==0 or n==1:
        return 1
    return n * factorial(n-1)
print(factorial(5))

#5! = 1*2*3*4*5
n=5
fact = 1
for i in range(1,n+1,1):
    fact = fact * i
print(fact)

fact = 1 * 1 = 1
fact = 1 * 2 = 2
fact = 2 * 3 = 6
fact = 6 * 4 = 24
fact = 24 * 5 = 120
'''
#lambda function
#A lambda function is a small, anonymous function
#no name).Defined using the keyword lambda.

def square(n):
    print(n**2)
square(3)

output = lambda n : n**2
print(output(3))

#map function
#Applies a given function to each item of an iterable
#(like a list) and returns a new iterable (map object).
#Often used when you want to transform all elements.


def oddOrEven(n):
    if n%2==0:
        return n
a = [1,2,3,4,5,6,7,8,9,10]
print(list(map(oddOrEven,a)))

#filter function
#Applies a function that returns True/False to each item .
#Keeps only the items where the function returns True .
#Often used when you want to select certain elements.

def oddOrEven(n):
    if n%2==0:
        return n
a = [1,2,3,4,5,6,7,8,9,10]
print(list(filter(oddOrEven,a)))





