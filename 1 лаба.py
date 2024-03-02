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