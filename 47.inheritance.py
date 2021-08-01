#    Inheritance     (kalıtım)      (Miras alma)
#Person => name ,lastname, eat(),drink(),run(),sleep()
# Student(Person)   Worker(Person)

class Person():
    def __init__(self,fname,lname):
        self.first_name = fname
        self.last_name = lname
        print('person created')
    def eat(self):
        print('I am eating')
    def who_am_i(self):
        print('I am a person')
class Student(Person):
    def __init__(self,fname,lname):
        Person.__init__(self,fname,lname)#normalde student init person initi ezer person init çalışması için bu kod gerekli ve diğer metotlar içinde gerekli
        print('student created')
    #      override
    def who_am_i(self):
        super().who_am_i()#16. satırdaki ile aynı işi yapıyor bir alternatif
        print('I am a student')
# p1 = Person()
s1 = Student('Ömer Faruk','Ballı')
s1.who_am_i()
s1.eat()

