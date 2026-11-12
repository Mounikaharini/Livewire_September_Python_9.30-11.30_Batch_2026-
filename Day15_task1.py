'''
#Read Mode

file = open("sample1.txt",'r')
print(file.read())
print(file.read(20))
for i in range(5):
    print(file.readline(),end="")
print(file.readlines())

#Write Mode

file = open("sample1.txt",'w')
file.write("Helloo............")
print("File Content is Updated")
file.close()
file.write("Bye............")
print("File Content is Updated")
file.close()

#Append Mode
file = open("sample1.txt",'a')
file.write("Helloo............")
print("File Content is Updated")
file.write("Bye............")
print("File Content is Updated")
file.close()

#File Does Not Exist
file = open("sample2.txt",'a')
file.write("Helloo............")
print("File Content is Updated")
'''
#Exception Handling
'''
a = int(input("Enter Data : "))
if a%2==0:
    print("Even")
else:
    print("Odd")

print(b)

a = [1,2,3,4]
print(a[9])
'''


print("Welcome to our prgm")
try:
    c = {1:"hi",2:"bye"}
    print(c[3])
except Exception as e:
    print(e, "Key is Not in A Dictionary")
finally:
    print("I'm Finally Block")
print("Thank You for coming")




















