'''
n = int(input("Enter a number :"))
if n>0:
    print("positive")
else:
    print("Negative")
    
n = int(input("Enter a number :"))
if n>0:
    print("positive")
elif n==0:
    print("Zero")
else:
    print("Negative")

#check whether the given number is odd / even
n = int(input("Enter a number :"))
if n%2==0:
    print("Even")
else:
    print("Odd")

#check whether the given character is vowel or consonants
ch = input("Enter a character : ")
if (ch>='a' and ch<='z')or(ch>='A' and ch<='Z'):
    vowel = ['a','e','i','o','u','A','E','I','O','U']
    if ch in vowel:
        print("Vowel")
    else:
        print("Consonant")
else:
    print("Invalid Character")

#check the given number is even and lies between the range of 1 to 100
#constraints
#if a number is even lies between 1 to 100 -> Output is Yes
#if a number is odd lies between 1 to 100 -> Output is No
#if a number is even lies not between 1 to 100 -> Output is No
#if a number is odd lies not between 1 to 100 -> Output is No

n = int(input("Enter a number : "))
if(n>=1 and n<=100) and (n%2==0):
    print("Yes")
else:
    print("No")

#check the given character is Capital Letter/ Small Letter/ Number/ Symbol
#constraints
#If the character is Capital Letter -> output is "1"
#If the character is Small Letter -> output is "2"
#If the character is Number -> output is "3" -> input is only b/w(0-9)
#If the character is Symbol -> output is "4"

ch = input("Enter a character")
if (ch>='A' and ch<='Z'):
    print(1)
elif (ch>='a' and ch<='z'):
    print(2)
elif (ch>='0' and ch<='9'):
    print(3)
else:
    print(4)
'''





















