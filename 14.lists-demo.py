# 1-  "Bmw, Mercedes, Tesla, Fiat" elemanlarına sahip bir liste oluşturunuz.
arabalar = ['Bmw','Mercedes','Tesla','Fiat']
# 2-  Liste Kaç elemanlıdır ?
result = len(arabalar)
# 3-  Listenin ilk ve son elemanı nedir ?
result = arabalar[0]
result = arabalar[-1]
result = arabalar[3]

# 4-  Fiat değerini Toyota ile değiştirin.
arabalar[-1] = 'Toyota'
result = arabalar
# 5-  Mercedes listenin bir elemanı mıdır ?
result = 'Mercedes' in arabalar
# 6-  Porsche listenin bir elemanı mıdır ?
result = 'Porsche' in arabalar

# 7-  Listenin -2 indeksindeki değer nedir ?
result = arabalar[-2]
result = arabalar[2]
# 8-  Listenin ilk 3 elemanını alın.
result = arabalar[0:3]
result = arabalar[:3]

result = arabalar[-2:]
# 9-  Listenin son 2 elemanı yerine "Toyota" ve "Renault" değerlerini ekleyin.
arabalar[-2:] = ['Toyota',"Renault"]
result = arabalar
# 10- Listenin üzerine "Audi" ve "Nissan" değerlerini ekleyin.
result = arabalar + ["Audi","Nissan"]
# 11- Listenin son elemanını silin.
del arabalar[-1]
result = arabalar
# 12- Liste elemanlarını tersten yazdırınız.
result = arabalar[::-1]
# 13- Aşağıdaki verileri bir liste içinde saklayınız. 
    # studentA: Ömer Faruk Ballı 2000, (90,89,98)
    # studentB: Mehmet Bozkurt  1999, (97,80,99)
    # studentC: Emre Çimen 1998, (80,70,90) 
studentA = ['Ömer Faruk','Ballı',2000,[90,89,98]]
studentB = ['Mehmet','Bozkurt',1999,[97,80,99]]
studentC = ['Emre','Çimen',1998,[80,70,90]]
# 14- Liste elemanlarını ekrana yazdırınız.
result = studentA[3]
result = studentA[3][1]
result = f"{studentA[0]} {studentA[1]} {2021-studentA[2]} yaşında ve mat not ortalaması {(studentA[3][0]+studentA[3][1]+studentA[3][2])/3} "
print(result)
