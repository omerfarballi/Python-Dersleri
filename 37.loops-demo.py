'''
    1-10 arasında rastgele üretilecek bir sayıyı aşağı yukarı ifadeleri ile buldurmaya çalışın. (hak = 5)
    ** "random modülü" için "python random" şeklinde arama yapın.
    ** 100 üzerinden puanlama yapın. Her soru 20 puan.
    ** Hak bilgisini kullanıcıdan alın ve her soru belirtilen can sayısı 
        üzerinden hesaplansın.
'''
import random
sayi = random.randint(0,10)
can = int(input("Tahmin uygulaması için kaç hakkınız olmasını istersiniz ? "))
hak = can
sayac = 0
while hak > 0:
    hak -= 1
    sayac += 1
    tahmin = int(input("Tahmin için bir intiger tipinde değer giriniz : "))
    if tahmin == sayi:
        print("Tebrikler {sayac}. tahminiz doğru. Toplam puanınız : ",100-(100/can)*(sayac-1))
        break
    elif tahmin > sayi:
        print(" Aşağı ")
    else:
        print(" Yukarı")
    if hak == 0:
        print(f"Hakkınız bitti. Tutulan sayı : {sayi}")
    



