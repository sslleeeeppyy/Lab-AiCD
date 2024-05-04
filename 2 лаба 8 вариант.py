'''
Написать программу, которая читая символы из бесконечной последовательности
(эмулируется конечным файлом, читающимся поблочно), распознает, преобразует и
выводит на экран лексемы по определенному правилу. Лексемы разделены пробелами.
Преобразование делать по возможности через словарь. Для упрощения под выводом числа
прописью подразумевается последовательный вывод всех цифр числа.

Вариант 8.
Шестнадцатеричные целые числа. Максимальное число выводить прописью на английском.
'''
import re

# Словарь для перевода цифр в пропись
digits_to_words = {
    '0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four',
    '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine',
    'A': 'ten', 'B': 'eleven', 'C': 'twelve', 'D': 'thirteen', 'E': 'fourteen', 'F': 'fifteen'
}

def hex_to_words(hex_number):
    return ' '.join(digits_to_words[digit] for digit in hex_number)

def find_max_hex_number(file_path):
    hex_pattern = re.compile(r'\b[0-9A-F]+\b', re.IGNORECASE)
    max_hex = None
    max_dec = -1

    with open(file_path, 'r') as file:
        for block in iter(lambda: file.read(1024), ''):
            for match in re.finditer(hex_pattern, block):
                current_hex = match.group()
                current_dec = int(current_hex, 16)
                if current_dec > max_dec:
                    max_dec = current_dec
                    max_hex = current_hex

    return max_hex

# Путь к вашему файлу
file_path = 'txt.txt'
max_hex_number = find_max_hex_number(file_path)
if max_hex_number:
    print(f"Наибольшее число в файле: {max_hex_number}, в десятичной системе это: {hex_to_words(max_hex_number)}")
else:
    print("No hex numbers found.")