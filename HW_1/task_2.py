#Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали
#одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
#*Пример:*
#6 -> 1  4  1
#24 -> 4  16  4'''

S = int(input("Введите число: "))
if S % 6 == 0:
    Катя = int((S / 3) * 2)
    Петя = int((S / 3) / 2)
    Сережа = int((S / 3) / 2)
    print(Петя, Катя, Сережа)
else:
    print("Число не подходит!")