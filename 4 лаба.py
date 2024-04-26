'''
С клавиатуры вводится два числа K и N. Квадратная матрица А(N,N), состоящая из
4-х равных по размерам подматриц, B,C,D,E заполняется случайным образом целыми
числами в интервале [-10,10]. Для отладки использовать не случайное заполнение,
а целенаправленное. Вид матрицы А:

В	С
D	Е

Формируется матрица F следующим образом: скопировать в нее А и
если в С количество минимальных чисел в нечетных столбцах, чем количество
максимальных чисел в четных строках, то поменять местами В и С симметрично,
иначе С и Е поменять местами несимметрично. При этом матрица А не меняется.
После чего если определитель матрицы А больше суммы диагональных элементов матрицы F,
то вычисляется выражение: A-1*A – K * F, иначе вычисляется выражение (AТ +GТ-F-1)*K,
где G-нижняя треугольная матрица, полученная из А. Выводятся по мере формирования А, F
и все матричные операции последовательно.
'''
import numpy as np
import matplotlib.pyplot as plt
from sympy import isprime

# Векторизованная функция для проверки на простоту
is_prime_vect = np.vectorize(isprime)

# Функция для отображения матрицы в виде тепловой карты
def plot_heatmap(matrix, title):
    plt.imshow(matrix, cmap='hot', interpolation='nearest')
    plt.title(title)
    plt.colorbar()
    plt.show()

# Функция для отображения матрицы в виде графика сетки
def plot_grid(matrix, title):
    plt.spy(matrix)
    plt.title(title)
    plt.show()

# Функция для отображения матрицы в виде гистограммы значений
def plot_histogram(matrix, title):
    plt.hist(matrix.ravel(), bins=range(-10, 11))
    plt.title(title)
    plt.show()
def plot_matrix(matrix, title):
    plt.matshow(matrix)
    plt.title(title)
    plt.colorbar()
    plt.show()

# Создание матрицы A с целенаправленным заполнением
def create_matrix(N):
    return np.random.randint(-10, 11, size=(N, N))


# Подсчёт простых чисел в нечётных столбцах и нулей в чётных строках
def count_primes_zeros(C, E):
    primes = np.sum(is_prime_vect(C[:, 0::2]))
    zeros = np.sum(E[1::2, :] == 0)
    return primes, zeros


# Формирование матрицы F
def form_matrix_F(A, B, C, D, E):
    N = A.shape[0]
    F = A.copy()
    primes, zeros = count_primes_zeros(C, E)
    if primes > zeros:
        F[N // 2:, :N // 2], F[:N // 2, N // 2:] = E.copy(), C.copy()
    else:
        F[:N // 2, :N // 2], F[:N // 2, N // 2:] = C.copy(), B.copy()
    return F


# Вычисление результата
def calculate_result(A, F, K):
    det_A = np.linalg.det(A)
    trace_F = np.trace(F)
    if det_A > trace_F:
        return np.linalg.inv(A) @ A.T - K * F
    else:
        G = np.tril(A)
        return (A.T + np.linalg.inv(G) - np.linalg.inv(F)) * K


# Визуализация матриц
def visualize_matrices(*matrices, titles):
    n = len(matrices)
    fig, axes = plt.subplots(1, n, figsize=(n * 5, 5))
    for i, matrix in enumerate(matrices):
        ax = axes[i] if n > 1 else axes
        im = ax.imshow(matrix, cmap='viridis')
        ax.set_title(titles[i])
        plt.colorbar(im, ax=ax)
    plt.show()


# Основная функция
def main():
    K = int(input("Введите число K: "))
    N = int(input("Введите размер матрицы N (должен быть четным): "))

    A = create_matrix(N)
    B, C, D, E = A[:N // 2, :N // 2], A[:N // 2, N // 2:], A[N // 2:, :N // 2], A[N // 2:, N // 2:]
    F = form_matrix_F(A, B, C, D, E)
    result = calculate_result(A, F, K)

    # Вывод результата
    print("Результат вычислений:")
    print(result)

    # Выводим графики
    plot_heatmap(A, "Тепловая карта матрицы A")
    plot_grid(F, "График сетки матрицы F")
    plot_histogram(result, "Гистограмма значений матрицы result")


main()
