website = "https://github.com/omerfarballi"
course  = "Python 3.9  Python Dersleri "
# 1-  ' Merhaba Dünya  ' karakter dizisinin baş ve sondaki boşluk karakterlerini silin.
# result = ' Merhaba Dünya  '.strip()
# result = ' Merhaba Dünya  '.lstrip()
# result = ' Merhaba Dünya  '.rstrip()

# result = website.lstrip('/:pths')

# 2- 'Merhaba Güneş' içindeki Güneş bilgisi haricindeki her karakteri silin.
result = 'Merhaba Güneş'
result = result.strip('Merhaba ')

# 3-  'course' karakter dizisinin tüm karakterlerini küçük harf yapın.
# result = course.lower()
# result = course.upper()
# result = course.title()
# 4- 'website' içinde kaç tane a karakteri vardır ? (count('a'))
result = website.count('a')
result = website.count('www')
result = website.count('mer',0,25)
result = website.count('mer')

# 5- 'website' "www" ile başlayıp com ile bitiyor mu?
# result = website.startswith('www')
# result = website.startswith('http')
# result = website.endswith('lli')
# 6-  'website' içinde '.com' ifadesi var mı?
# result = website.find('.com')
# result = website.find('git',0,10)
# result = course.find('Python')
# result = course.rfind('Python')

# 7- 'course' içindeki karakterlerin hepsi alfabetik mi? (isalpha, isdigit)

# result = course.isalpha()
# result = 'Merhaba'.isalpha()
result = course.isdigit()
result = '123'.isdigit()

# 8- 'Merhaba' ifadesini satırda 20 karakter içine yerleştirip sağ ve soluna * ekleyiniz.
result = 'Merhaba'.center(20, '*')
result = 'Merhaba'.ljust(30, '*')
result = 'Merhaba'.rjust(50, '*')

# 9-  'course' karakter dizisindeki tüm boşluk karakterlerini '-' ile değiştirin.
result = course.replace(' ', '-')
result = course.replace(' ', '-',2)
result = course.replace(' ', '')

# 10- 'Merhaba Dünya' karakter dizisinin 'Dünya' ifadesini 'Mars' olarak değiştirin
result = 'Merhaba Dünya'.replace('Dünya','Mars')

# 11-  'course' karakter dizisini boşluk karakterlerinden ayırın.
result = course.split(' ')

print(result)   
print(result[1])
print(result[5])
