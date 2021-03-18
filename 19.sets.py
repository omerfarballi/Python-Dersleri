fruits = {"banana","apple","orange"}
# print(fruits[0]) indekslenemez
# print(fruits)
for x in fruits:
    print(x)
fruits.add("blackberry")
fruits.update(["berry","blueberry"])
fruits.update(["blueberry"])

# print(fruits)
# my_list =[0,0,11,1,1,1,12,2,2,2,2,3]
# print(set(my_list))

fruits.remove("berry")
print(fruits)

fruits.discard("apple")
print(fruits)

fruits.pop()
print(fruits)
fruits.clear()
print(fruits)
