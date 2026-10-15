'''
sentence = input("Enter a sentence : ")
#count the spaces

space = 0
for i in sentence:
    if i.isspace():
        space+=1
    
print("Total Number of Spaces : ",space)

#count the ocurrence
target_variable = input("Enter a Target Character : ")
count = 0
for i in sentence:
    if i==target_variable:
        count+=1
print("Total Number of Character : ",count)

#remove space
ch = "p t y    r r e e "
print(ch)
ch = ch.split()
print(ch)
ch = ''.join(ch)
print(ch)

#String formatting
name = "Mounika"
course = "Python"
duration = 70
print("Name :",name,"Course :",course,"Duration :",duration)

#F-string
print(f"""My name is {name}
I'm Currently Doing {course} Course
That Takes the Duration Of {duration + 50} Hours
""")

#format()
print("""My name is {}
I'm Currently Doing {} Course
That Takes the Duration Of {} Hours
""".format(name,course,duration))

print("""My name is {0}
I'm Currently Doing {1} Course
That Takes the Duration Of {2} Hours
""".format(name,course,duration))

print("""My name is {n}
I'm Currently Doing {c} Course
That Takes the Duration Of {d} Hours
""".format(n=name,c=course,d=duration))

#Percentage
#for string = %s
#for integer = %d
#for float = %f

name = "Mounika"
course = "Python"
duration = 70
cgpa = 8.6

print("""My name is %s
I'm Currently Doing %s Course
That Takes the Duration Of %d Hours
I'm secured %.2f in my academics
"""%(name,course,duration,cgpa))
'''

#List
# Create a List
a = [1, 2, 3, 4, 5]
print("Original list:", a)
# Access Elements
print("First element:", a[0])
print("Last element:", a[-1])
print("Particular element:", a[2:5])
print("Particular element:", a[2:])
print("Particular element:", a[:])
print("Particular element:", a[:5])
#adding an element
a.append(20)
print(a)
a.extend([20,20])
print(a)
a.insert(2,30)
print(a)






















