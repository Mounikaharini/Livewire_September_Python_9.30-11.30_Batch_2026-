#string slicing
s = "Hello Python"
print(s[0:5])
print(s[6:12])
print(s[3:8])
print(s[0:])
print(s[:17])
print(s[:])
print(s[::-1])
print(s[7])
print(s[-1])

#palindrome
m = "max"
if m==m[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")

s="mom"
#count the no of characters in a string
n = 0
for i in s:
    n+=1

#reverse a string
x = ""
for i in range(n-1,-1,-1):
    x = x + s[i]

#check palindrome or not
if s==x:
    print("Palindrome")
else:
    print("Not a palindrome")

#Case conversion
    
data = "HELLO world"
print(data.upper())
print(data.lower())
print(data.title())
print(data.capitalize())
print(data.swapcase())

#Alignment

data = "hi"
print(data.center(10))
print(data.ljust(10))
print(data.rjust(10))
print("20".zfill(5))

#Remove Whitespace
n = "    hi     hi     "
print(n.strip())
print(n.lstrip())
print(n.rstrip())

#spliting and Joining

n = "This is the class"
print(n.split())
n = "Mounika,Python,70Hrs"
m = n.split(',')
print(' '.join(m))
print(n.rsplit(',',1))

#search and replace

x = "welcome to learn python"
print(x.find('l'))
print(x.rfind('l'))
print(x.find('s'))
print(x.index('p'))
#print(x.index('s'))
print(x.replace('o','-'))
print(x.count('n'))
mail = "mounika@gmail.com"
print(mail.endswith("@gmail.com"))
phone = "+91935555555"
print(phone.startswith("+91"))

#Testing
text = "mounikaharini"
print(text.isalpha())
text = "9236974580"
print(text.isdigit())
text = "Live123"
print(text.isalnum())
text = " "
print(text.isspace())
text = "mail@gmail.com"
print(text.islower())
text = "MOUNIKA HARINI"
print(text.isupper())
text = "Hello Hi"
print(text.istitle())

#count the characters
#n = "The class Starts @ 9.30 a.m. and end @ 11.30 p.m."
#Lower =
#Upper =
#Space =
#Digit =
#Symbols =
