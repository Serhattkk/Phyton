#Inheritance( Kalıtım): Miras Alma

# Person => name, lastname, age ,eat(), run(), drink()
# Student(Person), Teacher(Person)

class Person():
    def __init__(self, name, surname, age):
        self.firstname = name
        self.surname = surname 
        self.age = age
        print('Person ready')
class Student(Person):
    def __init__(self, name, surname, age):
        Person.__init__(self, name, surname, age)
        print('Student ready')

p1 = Person('Serhat', 'Kayır', 15)
s1 = Student('Merve', 'Turgut', 16)
 



print(f'Person name: {p1.firstname + " " + p1.surname}\n Age: {p1.age}')
print(f'Person name: {s1.firstname + " " + s1.surname}\n Age: {s1.age}')

