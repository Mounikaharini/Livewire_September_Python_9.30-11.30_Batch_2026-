#first largest
'''
a = [45, 12, 89, 67, 34, 90]
key = a[0]
for i in a:
    if i>= key:
        key = i
print(key)

#Second Largest without sorting
a = [45, 12, 89, 67, 34, 90]
frs = a[0]
sec = a[0]
for i in a:
    if i>frs:
        sec = frs
        frs = i
print(frs)
print(sec)

#Second Largest with sorting
a = [45, 12, 89, 67, 34, 90]
a.sort()
print(a[-2])

#Find Missing Number
#Given numbers from 1 to N with one number missing,
#find the missing number.

a = [11, 12, 13, 15, 16 , 18]
j = 0

for i in range(a[0],a[-1],1):
    if a[j]!=i:
        print(i)
    else:
        j+=1

#Find Common Elements
#Find the common elements between two tuples.
A = (10, 20, 30, 40)
B = (30, 40, 50, 60)

for i in A:
    if i in B:
        print(i)

'''
#Given employee records as tuples, find the employee with
#the highest salary.
employees = (("E101", "Arun", 45000), ("E102", "Priya", 52000),
             ("E103", "Kumar", 48000))

high = employees[0]
for i in employees:
    if i[2]>high[2]:
        high = i
print(high)

#Find Missing Employee IDs
#Given all employee IDs and the IDs that reported attendance,
#find employees who are absent.

AllIDs ={101, 102, 103, 104, 105}
Present = {101, 103, 105}

print(AllIDs.difference(Present))


