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

secret=33

while True:
    guessed_value=int(input("Guess the 2 digit number: "))
    if guessed_value==secret:
        print("You got it!")
        break
    else:
        print("Try again!")