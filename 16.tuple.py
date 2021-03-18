list = [0,1,2,3,"abcde"]
tuple = (0,1,2,3,3,"abcde")
# print(type(tuple))
# print(type(list)) 
# print(list[2])
# print(tuple[2])
# print(len(tuple))

list = [0,1,2,3,4,5,6,7]
tuple = (0,0,0,1,2,3,4,5,6,7)
numbers = (1,2,3,4,5,6,7) + tuple
print(numbers)
list[0] = "ömer"
# tuple[1] = "85"
print(tuple.count(0))
print(tuple.index(1))

print(list,tuple)