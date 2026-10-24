'''
a = [1,2,"hi"]
print(a)
a.append(10)
print(a)
a.extend([10,20,30])
print(a)
a.insert(2,'k')
print(a)
print(a[2])
print(a[0:5])
print(a[0:])
print(a[::-1])
for i in a:
    print(i)
a.remove("hi")
print(a)
a.pop()
print(a)
a.pop(2)
print(a)
print(a.index(2))

a=[1,2,3]
b=a
c=a.copy()
print(a)
print(b)
print(c)
b.append(4)
c.append(5)
print(a)
print(b)
print(c)

for i in range(5):
    print(i**2)
print([i**2 for i in range(5)])

#TUPLE
a = (1,2,3)
b = (4,6)
c = a + b
print(c)
print(tuple("py"))
details = ("python",5,"9.30")
course , count , time = details
print(course)
print(count)
print(time)

#Set
s = {1,1.0,2,14,2,True,"hi",14,29,3,5,6,}
print(s)
s.add(1.0)
print(s)
s.update([12,3,4,5,5,32,4,6])
print(s)
s.update({21,22,23})
print(s)

#remove duplicates in a list
a = [1,2,1,2,3,4,3,4,5]
#print(set(a))
b = []
for i in a:
    if i not in b:
        b.append(i)
print(b)

#linear search
a = [2,3,2,4,66,7,9,3,4,5]
key = 9
length = 0
flag = False
for i in a:
    length+=1
for i in range(0,length):
    if a[i]==key:
        print("Element Found in index : ",i)
        flag = True
        break
if flag == False:
    print("Element Not Found in the List")

#binary search

a = [1,4,6,8,9,12,16,26,29,31]
key = 26
length = 0
for i in a:
    length+=1
    
mid = length//2

s = {1,2,3} 
#s.remove(1)
#s.remove(4)
s.discard(1)
s.discard(4)
s.pop()
print(s)

s1 = {1,2,3,4}
s2 = {2,4,6,8}
print(s1.union(s2))
print(s1.intersection(s2))
#s1.intersection_update(s2)
#print(s1)
print(s1.difference(s2))
print(s2.difference(s1))
print(s1.symmetric_difference(s2))

a = {1,2,3,4,5,6}
b = {1,2,9}
c = {4,5}

print(a.issuperset(b))
print(a.issuperset(c))

print(b.issubset(a))
print(c.issubset(a))

print(a.isdisjoint(b))
print(c.isdisjoint(b))
'''
#dictionary

k = {1:"Id1",2:"Id2",1:"Id3"}
print(k)
print(k.keys())
print(k.values())
print(k.items())
print(k[1])
print(k.get(1))
k[1]="Id1"
print(k)
k.update({3:"Id3"})
print(k)
k.pop(3)
print(k)
for i in k.keys():
    print(i," : ",k[i])
l = {"user1":{"username":"m@gmail.com","password":"m@2026"},
     "user2":{"username":"p@gmail.com","password":"p@2026"},
     "user3":{"username":"r@gmail.com","password":"r@2026"},
     "user4":{"username":"a@gmail.com","password":"a@2026"},
     "user5":{"username":"k@gmail.com","password":"k@2026"}
     }
print(l["user1"])
print(l["user1"]["username"])














