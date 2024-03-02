#Вариант 8
#Шестнадцатеричные целые числа. Максимальное число выводить прописью на английском.

with open('input.txt','r') as f:
    s = f.read(1000)
    if not s:
        print('empty file')
    n = s.split()
    print(n)
    m = '0'
    for i in n:
        if int(i, 16) > int(m, 16):
            m = i
    print(m)
f.close()