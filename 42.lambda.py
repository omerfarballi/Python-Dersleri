#def square(number): return number**2
# square = lambda num : num**2
number_list = [2,4,6,8,10,3,9,57]
# result = list(map(lambda num : num**2,number_list))
# result = list(map(square,number_list))

# for item in map(square,number_list):
#     print(item)
# result = square(85)
def check_even(num) : return num%2==1
result = list(filter(check_even,number_list))



print(result)