# Задайте натуральное число N.
# Напишите программу, которая составит список простых множителей числа N.
# *Пример*
# - при N=236     ->        [2, 2, 59]
# 2,3,5,7,11,13

number = int(input("Введите число: "))
factor_list = [2, 3, 5, 7, 11, 13]
factors = []

for i in factor_list:
    while(number % i == 0):
        factors.append(i)
        print("i = ", i)
        print(number)
        number = number // i
        print(number)

if number > 1:
    factors.append(number)

print(factors)
