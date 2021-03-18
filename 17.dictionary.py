# cities = ["Mersin","Ankara"]
# plates = [33, 6 ]
# print(plates[cities.index("Mersin")])

# key - value
# dict = {"Mersin" : 33, "Ankara" : 6}
# dict['İstanbul'] = 34
# dict['Ankara'] = "New Value for Ankara"


# print(dict['Mersin'])
# print(dict)
users = {
    "Ömer Faruk Ballı":{
        "age":19,
        "role":["admin","user"],
        "mail":"omerfaruk@gmail.com",
        "phone":1235546132,
        "address":"Mersin Türkiye"
    },
    "Mehmet Bozkurt":{
        "age":20,
        "role":["user"],
        "mail":"bozkurt@gmail.com",
        "phone":1684564564,
        "address":"Mersin Türkiye"
    }
}
print(users["Ömer Faruk Ballı"]["role"][0])