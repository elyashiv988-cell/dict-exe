# 1
tags= {'python', 'bash', 'git', 'python'}
print(tags)
# 2
tags.add("linux")
print(tags)
#3
tags.discard("bush")
print(tags)
tags.discard("aaa")
#4 
a = {1, 2, 3}
b = {3, 4, 5}
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
# 5
print(True) if "git" in tags else print(False)
#6
point=(10,20)
print(point)
print(point[:1:])
print(point[1:])
# 7
#point[0]=99
print(point)
# 8
rgd= (255, 128, 0)
r=rgd[0]
print(r)
g=rgd[1]
print(g)
d=rgd[2]
print(d)
# 9
coords=(1, 2, 3, 2, 1)
print(coords.count(2))
print(coords.index(3))
# 10
list1=(1,2,3)
set1=(1,2,3)
tuple=(1,2,3)
print(list)
print(set)
print(tuple)
# list allow to change the values. 

#part 2

#1 
a = {1, 2, 3}
b = {3, 4, 5}
print(a.issubset(b))
print(a. issuperset(b))
# 2
pairs = [(1, 'a'), (2, 'b'), (3, 'c')]
print(pairs[1])
#3
list1=[1,2,3,4,3,2,1,2,3,4,]
list2=set(list1)
print(list2)
list3=list(list2)
print(list3)
# 4
set_1={1,2,3,4,5,}
set_2={7,8,8,9}
print(set_1.symmetric_difference(set_2))
#5
# because lists are mutible but tuple and set are immutible so they can connect each other. 
set_1={7,8,8,9}
tuple_1=(1,2,3)
list_1=[4,5,6]
print(list1.append(tuple_1))
print(tuple_1+set1)