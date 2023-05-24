#Задача 34

def ryfma(str):
    str = str.split()
    list = []
    for words in str:
        result = 0
        for i in words:
            if i in 'аеёиоуыэюя':
                result += 1
        list.append(result)
    return len(list) == list.count(list[0])

print('Введите: пара-ра-рам рам-пам-папам па-ра-па-дам')
str = input()
if ryfma(str):
    print('Парам пам-пам')
else:
    print('Пам парам')