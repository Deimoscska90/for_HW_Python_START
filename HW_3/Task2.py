#Задача 18: Требуется найти в массиве A самый близкий по величине элемент к заданному числу X. Если таких элементов несколько, 
#вы вывести один любой. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
#В последующих  строках записаны N целых чисел Ai (можно использовать псевдогенерацию). Последняя строка содержит число X
#*Пример:*
#5
#    7 -2 3 5 1
#    6
#    -> 7'''

import random
number = int(input('Введите число: '))
my_list = []
k = 0
closest_num = -1
for i in range(10):
    my_list.append(random.randint(-5,20))
    min = max(my_list) - number
    if int(my_list[i]) == number:
        k += 1
for i in set(my_list):
    if abs(i - number) < min:
        min = abs(i - number)
        closest_num = i
print(f'список {my_list}')
print(f'{k} раз встречается в заданном списке число {number}')
print(f'максимально близкое число {closest_num}')