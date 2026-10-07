'''
c	i	i<n+1	n%i==0	c+=1	i=i+1

0	1	1<21 ->T20%1==0->T	1	i=1+1
1	2	2<21->T	20%2==0->T	2	i=2+1
2	3	3<21->T	20%3==0->F		i=3+1
2	4	4<21->T	20%4==0->T	3	i=4+1

n = 20
c = 0
for i in range(1,n+1):
    if n%i==0:
        c+=1
print(c)

#2 3 5 7 11 13 17 19 23 29 31 37 39...

#Time complexity : O(n)

n = 150
c = 0
for i in range(1,n+1,1):
    if n%i==0:
        c+=1
if c==2:
    print("Prime")
else:
    print("Not a Prime")

#Time complexity : O(n-2)
n = 150
c = 0
for i in range(2,n):
    if n%i==0:
        c+=1
if c==0:
    print("Prime")
else:
    print("Not a Prime")

#Time complexity : log(n)
    
n = 150
c = 0
for i in range(2,(n//2)+1):
    if n%i==0:
        c+=1
if c==0:
    print("Prime")
else:
    print("Not a Prime")
    
n = 152828
c = 0
while(n>0):
    n//=10
    c+=1
print(c)

i = 1
while(i<=20):
    print(i)
    i+=1

i = 20
while(i>=1):
    print(i)
    i-=1

j = 1
while(j<=5):
    i=1
    while(i<=5):
        print("*",end=" ")
        i+=1
    print()
    j+=1

n = 107438
#(1+0+7+4+3+8)= 23
c = 0
while(n>0):
    r = n%10
    c = c + r
    n//=10
print(c)

n	s	n>0	        r=n%10	s=s+r	n//=10
123	0	123>0 ->T	r=3	s = 3	12
12	3	12>0 ->T	r=2	s = 5	1
1	5	1>0->T	        r=1	s = 6	0
0	6	0>0->F			

number = 153 => digit=3
1^digit => 1
5^digit => 125
3^digit => 27
tot => 153

total = number =>Armstrong

number = 153
number1 = number
number2 = number
digit = 0
while(number>0):
    number//=10
    digit+=1

total = 0
while(number1>0):
    r = number1%10
    total = total + (r**digit)
    number1//=10

if number2 == total:
    print("Armstrong Number")
else:
    print("Not A Armstrong Number")

'''
#jumping control -> break , continue , pass


for i in range(1,11,1):
    if i==5:
        break
    print(i)

for i in range(1,11,1):
    if i==5:
        continue
    print(i)

for i in range(1,11,1):
    if i==10:
        pass
    print(i)


for i in range(10):
    print(i)
else:
    print("Hi")

for i in range(10):
    if i==2:
        break
    print("hello")
else:
    print("hi")












