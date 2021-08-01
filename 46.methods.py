# #class
# class Person:
#     #class attributes
#     address = 'No information'
#     #object attributes
#     #constructor(yapıcı methot)
#     def __init__(self,name,surname,year):# self sınıftan yaratılan objeyi temsil eder
#         self.name = name
#         self.surname=surname
#         self.year=year
#     #instance metotları
#     def intro(self):
#         print('Hello There. I am ', self.name , self.surname)
#     def calculate_age(self):
#         return 2021 - int(self.year)
# #object
# person_object1 = Person('Ömer Faruk','Ballı',2001)#obje yaratıldı.
# person_object2 = Person(name='Bilge',surname='Kara',year='2001')
# person_object2.intro()
# print(f'yasim : {person_object1.calculate_age()}')

class Circle():
    pi=3.14
    def __init__(self,yaricap=1):
        self.yaricap = yaricap
    def cevre_uzunlugu(self):
        return 2 * self.pi * self.yaricap
    def alan(self):
        return self.pi*(self.yaricap**2)
c1 = Circle()# yarıçağı 1
c2 = Circle(75)
print(c1.alan() , c1.cevre_uzunlugu())
print(c2.alan() , c2.cevre_uzunlugu())

