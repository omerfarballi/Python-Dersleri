lst = [1,2,3]
my_string = ' String '
print(len(lst))
print(len(my_string))
print(type(lst))
print(type(my_string))
class Movie():
    def __init__(self,name,duration,rating):
        self.name = name
        self.duration = duration
        self.rating = rating
    def __str__(self):
        return f'filmin adı :{self.name}'
    def __len__(self):
        return self.duration
    def __del__(self):
        print('Film objesi silindi')

m1 = Movie('film adı',180,8.5)
print(type(m1))
print(str(lst))
print(str(m1))
print(len(m1))



