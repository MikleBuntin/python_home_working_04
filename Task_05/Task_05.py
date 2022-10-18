# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
# Коэффициенты могут быть как положительными, так и отрицательными.
# Степени многочленов могут отличаться.
#


import random
# import re
import math
def generate_polynomial(rate):
    string_result = str()
    while rate > 1:
        string_result = string_result + str(random.randint(-10, 10)) + "x^" + str(rate) + " + "
        rate -= 1
    string_result = string_result + str(random.randint(-10, 10)) + "x" + " + " + str(random.randint(-100, 100)) + " = 0"
    return(string_result)


rate_01 = int(input("Введите степень для первого многочлена: "))
rate_02 = int(input("Введите степень для второго многочлена: "))

with open('polynomial_01.txt', 'w') as file_01:
    file_01.writelines(generate_polynomial(rate_01))

with open('polynomial_02.txt', 'w') as file_02:
    file_02.writelines(generate_polynomial(rate_02))


file_01 = 'polynomial_01.txt'
first_polynomial_str = open(file_01, 'r')
first_polynomial_array = first_polynomial_str.read()
first_polynomial_array = first_polynomial_array.replace('+', '')
first_polynomial_array = first_polynomial_array.replace('=', '')
first_polynomial_array = first_polynomial_array.split()
# print(first_polynomial_array)

file_02 = 'polynomial_02.txt'
second_polynomial_str = open(file_02, 'r')
second_polynomial_array = second_polynomial_str.read()
second_polynomial_array = second_polynomial_array.replace('+', '')
second_polynomial_array = second_polynomial_array.replace('=', '')
second_polynomial_array = second_polynomial_array.split()

# print(second_polynomial_array)

result_polynomial_array_reversed = []
if len(first_polynomial_array) > len(second_polynomial_array):
    count = 0
    for count in range(0, len(second_polynomial_array)):
        k_first = int(first_polynomial_array[len(first_polynomial_array) - count - 1].split('x', )[0])
        k_second = int(second_polynomial_array[len(second_polynomial_array) - count - 1].split('x', )[0])
        result_polynomial_array_reversed.append(k_first + k_second)
    for count in range(len(second_polynomial_array), len(first_polynomial_array)):
        result_polynomial_array_reversed.append(int(first_polynomial_array[len(first_polynomial_array) - count - 1].split('x', )[0]))
else:
    count = 0
    for count in range(0, len(first_polynomial_array)):
        k_first = int(first_polynomial_array[len(first_polynomial_array) - count - 1].split('x', )[0])
        k_second = int(second_polynomial_array[len(second_polynomial_array) - count - 1].split('x', )[0])
        result_polynomial_array_reversed.append(k_first + k_second)
    for count in range(len(first_polynomial_array), len(second_polynomial_array)):
        result_polynomial_array_reversed.append(int(second_polynomial_array[len(second_polynomial_array) - count - 1].split('x', )[0]))

# print(result_polynomial_array_reversed)

result_polynomial_str = str()
count = len(result_polynomial_array_reversed) - 1
if result_polynomial_array_reversed[count] >= 0:
    result_polynomial_str = result_polynomial_str + " + "
else:
    result_polynomial_str = result_polynomial_str + " - "
result_polynomial_str = str(result_polynomial_array_reversed[count]) + "x^" + str(count - 1)

for count in range(len(result_polynomial_array_reversed) - 2, 2, -1):
    if result_polynomial_array_reversed[count] >= 0:
        result_polynomial_str = result_polynomial_str + " + "
    else:
        result_polynomial_str = result_polynomial_str + " - "
    result_polynomial_str = result_polynomial_str + str(abs(result_polynomial_array_reversed[count])) + "x^" + str(count - 1)\

if result_polynomial_array_reversed[2] >= 0:
    result_polynomial_str = result_polynomial_str + " + "
else:
    result_polynomial_str = result_polynomial_str + " - "

result_polynomial_str = result_polynomial_str + str(abs(result_polynomial_array_reversed[2])) + "x"\

if result_polynomial_array_reversed[1] >= 0:
    result_polynomial_str = result_polynomial_str + " + "
else:
    result_polynomial_str = result_polynomial_str + " - "

result_polynomial_str = result_polynomial_str + str(abs(result_polynomial_array_reversed[1])) + " = 0"

with open('result_polynomial.txt', 'w') as result_file:
    result_file.writelines(result_polynomial_str)

print("Сумма многочленов: ", result_polynomial_str, " записана в файл result_polynomial.txt")