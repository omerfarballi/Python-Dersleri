# Kişinin ad, kilo ve boy bilgilerini alıp kilo indekslerini hesaplayınız.
#    Formül: (Kilo / boy uzunluğunun karesi)
#    Aşağıdaki tabloya göre kişi hangi gruba girmektedir.
#    0-18.4    => Zayıf 
#    18.5-24.9 => Normal  
#    25.0-29.9 => Fazla Kilolu
#    30.0-34.9 => Şişman
name = input("İsminiz : ") # string
kg = float(input("Kilonuz : "))
height = float(input("Boyunuz : ")) #metre 
kg_index = kg / (height**2)
zayif = kg_index<=18.4 and kg_index>0
normal = kg_index<=24.9 and kg_index>18.4
kilolu = kg_index<=29.9 and kg_index>24.9
asırı_kilolu = kg_index<=34.9 and kg_index>29.9


print(f"{name} kilo indeksin : {kg_index} ve kilo değerlendirmen zayıf {zayif} ")
print(f"{name} kilo indeksin : {kg_index} ve kilo değerlendirmen normal{normal} ")
print(f"{name} kilo indeksin : {kg_index} ve kilo değerlendirmen  kilolu{kilolu} ")
print(f"{name} kilo indeksin : {kg_index} ve kilo değerlendirmen aşırı kilolu{asırı_kilolu} ")
