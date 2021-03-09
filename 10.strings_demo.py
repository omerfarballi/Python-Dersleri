website = "https://github.com/omerfarballi"
course = "Python 3.9 Dersleri"
lenght = len(website)
# 1- "course" değişkeninin uzunluğunu bulun
result = len(course)
# 2- "website" değişkeni içerisinden github karakterlerini alın
result = website[8:14]

# 3- "website" değişkeni içerisinden omerfarballi karakterlerini alın
result = website[19:]
result = website[lenght-12:]

# 4- "course" değişkeni içerisinden son 5 ve ilk 5 karakteri alın 
result = course[-5:]
result = course[:5]

# 5- "course" değişkeni tersten yazdırın
result = course[::-1]
numbers = "1234567890" *5
# print(numbers[::10])


name , surname , age , job = 'Mehmet' , 'Bozkurt' , 26 , 'Doktor'
# 6- Yukarıdaki değişkenleri şu şekilde yazdırın
# 'Benim adim  Mehmet soyadim Bozkurt yaşım  26 ve Mesleğim doktor.'
result = 'Benim adım '+name + ' ' + "soyadım "+surname + " Yaşım " + str(age)  + " ve Mesleğim " + job
result = "Benim adım {} soyadım {} Yaşım {} ve Mesleğim {}".format(name,surname,age,job)
result =f'Benim adım {name} soyadım {surname} Yaşım {age} ve "Mesleğim" {job}'

# 7- 'Hello world' kelimesindek w ile W yer değiştirin
result = 'Hello world'
result = result[0:6] + 'W' + result[7:]

# 8- 'xyz' kelimesini 5 kez yanyana yazdırın
result = 'xyz'*5

print(result)
print("abc"*5)