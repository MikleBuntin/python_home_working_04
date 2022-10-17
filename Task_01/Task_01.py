# Вычислить число π c заданной точностью d
# *Пример: - при $d = 0.001, π = 3.141.$
# $10^{-1} ≤ d ≤10^{-10}$

accuracy = int(input("Введите число знаков после запятой: "))
pi = 0
for d in range (0, accuracy):
    pi = pi + 1 / 16 ** d * (4 / (8 * d + 1) - 2 / (8 * d + 4) - 1 / (8 * d + 5) - 1 / (8 * d + 6))

pi_int = pi * 10 ** accuracy
pi = int(pi_int) / 10 ** accuracy

print(pi)
