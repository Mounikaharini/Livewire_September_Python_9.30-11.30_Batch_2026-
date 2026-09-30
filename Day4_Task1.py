'''
#Greater of three
a = int(input("Enter value 1 :"))
b = int(input("Enter value 2 :"))
c = int(input("Enter value 3 :"))
if (a>=b and a>=c):
    print(a)
elif (b>=a and b>=c):
    print(b)
else:
    print(c)

#Swapping
a = int(input("Enter value 1 :"))
b = int(input("Enter value 2 :"))
print("A : ",a)
print("B : ",b)
a = a+b #a=15
b = a-b #b=15-5 =>10
a = a-b #a=15-10=>5
print("A : ",a)
print("B : ",b)

#a,b=b,a

a = 10
b = 20
c = a #c=10
a = b #a=20
b = c #b=10

a = 12345
a = a//100 # a = 123
print((a%10)**2)

a = 23
b = a%10 #b=3
a = a//10 #a=2
'''
#A -> 65 , Z ->90
#a -> 97 , z ->122
#0 -> 48 , 9 ->57
#space -> 32

a = 923
if (a>=100 and a<=999):
    if (a%10==0):
        print("Yes")
    else:
        print("No")
else:
    print("No")













