# class MyClass:
#     x = 5

# p1 = MyClass()
# p2 = MyClass()

# print(p1.x)
# print(p2.x)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greeting(self):
        print("Hello " + self.name)

p1 = Person("Farhan", 20)
p2 = Person("Mardadi", 24)

# print(p1.name)
# print(p1.age)
# print(p2.name)
# print(p2.age)

p1.greeting()
p2.greeting()