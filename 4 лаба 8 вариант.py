import numpy as np
import matplotlib.pyplot as plt

# Функция для проверки простого числа
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Функция для генерации нижнетреугольной матрицы G из A
def lower_triangular(A):
    return np.tril(A)

# Функция для вычисления выражения (AТ + G-1 - F-1) * K
def calculate_expression1(A, G, F, K):
    return (np.transpose(A) + np.linalg.inv(G) - np.linalg.inv(F)) * K

# Функция для вычисления выражения A-1 * AT - K * F
def calculate_expression2(A, AT, F, K):
    return np.linalg.inv(A) @ AT - K * F

# Функция для проверки условия и обмена матриц
# Функция для проверки условия и обмена матриц
def check_and_swap(A, B, C, D, E, F):
    num_primes_C = np.sum([1 for j in range(C.shape[1]) if j % 2 != 0 and is_prime(np.sum(C[:, j]))])
    num_zeros_B = np.sum([1 for i in range(B.shape[0]) if i % 2 == 0 and np.count_nonzero(B[i]) == 0])

    if num_primes_C > num_zeros_B:
        return E, C
    else:
        return C, B

# Функция для генерации специальной матрицы F и последующих вычислений
def generate_special_matrix_and_compute(A, K):
    N = A.shape[0]
    F = np.copy(A)
    B, C, D, E = np.split(F, 4)

    # Обмен матриц в соответствии с условием
    C, swapped_matrix = check_and_swap(A, B, C, D, E, F)

    # Проверка условия определителя
    det_A = np.linalg.det(A)
    diag_sum_F = np.trace(F)
    if det_A > diag_sum_F:
        expression = calculate_expression1(A, lower_triangular(A), swapped_matrix, K)
    else:
        AT = np.transpose(A)
        expression = calculate_expression2(A, AT, swapped_matrix, K)

    return expression

# Функция для отображения графика матрицы
def plot_matrix(matrix, title):
    plt.imshow(matrix, cmap='viridis')
    plt.colorbar()
    plt.title(title)
    plt.show()

# Пример использования:
K = int(input("Введите размер подматрицы K: "))
N = int(input("Введите размер матрицы N (N >= K): "))

if N < K:
    print("Размер матрицы должен быть больше или равен размеру подматрицы.")
else:
    A = np.random.randint(-10, 10, size=(N, N))
    print("Матрица A сформирована:")
    print(A)

    F = generate_special_matrix_and_compute(np.copy(A), K)
    print("Матрица F сформирована:")
    print(F)

    # Покажем первую половину матрицы F
    plot_matrix(F[:N//2, :N//2], "Первая половина матрицы F")

    # Покажем вторую половину матрицы F
    plot_matrix(F[N//2:, N//2:], "Вторая половина матрицы F")

    # Покажем всю матрицу F
    plot_matrix(F, "Матрица F целиком")