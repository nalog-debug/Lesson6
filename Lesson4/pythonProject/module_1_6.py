my_dict = {'Vasya': 1975, 'Egor': 1999, 'Masha': 2002}
print(my_dict)
print(my_dict['Vasya'])
print(my_dict.get('Ivan'))
my_dict.update({'Ira': 2004,
                'Gena': 1998})
a = my_dict.pop('Egor')
print(a)
print(my_dict)
my_set = {1, 6, 6, 4, 8, 2, 3, 3, 4}
print(my_set)
print(my_set.add(5))
print(my_set.add(7))
print(my_set.discard(3))
print(my_set)
