#İdentity operator  is (reference karşılarştırır.)(adres)
liste1 = liste2 = [0,1,2,3,4,5,6,98]
liste3 = [0,1,2,3,4,5,6,98]
print(liste1 == liste2)
print(liste1 == liste3)
print(liste1 is not liste2)
print(liste1 is liste3)

#Membership Operator   in
liste4 =["Ömer","Bilge"]
print("Bilge" in liste4)
name = "Bilge"
print( "i" in name[:3])
print( "i" not in name[:3])

