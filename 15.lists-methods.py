number =[0,1,2,3,6,5,98,65,2,3,5]
letters = ["a","b","c","k","p","ü","k","a"]
values = min(number)
values = min(letters)
values = max(number)
values = max(letters)

values =number[:5]

number[5] = 9999

number.append(letters)
number.insert(0,963946556468)

number.pop()
number.pop(0)

number.remove(9999)

number.sort(reverse=True)
# number.reverse()
letters.sort()
letters.reverse()
# number.clear()
print(len(number))

print(number)
print(letters)
print(number.count(3))