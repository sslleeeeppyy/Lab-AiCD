import time

def chet(number):
    return number % 2 == 0

def odin_v_chisle(number):
    return str(number).count('1') == 1

def chet_plus_odin(n, even_only=False):
    result = []
    for i in range(1, n+1):
        if even_only and not chet(i):
            continue
        if odin_v_chisle(i):
            result.append(i)
    return result

# Часть 1
n = int(input("Введите число n: "))

start = time.perf_counter()
print("\nЧасть 1:\nАлгоритмический подход:\n")
numbers = chet_plus_odin(n)
for number in numbers:
    print(number)
end = time.perf_counter()
execution_time = end - start
print(f"\nВремя выполнения: {execution_time} секунд\n")

start = time.perf_counter()
print("//////////////////////////////////\n\nФункциональный подход:\n")
numbers = [i for i in range(1, n+1) if odin_v_chisle(i)]
for number in numbers:
    print(number)
end = time.perf_counter()
execution_time1 = end - start
print(f"\nВремя выполнения: {execution_time1} секунд")
print(f"Разница по времени выполнения: {abs(execution_time1 - execution_time)} сек")

# Часть 2
start = time.perf_counter()
print("\nЧасть 2:\nАлгоритмический подход:\n")
numbers = chet_plus_odin(n, even_only=True)
for number in numbers:
    print(number)
end = time.perf_counter()
execution_time = end - start
print(f"\nВремя выполнения: {execution_time} секунд\n")

start = time.perf_counter()
print("//////////////////////////////////\n\nФункциональный подход:\n")
numbers = [i for i in range(1, n+1) if chet(i) and odin_v_chisle(i)]
for number in numbers:
    print(number)
end = time.perf_counter()
execution_time1 = end - start
print(f"\nВремя выполнения: {execution_time1} секунд")
print(f"Разница по времени выполнения: {abs(execution_time1 - execution_time)} сек")
