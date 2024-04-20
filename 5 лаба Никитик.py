import math
import timeit
import matplotlib.pyplot as plt

def recursive_F(n):
    if n == 0 or n == 1:
        return 3
    else:
        return (-1)**n * (recursive_F(n-1) / math.factorial(n) - recursive_F(n-2) / math.factorial(2*n))


def iterative_F(n):
    if n == 0 or n == 1:
        return 3

    F_n_minus_1 = 3
    F_n_minus_2 = 3
    F_n = 0

    for i in range(2, n + 1):
        F_n = (-1)**i * (F_n_minus_1 / math.factorial(i) - F_n_minus_2 / math.factorial(2*i))
        F_n_minus_2, F_n_minus_1 = F_n_minus_1, F_n

    return F_n



# Измерение времени выполнения
def measure_time(function, n):
    start_time = timeit.default_timer()
    function(n)
    return timeit.default_timer() - start_time

# Сравнение времени выполнения
recursive_times = []
iterative_times = []
n_values = range(1, 10)  # Ограничим n для рекурсивного метода малым значением, чтобы избежать переполнения стека

for n in n_values:
    recursive_times.append(measure_time(recursive_F, n))
    iterative_times.append(measure_time(iterative_F, n))

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