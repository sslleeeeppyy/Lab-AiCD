#Вариант 8
#Шестнадцатеричные целые числа. Максимальное число выводить прописью на английском.

slovar = {
    '0': 'zero',
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine'
}

with open('input.txt','r') as f:
    s = f.read()
    if not s:
        print('empty file')
    n = s.split()
    print(n)
    m = '0'
    for i in n:
        try:
            if "'" in i or '"' in i:
                i = i[1:-1]
            u = str(int(i, 16))
        except ValueError:
            continue

        if int(i, 16) > int(m, 16):
            m = i
    print("Ответ:", m)
f.close()