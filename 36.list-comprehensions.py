# number = []
# for x in range(10):
#     number.append(x)
# print(number)

# number = [x for x in range(10)]
# print(number)

# for x in range(10):
#     print(x**2)
# number = [x**2 for x in range(10)]
# print(number)

# number = [x**2 for x in range(10) if x % 3 == 0 ]
# print(number)

for x in range(3):
    for y in range(3):
        print(x,y)
koordinat = [(x,y) for x in range(3) for y in range(3)]
print(koordinat)
