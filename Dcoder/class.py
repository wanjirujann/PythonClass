class Student:
    school = "Akirachix"
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
jann = Student(name="jann", age=21)
wendy = Student(name="wendy", age=22)

print(jann.school)
print(jann.name)
print(wendy.school)
print(wendy.age)
print("******************************")

class Car:

    def __init__(type, model,plate):
        type.model = model
        type.plate = plate
        
ferrari = Car(model="ferrari", plate="VGt06")
classic = Car(model="classic", plate="271G")

print(ferrari.model)
print(ferrari.plate)
print(classic.model)
print(classic.plate)

print("*******************************")

class Dog:

    def __init__(self, breed, home):
        self.breed = breed
        self.home = home
    
bulldog = Dog(breed="bulldog", home="kennel")
beagle = Dog(breed="beagle", home="shelter")
    
print(bulldog.breed)
print(bulldog.home)
print(beagle.breed)
print(beagle.home)

print("*******************************")

class BankAccount:
    
    def __init__(self, owner, number):
        self.owner = owner
        self.number = number
    
jann = BankAccount(owner="jann", number=1110010111)
carole = BankAccount(owner="carole", number=1071100001)

print(jann.owner)
print(jann.number)
print(carole.owner)
print(carole.number)