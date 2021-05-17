"""
    Girilen bir sayının asal saı olup olmadığını kontrol ediniz.
                    *** Asal sayılar sadece kendilerine ve 1'e bölünebilen sayılardır.*** 3 asaldır. 1 sayısı asal değildir.
"""
number = int(input("Sayi : "))
asalmi =  True
if number == 1:
    asalmi = False

for i in range(2,number):
    if (number % i == 0):
        asalmi = False
        break
if asalmi:#True False 
    print(f"{number} sayısı asaldır.")
else:
    print(f"{number} sayısı asal değildir.")