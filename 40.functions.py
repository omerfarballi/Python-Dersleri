def say_hello(name="user"):
    print(f"Hello {name}")
    return " return tarafından geriye gönderilmiş isim : " + name 
print("merhaba")
say_hello("Ömer")
say_hello("Bilge")
hello = say_hello("Faruk")
print(hello)

def sum(number1,number2):
    result = number1 + number2
    return result
number1 = int(input("Sayı 1 :"))
number2 = int(input("Sayı 2 :"))
result = sum(number1,number2)
print("Return komutuyla geri dönderilmiş sonuç : " ,result)
def divide(number1,number2):
    return number1/number2
result2 = divide(number1=number2,number2=number1)
def divide(number1,number2,number3):
    return (number1/number2)+number3
result3 = divide(number2=number2,number1=number1,number3=0)
print(result2,result3)
