'''
for i in range(1,11):

    print("hi")
for variable in range(start,end+1,inc/dec):
    #block of code

for i in range(1,6,1):
    print(i)

#2 4 6 8 10

for i in range(2,11,2):
    print(i)

# 3 6 9 12 15
for i in range(3,16,3):
    print(i)

3 x 1 = 3
3 x 2 = 6
.........
3 x 10 = 30

for i in range(1,11,1):
    print("3 x",i,"=",i*3)

3 x 1 = 3
3 x 3 = 9
3 x 5 = 15
3 x 7 = 21
3 x 9 = 27
'''
#factorial
'''
5!=1*2*3*4*5
4!=1*2*3*4

n = int(input("Enter a number : "))
s = 1
for i in range(1,n+1,1):
    #print("s = ",s,", i = ",i,", s * i =",s*i)
    s = s * i
print("Factorial of",n,":",s)

# 5 4 3 2 1
for i in range(5,0,-1):
    print(i)

#10 8 6 4 2
    
for i in range(10,1,-2):
    print(i)

#sum of N natural numbers
#n=5 =>1+2+3+4+5=15
#n=3 =>1+2+3=>6

n = int(input("Enter a number : "))
s = 0
for i in range(1,n+1):
    s = s + i
print(s)


#sum of even numbers in a given range
n = 20
c = 0
for i in range(2,n+1,2):
    c+=i
print(c)
'''
#nested loop
#* * * * *
#* * * * *
#* * * * *
#* * * * *
#* * * * *

for j in range(10):
    for i in range(10):
        print("*",end=" ")
    print()

