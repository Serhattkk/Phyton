# #class

# class Person:
#     pass
#     #class attributes
#     address = 'No information'
#     #constructor(yapıcı metod)
#     def __init__(self, name, year):

#         #object attributes
#         self.name = name
#         self.year = year
      
#     #instance methods
#     def intro(self):
#         print('Hello')
    
#     def calculateage(self):
#         return 2022 - self.year



# #object (instance)
# p1 = Person('Serhat', 2007)
# p2 = Person('Merve', 2006)

# p1.intro()
# print(f'name:{p1.name} and age: {p1.calculateage()}')
# print(f'name:{p2.name} and age: {p2.calculateage()}')


import re


class Circle:
    pi = 3.14
    
    def __init__(self, yarıcap=1):
        self.yarıcap = yarıcap
    
    def cevre_hesap(self):
        return 2*self.pi + self.yarıcap
    
    def alan_hesap(self):
        return self.pi * (self.yarıcap**2)
    
kk = int(input('Yarıçap?:'))
c1 = Circle(kk)

print(f'alan = {c1.alan_hesap()}\n çevre = {c1.cevre_hesap()}')