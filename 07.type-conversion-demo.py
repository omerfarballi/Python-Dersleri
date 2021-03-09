""" 
Bir dairenin alanını hesaplayalım.
A = pi*r*r

Bir dairenin çevresini hesaplayalım.
Çevre = 2*pi*r
"""
pi = 3.14    #float
yaricap = float(input("Yarıçap giriniz: "))# değişkene atadığımız değer string bir değerdir bu yüzden veri dönüşümü yapmalıyız.
alan = pi*yaricap*yaricap
cevre = 2*pi*yaricap
print("Girdiğiniz yarıçapa göre alan : ",alan)
print("Girdiğiniz yarıçapa göre çevre : ",cevre)
print("Girdiğiniz yarıçapa göre çevre : "+ str(cevre) +  "  Girdiğiniz yarıçapa göre alan : "+ str(alan) )
