# value type => string,number(intiger and float)      (call by value)
x = 10
y = 12

x = y 
y = 12+y

# print(x,y)

# reference type => list, class   (call by reference)
liste1 = ["Ömer","Bilge"]
liste2 = ["Ömer","Bilge"]
liste1 = liste2
liste2[0] = "Faruk"
print(liste1,liste2)
