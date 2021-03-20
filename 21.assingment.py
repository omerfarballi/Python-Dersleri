# x = 1
# y = 2
# z = 3
x,y,z = 1,2,3

# x,y = y,x

x += 9      # x = x + 9
x -=  9     # x = x - 9
x *= 9      # x = x * 9
x /= 10     # x = x / 9
x %= 2      # x = x % 9
x //= 0.49  # x = x // 9
x **= y  # x = x ** y

values = 9,99,999,9999,99999
x,y,*z = values
print(values)
print(type(values))
print(x,y,z)
print(x,y,z[2])

