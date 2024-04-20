'''С клавиатуры вводится два числа K и N. Квадратная матрица А(N,N),
состоящая из 4-х равных по размерам подматриц, B,C,D,E заполняется
случайным образом целыми числами в интервале [-10,10]. Для тестирования
использовать не случайное заполнение, а целенаправленное.
Для ИСТд-11 вид матрицы А

B	C
D	E

Вариант 8.

Формируется матрица F следующим образом: скопировать в нее А
и если в С количество простых чисел в нечетных столбцах,
чем количество нулевых  элементов в четных строках,
то поменять местами Е и С симметрично, иначе С и В поменять местами
несимметрично. При этом матрица А не меняется. После чего если
определитель матрицы А больше суммы диагональных элементов матрицы F,
то вычисляется выражение: A-1*AT – K * F, иначе вычисляется выражение (AТ +G-1-F-1)*K,
где G-нижняя треугольная матрица, полученная из А.
Выводятся по мере формирования А, F и все матричные операции последовательно.
'''

import numpy as np
import matplotlib.pyplot as plt

# Функция для проверки, является ли число простым
def is_prime(n):
    """Проверка числа на простоту."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Функция для подсчета простых чисел в нечетных столбцах матрицы
def count_primes_in_odd_columns(matrix):
    return np.sum([is_prime(x) for x in matrix[:, 1::2].flatten()])

# Функция для подсчета нулевых элементов в четных строках матрицы
def count_zeros_in_even_rows(matrix):
    return np.sum(matrix[::2, :] == 0)

# Ввод K и N
K = int(input("Введите K: "))
N = int(input("Введите N: "))

# Создаем квадратную матрицу A размером N x N и заполняем ее случайными числами
A = np.random.randint(-10, 11, (N, N))

# Для отладки можно использовать целенаправленное заполнение
# A = np.array([...])

# Подматрицы B, C, D, E
mid = N // 2
B = A[:mid, :mid]
C = A[:mid, mid:]
D = A[mid:, :mid]
E = A[mid:, mid:]

# Формирование матрицы F
F = A.copy()
if count_primes_in_odd_columns(C) > count_zeros_in_even_rows(C):
    # Меняем E и C симметрично
    F[:mid, mid:], F[mid:, mid:] = E.copy(), C.copy()
else:
    # Меняем C и B несимметрично
    F[:mid, mid:], F[:mid, :mid] = B.copy(), C.copy()

# Вычисление выражения
if np.linalg.det(A) > np.trace(F):
    result = np.linalg.inv(A).dot(A.T) - K * F
else:
    G = np.tril(A)  # Нижняя треугольная матрица из A
    result = (A.T + np.linalg.inv(G) - np.linalg.inv(F)) * K

# Вывод матриц
print("Матрица A:")
print(A)
print("Матрица F:")
print(F)
print("Результат вычислений:")
print(result)

# Функция для отображения матрицы в виде графика
def plot_matrix(matrix, title):
    plt.figure(figsize=(6, 6))
    plt.matshow(matrix, fignum=1)
    plt.title(title)
    plt.colorbar()
    plt.show()

# Выводим графики
plot_matrix(A, "Матрица A")
plot_matrix(F, "Матрица F")
plot_matrix(result, "Результат вычислений")