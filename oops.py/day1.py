# class student:
#     pass
# student1=student()
# student2=student()

# print(student1)
# print(student2)

# constructor
# class student:
#     def __init__(self):
#         print ("student created")
# s1=student()


# attribute
# class student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# s1=student("anjali",21)

# print(s1.name)
# print(s1.age)

# method
# class student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def introduce(self):
#      print("my name is",self.name)
    
#     def ages(self):
#      print("my age is", self.age)
# s1=student("anjali",21)
# s1.ages()
# s1.introduce()

  
# encapsulation
# class bankAccount:
#    def __init__(self,balance):
#       self.__balance=balance
#    def show_balance(self):
#       print("balance:",self.__balance)
# account=bankAccount(10000)
# account.show_balance()

#  single inheritance
# class animal:
#     def eat (self):
#         print("animal is eating")
# class dog(animal):
#         def bark(self):
#             print("dog is barking")
# dd = dog ()
# dd.eat()
# dd.bark()
# multi inheritance
# class grandfather:
#     def house(self):
#         print("house")
# class father(grandfather):
#             pass
# class son(father):
#             pass
# s=son()
# s.house()

# multiple
# class father:
#     def skill1(self):
#         print("driving")
# class mother:
#     def skill2(self):
#         print("cooking")
# class child(father,mother):
#     pass
# c=child()
# c.skill1()
# c.skill2()
# polymorphism
# class dog:
#     def sound (self):
#         print("bark")
# class cat:
#     def sound (self):
#         print("meow")
# class monkey:
#     def sound (self):
#         print("chikku")
# animals=[dog(),cat(),monkey()]
# # c1=cat()
# # c1.sound()
# for animal in animals:
#     animal.sound()               
# # abstraction
# from abc import ABC ,abstraction
# class vehicle (ABC):
#     @abstraction
#     def start (self):
#         pass
# class car (vehicle):
#     def start(self):
#         print("car started")
# c=car 
# c.start() 

# class vs instance variable
# class
# class school():
#     student="anjali"
# s1=school()
# print(s1.student)
# # instAnce
# class school():
#     def __init__(self,name):
#         self.name=name
# s1=school("anjali")
# print(s1.school) 

class Employee:
    company="cortube"
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def display(self):
        print(f"Name:{self.name}")
        print(f"salary:{self.salary}")
class Developer(Employee):
    def __init__(self,name,salary,tech):
        super().__init__(name,salary)
        self.tech=tech 
    def display(self):
        super().display()
        print(f"technology:{self.tech}")
s1=Developer("anjali",70000,"software developer")
s1.display()
# super key
class person:
    def __init__(self,name):
class student(person):
    def __init__(self, name,id):
        super().__init__(name)
        self.id=id
s=student("anjali",3245)
print(s.name)
print(s.id)
    


