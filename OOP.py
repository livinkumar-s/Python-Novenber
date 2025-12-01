class Cat:
    def __init__(self):
        self.name="Tommy"
        self.legs=4

    def sayHello(self):
        print("Meoww.....")
    def run(self):
        print("Tommy is running!")


class Car(Cat):
    def __init__(self):
        self.name="Audi"
    
    def start(self):
        print("Car is StARTING")
    
    def stop(self):
        print("Car is stopping")

car1=Car()
# car1.sayHello()
print(car1.name)

# Cat --> 2 attributes --> 2 methods
# Car --> 1 attribute --> 2 methods

# c1=Cat()
# c2=Cat()
# c3=Cat()
# c4=Cat()

# car1=Car()
# car2=Car()

# c2.sayHello()
# print(c4.name)

# car1.sayHello()

# a=99
# b="99"
# c=Car()

# print(type(c)) #<class 'str'>

# a="Hello"
# b=[1,2,3,4,5]
# c=Car()
# d=Cat()


# print(type(d))



