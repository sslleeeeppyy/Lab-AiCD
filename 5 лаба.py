'''
Задана рекуррентная функция. Область определения функции – натуральные числа.
Написать программу сравнительного вычисления данной функции рекурсивно и итерационно.
Определить границы применимости рекурсивного и итерационного подхода. Результаты сравнительного
исследования времени вычисления представить в табличной и графической форме.

F(0) = F(1) = 3; F(n) = (-1)n*(F(n-1)/n!- F(n-2) /(2n)!)


'''

import math
import timeit
import matplotlib.pyplot as plt

def factorial(n):
    return math.factorial(n)
sign1 = 1
def recursive_F(n, cache={0: 3, 1: 3}):
    global sign1
    if n in cache:
        return cache[n]
    else:
        sign1 *= (-1)
        result = sign1 * (recursive_F(n-1, cache) / factorial(n) - recursive_F(n-2, cache) / factorial(2*n))
        cache[n] = result
        return result
sign = 1
def iterative_F(n):
    if n == 0 or n == 1:
        return 3
    F_n_minus_1 = 3
    F_n_minus_2 = 3
    F_n = 0

    for i in range(2, n + 1):
        global sign
        sign *= (-1)
        F_n = sign * (F_n_minus_1 / factorial(i) - F_n_minus_2 / factorial(2*i))
        F_n_minus_2, F_n_minus_1 = F_n_minus_1, F_n

    return F_n

# Измерение времени выполнения
def measure_time(function):
    start_time = timeit.default_timer()
    function()
    return timeit.default_timer() - start_time

# Сравнение времени выполнения
recursive_times = []
iterative_times = []
n_values = range(1, 10)

for n in n_values:
    recursive_times.append(measure_time(lambda: recursive_F(n)))
    iterative_times.append(measure_time(lambda: iterative_F(n)))

# Вывод результатов в табличной форме
print("n | Recursive Time | Iterative Time")
for n, rec_time, iter_time in zip(n_values, recursive_times, iterative_times):
    print(f"{n} | {rec_time:.6f} | {iter_time:.6f}")

# Построение графиков
plt.plot(n_values, recursive_times, label='Recursive')
plt.plot(n_values, iterative_times, label='Iterative')
plt.xlabel('n')
plt.ylabel('Time (seconds)')
plt.legend()
plt.show()
