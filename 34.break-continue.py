# name = 'Ömer ve Bilge'
# for letter in name:
#     if letter == ' ':
#         continue
#         #break
#     print(letter)
# x=0
# while  x<15:
#     x += 1
#     if x % 2 == 1:
#         continue
#     print(x)
#1-1000 olan çift sayıların toplamını
x = 0
toplam = 0
while x <= 1000:
    x += 1
    if x % 2 == 0:
        continue
    toplam += x
print(toplam)
