#class
class Person:
    #class attributes
    address = 'No information'
    #object attributes
    #constructor(yapıcı methot)
    def __init__(self,name,surname,year):# self sınıftan yaratılan objeyi temsil eder
        self.name = name
        self.surname=surname
        self.year=year
        print('init metotu çalıştı ')
    #metotları

#object
person_object1 = Person('Ömer Faruk','Ballı',2001)#obje yaratıldı.

print(person_object1.year,person_object1.address)# accessing object attributes
person_object2 = Person(name='Bilge',year='Kara',surname='2001')
person_object2.address = 'İstanbul'#updating
print(person_object2.year,person_object2.address)# accessing object attributes
# print(type(person_object1))
# print(person_object1)
