'''
Задание состоит из двух частей.
1 часть – написать программу в соответствии со своим вариантом задания. Написать 2 варианта формирования
(алгоритмический и с помощью функций Питона), сравнив по времени их выполнение.

2 часть – усложнить написанную программу, введя по своему усмотрению в условие минимум одно ограничение
на характеристики объектов (которое будет сокращать количество переборов)  и целевую функцию для
нахождения оптимального  решения.

Вариант 8:
Вывести все натуральные числа до n, в записи которых встречается ровно одна единица.
'''

import time

#1
start = time.perf_counter()
n = int(input("Введите число n: "))

print("\nЧасть 1:\nАлгоритмический подход:\n")
for i in range(1, n+1):
    count = 0
    for digit in str(i):
        if digit == '1':
            count += 1
    if count == 1:
        print(i)
end = time.perf_counter()
execution_time = end - start
print(f"\nВремя выполнения: {execution_time} секунд\n")

frst = time.perf_counter()
print("//////////////////////////////////\n\nФункциональный подход:\n")
for i in range(1, n+1):
    count = sum(1 for digit in str(i) if digit == '1')
    if count == 1:
        print(i)
end1 = time.perf_counter()
execution_time1 = end1 - frst
print(f"\nВремя выполнения: {execution_time1} секунд")
print(f"Разница по времени выполнения: {abs(execution_time1 - execution_time)} сек")


#2
sec = time.perf_counter()
print("\n//////////////////////////////////\n\nЧасть 2:\nУсложненный алгоритмический подход:\n")
for i in range(1, n+1):
    count = 0
    for digit in str(i):
        if digit == '1':
            count += 1
    if count == 1 and '6' in str(i):
        print(i)
end2 = time.perf_counter()
execution_time2 = end2 - sec
print(f"\nВремя выполнения: {execution_time2} секунд\n")

thrd = time.perf_counter()
print("//////////////////////////////////\n\nУсложненный функциональный подход:\n")
for i in range(1, n+1):
    count = sum(1 for digit in str(i) if digit == '1')
    if count == 1 and '6' in str(i):
        print(i)
end3 = time.perf_counter()
execution_time3 = end3 - thrd
print(f"\nВремя выполнения: {execution_time1} секунд")
print(f"Разница по времени выполнения: {abs(execution_time3 - execution_time2)} сек")