immutable_var = ['Hello'], True, 1, 2, 3
print(immutable_var)
# immutable_var[2] = 200
# print(immutable_var)
# Изменить нельзя, потомучто значение данной переменной относится
# к неизменяемому объекту.
mutable_list = ['One', 'Two', 'Trhee']
mutable_list[0] = 'For'
print(mutable_list)