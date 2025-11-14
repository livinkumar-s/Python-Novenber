# i=0

# while i<5: 
#     print("Step1")
#     print("Step2")
#     print("Step3")
#     print("--------------------")
#     i-=1

# no of execution: infinite
# i:0,-1,-2,-3,-4,-5
# executions:1,2,3,4,5,6

# a="Hello world"

# print(len(a))
# print(a[10])

# str=""

# [0,1,2,3,4]

# for i in range(5):
#     print("Step1")
#     print("Step2")
#     print("Step3")
#     print("--------------------")

# print(list(range(9)))
# print(list(range(3,20,3)))

# for i in range(20,50,5):
#     print(i)

# for i in range(0,101):
#     print(i)

# 100
# 99
# 98
# .
# .
# .
# 0

# for i in range(100,-1,-1):
#     print (i)

# [0,1,2,3,.....9]

# for i in range(10):
#     if i==5:
#         break
#     print(i)
#[0,1,2,3....49,50,51,.....99]

# for i in range(100):
#     if i==50:
#         continue
#     print("---------")
#     print(i)
#     print("----------")

# for i in range(100):
#     print(i)

# secret=33

# while True:
#     guessed_value=int(input("Guess the 2 digit number: "))
#     if guessed_value==secret:
#         print("You got it!")
#         break
#     else:
#         print("Try again!")

# i  -->[1,2,3,4,5]
# j  -->[1,2,3,4,5]

# for i in range(1,6):
#     for j in range(1,6):
#         if i+j==6:
#             print("* ",end="")
#         elif i==j:
#             print("* ",end='')
#         else:
#             print("  ",end="")
#     print()

# for i in range(1,6):
#     for j in range(1,6):
#         if j==1:
#             print("* ",end="")
#         elif j==5:
#             print("* ",end='')
#         elif i==j and i<=3:
#             print("* ",end='')
#         elif i+j==6 and i<=3:
#             print("* ",end='')
#         else:
#             print("  ",end="")
#     print()

size=int(input("Enter odd size: ")) #5

for i in range(1,size+1): #6
    for j in range(1,size+1):
        if j==1:
            print("* ",end="")
        elif j==size:
            print("* ",end='')
        elif i==j and i<=(size+1)/2:
            print("* ",end='')
        elif i+j==size+1 and i<=(size+1)/2:
            print("* ",end='')
        else:
            print("  ",end="")
    print()

# * * * * * 
