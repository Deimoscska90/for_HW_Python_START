#Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит 
#число А в целую степень B с помощью рекурсии.



def power(x, n):
    if n == 0:
        return 1
    if n % 2 == 0:
        return power(x, n // 2) * power(x, n // 2)
    else:
       return power(x, n-1) * x
x = int(input())
n = int(input())
print(power(x, n))