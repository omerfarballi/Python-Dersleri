# def change_name(name_arg):
#     print(name_arg)
#     name_arg = 'mahmut'
#     print(name_arg)
# name = 'ışıl'
# change_name(name)
# print(name)
# def change_index(liste):
#     liste[0]= 58
# listee = [0,2,4,6,8]
# liste_slicing = listee[:3]
# print(listee)
# change_index(liste_slicing)
# print(liste_slicing)
# * tuple ; ** dict
# def add(*params):
#     print(params)
#     return sum((params))
# print(add(10,25,60))
# print(add(10,25,60,52,47,58))
# print(add(10,25,60,98,85,75,41))
def display_user(**args):
    print(type(args))
    for key, value in args.items():
        print('{} is {} '.format(key,value))
display_user(name = 'Bilge', age = 20, city = 'İstanbul')
