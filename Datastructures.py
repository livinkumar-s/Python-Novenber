# a="Hello guys I am from tamilnadu!"
# print(len(a))

# print(a[29])
# print(a[6:10])  #6,7,8,9
# print(a[-10:-5])  
# print(a[-10:])  
# print(a[:8])  

# print(a[::-1])


# List

# a=[1,2,3,"Hello","Hi",3.14,False]
# print(len(a))
# print(a[5])
# print(a[a[2]])


# print(a[4])
# a[4]=66

# a.append("last")
# a.extend("hello")
# a.insert(4,100)
# a=[4,3,2,5,6,7,8,8,7] #0
# a.remove(7)
# a.pop(5)
# a.pop()
# print(a.index(8))
# print(a.index(88))
# print(a.count(80))
# a.sort()
# a.reverse()
# print(a)


# Tuple 

a=(2,3,3,1,"Hello",77,88.88,99,101,108)
# print(len(a))

# a[0]=0
# print(a[5])

# print(a.count(5))
# print(a.index(101))

# b=(34,45,99)
# x,y,z=b 

# print(y)

# Set 

# s1={3,4,5,6,7,8,7,6,5,4,3,3,3,5}
# s2={5,6,7,8,9,10,11,12}

# print(s1[4])
# s1.add(56)
# s1.clear()
# print(s1)

# print(s1.union(s2)) #{}
# print(s1.intersection(s2))
# print(s1.difference(s2))
# print(s2.difference(s1))

# Dictionaries


# print(d1['isMarried'])

# d1["age"]=39

# d1["latestMovie"]="Maaman"

# del d1["isMarried"]

# print(d1.keys())
# print(d1.values())
# print(d1.items())

# seq=[22,3,44,55,66]
# d1={"name":"Soori","age":40,"isMarried":True}
# # print(d1["age"])
# for i in d1:
#     print(d1[i])

lis1=[1,2,3,[4,5,6,[7,8,9,["nine","ten","eleven"]]]]

print(lis1[-1][-1][-1][-1][-1])