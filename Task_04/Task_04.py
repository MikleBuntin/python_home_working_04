# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# *Пример:*
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random
rate = int(input("Введите степень: "))
string_result = str()
while rate > 1:
    string_result = string_result + str(random.randint(0, 100)) + "x^" + str(rate) + " + "
    rate -= 1
string_result = string_result + str(random.randint(0, 100)) + "x" + " + " + str(random.randint(0, 100)) + " = 0"
print(string_result)

data = open('file.txt', 'a')
data.writelines(string_result)
data.close()