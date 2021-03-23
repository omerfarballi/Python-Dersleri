''' 1 ) Girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz.'''
# sayi = float(input("0 ile 100 arasında olduğunu bilmek istediğiniz bir sayı giriniz : "))
# if (sayi>0 and sayi<100):
#     print(f"Girmiş olduğunuz {sayi} 0 ile 100 arasındadır.")
# else:
#     print(f"Girmiş olduğunuz {sayi} 0 ile 100 arasında değildir.")

''' 2 ) Bir öğrencinin 2 yazılı 1 sözlü notunu alıp hesaplanan ortalamaya göre
        not aralığına karşılık gelen not bilgisini yazdırınız.
        0-44  => 1
        45-54  => 2
        55-69  => 3
        70-84  => 4
        85-100 => 5
        '''
# yazili1 = float(input("1.yazılı : "))
# yazili2 = float(input("2.yazılı : "))
# sozlunotu = float(input("Sözlü notu : "))
# not_ortalama = (yazili1+yazili2+sozlunotu)/3
# if (not_ortalama>=0 and not_ortalama<=44.9999):
#     print(f"Not ortalamanız {not_ortalama} notunuz : 1")
# elif (not_ortalama>=45 and not_ortalama<=54.9999):
#     print(f"Not ortalamanız {not_ortalama} notunuz : 2")
# elif (not_ortalama>=55 and not_ortalama<=69.9999):
#     print(f"Not ortalamanız {not_ortalama} notunuz : 3")
# elif (not_ortalama>=70 and not_ortalama<=84.9999):
#     print(f"Not ortalamanız {not_ortalama} notunuz : 4")
# elif (not_ortalama>=85 and not_ortalama<=100):
#     print(f"Not ortalamanız {not_ortalama} notunuz : 5")
# else:
#     print("Girmiş olduğunuz değerle göre bir not hesaplaması yapılamamaktadır.")

""" 3 ) Girilen bir sayının pozitif çift sayı(MOD ( % )) olup olmadığını kontrol ediniz. """
# sayi = float(input("Sayı :"))
# if (sayi>0 and sayi % 2 == 0):
#     print(f"Girdiğiniz {sayi} sayısı hem pozitif hem de çift sayıdır.")
# elif (sayi>0):
#     print(f"Girdiğiniz {sayi} sayısı sadece pozitif sayıdır.")
# elif (sayi<0 and sayi % 2 == 0):
#     print(f"Girdiğiniz {sayi} sayısı hem negatif ve çift bir sayıdır.")
# else :
#     print(f"Girdiğiniz {sayi} sayısı hem negatif hem de tek sayı değildir.")

""" 4 ) Girilen 3 sayıyı büyüklük olarak karşılaştırınız."""
# numbur1 = float(input("Birinci sayı : "))
# numbur2 = float(input("İkinci sayı : "))
# numbur3 = float(input("Üçüncü sayı : "))
# if (numbur1 > numbur2 and numbur1 > numbur3):
#     print("Birinci sayı en büyük sayıdır.")
# elif (numbur1 < numbur2 and numbur2 > numbur3):
#     print("İkinci sayı en büyük sayıdır.")
# elif (numbur3 > numbur2 and numbur1 < numbur3):
#     print("Üçüncü sayı en büyük sayıdır.")
# else :
#     print("Girdiğiniz sayılar hepsi eşit değerlerden oluşmaktadır.\nBunları kontrol ettikten sonra tekrar deneyiniz.")

""" 5 ) Kullanıcıdan 2 vize (%70) ve final (%30) notunu alıp ortalama hesaplayınız.
        Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.
            a-) Ortamalama 50 olsa bile final notu en az 50 olmalıdır.
            b-) Finalden 70 alındığında ortalamanın önemi olmasın."""
vize1 = float(input("1. Vize Notu : "))
vize2 = float(input("2. Vize Notu: "))
final = float(input("Final Notu : "))
ortalama = ((vize1+vize2)/2*0.7) + (final*0.3)
#1.Durum
# result = ortalama>50 and final>50
# if (ortalama>=50):
#     if (final>=50):
#         print(f"Öğrencinin ortalaması {ortalama} ve geçme durumu : başarılı.")
#     else :
#         print(f"Öğrencinin ortalaması {ortalama} ve geçme durumu : başarısız.(Finalden en az 50 almalısınız yoksa geçmezsiniz.)")
# else:
#     print(f"Öğrencinin ortalaması {ortalama} ve geçme durumu : başarısız.")
#2.Durum
# result = ortalama> 50 or final>=70
# if (ortalama>=50):
#     print(f"Öğrencinin ortalaması {ortalama} ve geçme durumu : başarılı.")
# else:
#     if(final>=70):
#         print(f"Öğrencinin ortalaması {ortalama} ve geçme durumu : başarılı.Final notunuz 70 ve üzeri olduğu geçiyorsunuz.")
#     else:
#         print(f"Öğrencinin ortalaması {ortalama} ve Geçme durumu : başarısız.")


