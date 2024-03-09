#Вариант 8
#Шестнадцатеричные целые числа. Максимальное число выводить прописью на английском.

digit_to_word = {
    '0': 'zero',
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine',
    'A': 'ten',
    'B': 'eleven',
    'C': 'twelve',
    'E': 'fourteen',
    'F': 'fifteen'
}

with open('input.txt', 'r') as f:
    s = f.read(1000)
    max_decimal = 0
    max_hex = ''

    while s:
        if not s:
            print('empty file')
        n = s.split()

        for i in n:
            try:
                if "'" in i or '"' in i:
                    i = i[1:-1]
                decimal_value = int(i, 16)
                if decimal_value > max_decimal:
                    max_decimal = decimal_value
                    max_hex = i
            except ValueError:
                continue

        s = f.read(1000)

    if max_hex:
        max_hex_word = ''
        for char in max_hex:
            max_hex_word += digit_to_word[char]
        print("Наибольшее число в десятичной системе:", max_decimal)
        print("Словесное представление наибольшего числа:", max_hex_word)
    else:
        print("В файле нет шестнадцатеричных чисел.")
