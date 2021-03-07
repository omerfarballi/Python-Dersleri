klavye = 50
gozluk = 300
kdv_oranı= 0.18
kdvli_klavye = klavye+(klavye*kdv_oranı)
kdvli_gozluk = gozluk+(gozluk*kdv_oranı)
print("kdvli gözlük : ",kdvli_gozluk,"kdvli klavye: ",kdvli_klavye)
# değişken isimi verirken dikkat etmemmiz gereken durumlar:
# sayı ile başlayamaz

number1 = 99
print(number1)
number1 = 999
print(number1)
number1 += 1
number1 -= 1
number1 /= 9
number1 *= 9

print(number1)
# age AGE 
age = 18
AGE = 81
Age =55
print(age,AGE,Age)
#Türkçe karakter kullnamayalım
age = 18            #int
money = 85.5        #float
name = "Ömer"       #str(string)
isStudent = True    #Bool 
age , money , name , isStudent = (18,85.6,'Ömer Faruk ',True )

number1 = '25'
number2 = '52'
print(number1+number2) # 77 => 2552
# Boşluk koyamayız
#ogrenci mi (Böyle bir değişken atayamayız)

