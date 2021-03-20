x = 7
result = 7 <= x < 12
# and 
# true,false => false
# true,true => true
# false,false => false
# false,true => false
result = (7 < x) and (x < 12 )
# or 
result = (7 < x) or (x % 2 == 0)
# true,false => true
# true,true => true
# false,false => false
# false,true => true
# not
result = not (x>0)
# x sayısı 0-50 olan bir tek dsayı mıdır?
result = (x>0 and x<50) and (x % 2 == 1)

print(result)
