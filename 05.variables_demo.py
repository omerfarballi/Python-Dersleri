'''
        İsim soyisim tc numarası adres doğum yılını tanımlamak için değişkenler ata
İsim tanımla
Soyisim tanımla
TC numarası tanımla
Adresi tanımla
Doğum yılı tanımla
        Yaşını bul
        Aylık harcamaların ve aylık gelirin arasındaki farkı bulalım
Maaş bilgisi 14000
Mutfak giderleri 3000
Faturalar 1000
kira tutarı 1500
Okul masrafları 2500
Aylık kredi tutarı 5000 

'''
musteri_adi = "Enes"
musteri_soyisimi = "Çiftçi"
tc_no = '16786578388'
musteri_adresi = ' Bursa İnegöl '
dogum_yili = "1995"
musteri_yasi = 2021 - int(dogum_yili)
print(musteri_yasi)
maasBilgisi = 14000
mutfakMasrafi = 3000
faturalar = 1000
kiraTutarı = 1500
okulMasraflari = 2500
kredi_tutari = 5000
cepte_kalan_para = maasBilgisi-(mutfakMasrafi+faturalar+kiraTutarı+okulMasraflari+kredi_tutari)
print("Ay sonu cepte kalan para : ", cepte_kalan_para)

