# range()
# number = []
# for x in range(0,10,2):
#     number.append(x)
# print(number)
# print(list(range(0,10000,2)))

#enumerate
# index = 0
name = 'Ömer'
for index,letter in enumerate(name) :

    print(index,' ',letter)
    # index += 1
#zip
liste1 = [0,1,2,3,4,5,6]
liste2 = ['a','b','c','d','e','f','g']
print(list(zip(liste1,liste2)))

