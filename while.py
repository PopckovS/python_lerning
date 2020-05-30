#! /usr/bin/python3

'''Цикл while'''
start_block = '========='

# ======================
'''Обычный цикл while - выводим i, до тех пор, пока i будет меньше 6'''
print(start_block)
i = 1
while i < 6:
    print(i)
    i += 1
# Answer:


# ======================
'''Прерывание цикла как и в цикле for методом break'''
print(start_block)
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1
# Answer:


# ======================
'''Как и в цикле for можно пропускать работу цикла'''
print(start_block)
i = 1
while i < 6:
    print(i)
    i += 1
    if i == 3:
        continue
# Answer:
