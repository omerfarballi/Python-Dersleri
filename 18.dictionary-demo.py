"""
    ogrenciler = {
        '100': {
            'ad': 'Enes',
            'soyad': 'Çiftçi',
            'telefon': '552 000 00 01'
        },
        '200': {
            'ad': 'Emre',
            'soyad': 'Çimer',
            'telefon': '532 000 00 02'
        },
        '300': {
            'ad': 'Mehmet',
            'soyad': 'Bozkurt',
            'telefon': '532 000 00 03'
        },
    }
    1- Bilgileri verilen öğrencileri kullanıcıdan aldığınız bilgilerle
        dictionary içinde saklayınız.
    2- Öğrenci numarasını kullanıcıdan alıp ilgili öğrenci bilgisini gösterin.
"""
ogrenciler = {}
number = input("Öğrencinin numarısı: ")
name = input("Öğrencinin ismi: ")
surname = input("Öğrencinin soyadı: ")
phone = input("Öğrencinin telefon numarası: ")
ogrenciler.update({
    number:{
        "ad":name,
        "soyisim":surname,
        "telefon":phone
    }
})
number = input("Öğrencinin numarısı: ")
name = input("Öğrencinin ismi: ")
surname = input("Öğrencinin soyadı: ")
phone = input("Öğrencinin telefon numarası: ")

ogrenciler.update({
    number:{
        "ad":name,
        "soyisim":surname,
        "telefon":phone
    }
})
number = input("Öğrencinin numarısı: ")
name = input("Öğrencinin ismi: ")
surname = input("Öğrencinin soyadı: ")
phone = input("Öğrencinin telefon numarası: ")

ogrenciler.update({
    number:{
        "ad":name,
        "soyisim":surname,
        "telefon":phone
    }
})
ogrenci_no = input("Hangi öğrencinin bilgisini öğrenmek istiyorsunuz? ")
print(f"Öğrencinin numarası{ogrenci_no}\n ismi :{ogrenciler[ogrenci_no]['ad']}\n soyismi :{ogrenciler[ogrenci_no]['soyisim']}\n telefon numarası : {ogrenciler[ogrenci_no]['telefon']}")


