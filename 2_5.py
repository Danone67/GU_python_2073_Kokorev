from copy import deepcopy

price_list = [57.08, 46.51, 97, 51, 1.76, 20, 25.08, 76, 23.34, 98.90,
	          70.01, 63, 39, 90.47, 29, 24, 42, 59.11, 45.78, 48.29,
	          8.53, 67, 95, 5.62, 11, 18.34, 13, 64.80, 78, 93, 88.08]
print(id(price_list)) # id до сортировки
my_list = deepcopy(price_list) #написал код, потом понял, что список не надо было трогать, пришлось так выкрутиться
for i, r in enumerate(my_list):
    my_list[i] = str(my_list[i])
    my_list[i] = my_list[i].rsplit('.')
    if len(my_list[i]) < 2:
        my_list[i].append(str(0))
        my_list[i][-1] = my_list[i][-1].zfill(2)
    else:
        my_list[i][1] = my_list[i][1].zfill(2)
    print(f'{my_list[i][0]} руб {my_list[i][1]} коп' , end = ', ')
print()
price_list.sort()
print(price_list)
print(id(price_list)) #id после сортировки

price_list_s = sorted(price_list, reverse=True)
print(price_list_s)
print(id(price_list_s))

i = 4
print('Самые дорогие товары по возрастанию ')
while i > -1:
    price_list_s[i] = str(price_list_s[i])
    price_list_s[i] = price_list_s[i].rsplit('.')
    if len(price_list_s[i]) < 2:
        price_list_s[i].append(str(0))
        price_list_s[i][-1] = price_list_s[i][-1].zfill(2)
    else:
        price_list_s[i][1] = price_list_s[i][1].zfill(2)
    print(f'{price_list_s[i][0]} руб {my_list[i][1]} коп', end=', ')
    i -= 1

#Минмум кода в этот раз не вышло