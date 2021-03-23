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
if (0 <= kg_index and 18.4>kg_index):
    print(f"{name} kilo indeksin : {kg_index} ve kilo değerlendirmen zayıftır.")
elif (18.5 <= kg_index and 24.9>kg_index):
    print(f"{name} kilo indeksin : {kg_index} ve kilo değerlendirmen normal.")
elif (24.9 <= kg_index and 29.9>kg_index):
    print(f"{name} kilo indeksin : {kg_index} ve kilo değerlendirmen kilolu.")
elif (30 <= kg_index and 34.9>kg_index):
    print(f"{name} kilo indeksin : {kg_index} ve kilo değerlendirmen aşırı kilolu.")